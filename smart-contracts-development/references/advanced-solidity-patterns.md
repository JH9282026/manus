# Advanced Solidity Patterns and Techniques

## Introduction

This reference covers advanced Solidity programming patterns, optimization techniques, and architectural decisions for building production-grade smart contracts. These patterns have been battle-tested in real-world applications and represent industry best practices.

## Upgradeable Contract Patterns

### Proxy Patterns

#### Transparent Proxy Pattern

**Architecture:**
- Proxy contract holds state and delegates calls to implementation
- Admin functions handled by proxy
- Regular functions delegated to implementation

**Implementation:**
```solidity
contract TransparentProxy {
    address public implementation;
    address public admin;
    
    constructor(address _implementation) {
        implementation = _implementation;
        admin = msg.sender;
    }
    
    modifier onlyAdmin() {
        require(msg.sender == admin, "Not admin");
        _;
    }
    
    function upgrade(address newImplementation) external onlyAdmin {
        implementation = newImplementation;
    }
    
    fallback() external payable {
        address impl = implementation;
        require(impl != address(0), "Implementation not set");
        
        assembly {
            calldatacopy(0, 0, calldatasize())
            let result := delegatecall(gas(), impl, 0, calldatasize(), 0, 0)
            returndatacopy(0, 0, returndatasize())
            
            switch result
            case 0 { revert(0, returndatasize()) }
            default { return(0, returndatasize()) }
        }
    }
}
```

**Advantages:**
- Clear separation between admin and user functions
- No function selector clashes
- Widely adopted (OpenZeppelin)

**Disadvantages:**
- Higher gas costs for admin checks
- More complex implementation

#### UUPS (Universal Upgradeable Proxy Standard)

**Architecture:**
- Upgrade logic in implementation contract
- Simpler proxy contract
- Lower gas costs

**Implementation:**
```solidity
// Proxy
contract UUPSProxy {
    address public implementation;
    
    constructor(address _implementation) {
        implementation = _implementation;
    }
    
    fallback() external payable {
        address impl = implementation;
        assembly {
            calldatacopy(0, 0, calldatasize())
            let result := delegatecall(gas(), impl, 0, calldatasize(), 0, 0)
            returndatacopy(0, 0, returndatasize())
            switch result
            case 0 { revert(0, returndatasize()) }
            default { return(0, returndatasize()) }
        }
    }
}

// Implementation
contract UUPSImplementation {
    address public implementation;
    address public admin;
    
    function upgradeTo(address newImplementation) external {
        require(msg.sender == admin, "Not admin");
        implementation = newImplementation;
    }
}
```

**Advantages:**
- Lower gas costs
- Simpler proxy
- Upgrade logic can be customized per implementation

**Disadvantages:**
- Risk of breaking upgrade mechanism
- Must ensure upgrade function in all implementations

#### Beacon Proxy Pattern

**Architecture:**
- Multiple proxies point to single beacon
- Beacon holds implementation address
- Upgrade all proxies by updating beacon

**Implementation:**
```solidity
contract Beacon {
    address public implementation;
    address public owner;
    
    constructor(address _implementation) {
        implementation = _implementation;
        owner = msg.sender;
    }
    
    function upgrade(address newImplementation) external {
        require(msg.sender == owner, "Not owner");
        implementation = newImplementation;
    }
}

contract BeaconProxy {
    address public beacon;
    
    constructor(address _beacon) {
        beacon = _beacon;
    }
    
    fallback() external payable {
        address impl = Beacon(beacon).implementation();
        assembly {
            calldatacopy(0, 0, calldatasize())
            let result := delegatecall(gas(), impl, 0, calldatasize(), 0, 0)
            returndatacopy(0, 0, returndatasize())
            switch result
            case 0 { revert(0, returndatasize()) }
            default { return(0, returndatasize()) }
        }
    }
}
```

**Advantages:**
- Upgrade multiple contracts simultaneously
- Efficient for factory patterns
- Clear upgrade path

**Disadvantages:**
- Additional beacon contract
- All proxies must upgrade together

### Storage Collision Prevention

**Problem:** Proxy and implementation share storage, risking collisions.

**Solution: EIP-1967 Storage Slots**
```solidity
contract EIP1967Storage {
    // bytes32(uint256(keccak256('eip1967.proxy.implementation')) - 1)
    bytes32 private constant IMPLEMENTATION_SLOT = 
        0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc;
    
    function _getImplementation() internal view returns (address impl) {
        bytes32 slot = IMPLEMENTATION_SLOT;
        assembly {
            impl := sload(slot)
        }
    }
    
    function _setImplementation(address newImplementation) internal {
        bytes32 slot = IMPLEMENTATION_SLOT;
        assembly {
            sstore(slot, newImplementation)
        }
    }
}
```

## Access Control Patterns

### Role-Based Access Control (RBAC)

**OpenZeppelin AccessControl:**
```solidity
import "@openzeppelin/contracts/access/AccessControl.sol";

contract MyContract is AccessControl {
    bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");
    bytes32 public constant BURNER_ROLE = keccak256("BURNER_ROLE");
    
    constructor() {
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(MINTER_ROLE, msg.sender);
    }
    
    function mint(address to, uint256 amount) public onlyRole(MINTER_ROLE) {
        // Minting logic
    }
    
    function burn(address from, uint256 amount) public onlyRole(BURNER_ROLE) {
        // Burning logic
    }
}
```

### Multi-Signature Pattern

**Implementation:**
```solidity
contract MultiSig {
    address[] public owners;
    uint256 public required;
    
    struct Transaction {
        address to;
        uint256 value;
        bytes data;
        bool executed;
        uint256 confirmations;
    }
    
    Transaction[] public transactions;
    mapping(uint256 => mapping(address => bool)) public confirmations;
    
    constructor(address[] memory _owners, uint256 _required) {
        require(_owners.length >= _required, "Invalid required");
        owners = _owners;
        required = _required;
    }
    
    function submitTransaction(address to, uint256 value, bytes memory data) 
        public 
        returns (uint256) 
    {
        uint256 txId = transactions.length;
        transactions.push(Transaction({
            to: to,
            value: value,
            data: data,
            executed: false,
            confirmations: 0
        }));
        return txId;
    }
    
    function confirmTransaction(uint256 txId) public {
        require(isOwner(msg.sender), "Not owner");
        require(!confirmations[txId][msg.sender], "Already confirmed");
        
        confirmations[txId][msg.sender] = true;
        transactions[txId].confirmations++;
        
        if (transactions[txId].confirmations >= required) {
            executeTransaction(txId);
        }
    }
    
    function executeTransaction(uint256 txId) internal {
        Transaction storage txn = transactions[txId];
        require(!txn.executed, "Already executed");
        
        txn.executed = true;
        (bool success, ) = txn.to.call{value: txn.value}(txn.data);
        require(success, "Transaction failed");
    }
    
    function isOwner(address account) public view returns (bool) {
        for (uint256 i = 0; i < owners.length; i++) {
            if (owners[i] == account) return true;
        }
        return false;
    }
}
```

### Timelock Pattern

**Implementation:**
```solidity
contract Timelock {
    uint256 public constant DELAY = 2 days;
    
    struct QueuedTransaction {
        address target;
        uint256 value;
        bytes data;
        uint256 eta;  // Estimated time of arrival
    }
    
    mapping(bytes32 => QueuedTransaction) public queuedTransactions;
    
    function queueTransaction(
        address target,
        uint256 value,
        bytes memory data
    ) public returns (bytes32) {
        uint256 eta = block.timestamp + DELAY;
        bytes32 txHash = keccak256(abi.encode(target, value, data, eta));
        
        queuedTransactions[txHash] = QueuedTransaction({
            target: target,
            value: value,
            data: data,
            eta: eta
        });
        
        return txHash;
    }
    
    function executeTransaction(bytes32 txHash) public payable {
        QueuedTransaction memory txn = queuedTransactions[txHash];
        require(txn.eta != 0, "Transaction not queued");
        require(block.timestamp >= txn.eta, "Timelock not expired");
        require(block.timestamp <= txn.eta + 7 days, "Transaction stale");
        
        delete queuedTransactions[txHash];
        
        (bool success, ) = txn.target.call{value: txn.value}(txn.data);
        require(success, "Transaction execution failed");
    }
}
```

## Gas Optimization Patterns

### Storage Packing

**Inefficient:**
```solidity
contract Inefficient {
    uint256 a;  // Slot 0
    uint128 b;  // Slot 1
    uint128 c;  // Slot 2
    uint256 d;  // Slot 3
}
```

**Optimized:**
```solidity
contract Optimized {
    uint256 a;  // Slot 0
    uint256 d;  // Slot 1
    uint128 b;  // Slot 2
    uint128 c;  // Slot 2 (packed with b)
}
```

### Calldata vs Memory

**Inefficient:**
```solidity
function processArray(uint256[] memory arr) external {
    // Memory copy costs gas
}
```

**Optimized:**
```solidity
function processArray(uint256[] calldata arr) external {
    // No copy, direct read from calldata
}
```

### Short-Circuit Evaluation

**Inefficient:**
```solidity
require(expensiveCheck() && cheapCheck(), "Failed");
```

**Optimized:**
```solidity
require(cheapCheck() && expensiveCheck(), "Failed");
```

### Unchecked Arithmetic

**When Safe:**
```solidity
function increment() public {
    unchecked {
        counter++;  // Save gas if overflow impossible
    }
}
```

### Custom Errors

**Inefficient:**
```solidity
require(balance >= amount, "Insufficient balance");
```

**Optimized:**
```solidity
error InsufficientBalance(uint256 available, uint256 required);

if (balance < amount) {
    revert InsufficientBalance(balance, amount);
}
```

## Security Patterns

### Reentrancy Guard

**Implementation:**
```solidity
contract ReentrancyGuard {
    uint256 private constant NOT_ENTERED = 1;
    uint256 private constant ENTERED = 2;
    uint256 private status;
    
    constructor() {
        status = NOT_ENTERED;
    }
    
    modifier nonReentrant() {
        require(status != ENTERED, "Reentrant call");
        status = ENTERED;
        _;
        status = NOT_ENTERED;
    }
    
    function withdraw(uint256 amount) public nonReentrant {
        // Safe from reentrancy
    }
}
```

### Pull Over Push Pattern

**Vulnerable (Push):**
```solidity
function distribute() public {
    for (uint256 i = 0; i < recipients.length; i++) {
        recipients[i].transfer(amounts[i]);  // Can fail, blocking all
    }
}
```

**Secure (Pull):**
```solidity
mapping(address => uint256) public pendingWithdrawals;

function setPendingWithdrawal(address recipient, uint256 amount) internal {
    pendingWithdrawals[recipient] += amount;
}

function withdraw() public {
    uint256 amount = pendingWithdrawals[msg.sender];
    pendingWithdrawals[msg.sender] = 0;
    payable(msg.sender).transfer(amount);
}
```

### Rate Limiting

**Implementation:**
```solidity
contract RateLimited {
    mapping(address => uint256) public lastAction;
    uint256 public constant COOLDOWN = 1 hours;
    
    modifier rateLimit() {
        require(
            block.timestamp >= lastAction[msg.sender] + COOLDOWN,
            "Rate limit exceeded"
        );
        lastAction[msg.sender] = block.timestamp;
        _;
    }
    
    function sensitiveAction() public rateLimit {
        // Protected action
    }
}
```

### Emergency Stop (Circuit Breaker)

**Implementation:**
```solidity
contract EmergencyStop {
    bool public stopped = false;
    address public owner;
    
    constructor() {
        owner = msg.sender;
    }
    
    modifier stopInEmergency() {
        require(!stopped, "Contract is stopped");
        _;
    }
    
    modifier onlyInEmergency() {
        require(stopped, "Not in emergency");
        _;
    }
    
    function toggleEmergency() public {
        require(msg.sender == owner, "Not owner");
        stopped = !stopped;
    }
    
    function normalOperation() public stopInEmergency {
        // Normal functionality
    }
    
    function emergencyWithdraw() public onlyInEmergency {
        // Emergency recovery
    }
}
```

## Advanced DeFi Patterns

### Flash Loan Pattern

**Implementation:**
```solidity
interface IFlashLoanReceiver {
    function executeOperation(
        address asset,
        uint256 amount,
        uint256 premium,
        address initiator,
        bytes calldata params
    ) external returns (bool);
}

contract FlashLoanProvider {
    function flashLoan(
        address receiver,
        address asset,
        uint256 amount,
        bytes calldata params
    ) external {
        uint256 balanceBefore = IERC20(asset).balanceOf(address(this));
        uint256 premium = amount * 9 / 10000;  // 0.09% fee
        
        // Transfer tokens to receiver
        IERC20(asset).transfer(receiver, amount);
        
        // Execute receiver's logic
        require(
            IFlashLoanReceiver(receiver).executeOperation(
                asset,
                amount,
                premium,
                msg.sender,
                params
            ),
            "Flash loan execution failed"
        );
        
        // Ensure repayment
        uint256 balanceAfter = IERC20(asset).balanceOf(address(this));
        require(
            balanceAfter >= balanceBefore + premium,
            "Flash loan not repaid"
        );
    }
}
```

### Staking with Rewards

**Implementation:**
```solidity
contract StakingRewards {
    IERC20 public stakingToken;
    IERC20 public rewardsToken;
    
    uint256 public rewardRate = 100;  // Tokens per second
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;
    
    mapping(address => uint256) public userRewardPerTokenPaid;
    mapping(address => uint256) public rewards;
    mapping(address => uint256) public balances;
    
    uint256 private totalSupply;
    
    function rewardPerToken() public view returns (uint256) {
        if (totalSupply == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + (
            (block.timestamp - lastUpdateTime) * rewardRate * 1e18 / totalSupply
        );
    }
    
    function earned(address account) public view returns (uint256) {
        return (balances[account] * 
            (rewardPerToken() - userRewardPerTokenPaid[account]) / 1e18) + 
            rewards[account];
    }
    
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            rewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }
    
    function stake(uint256 amount) external updateReward(msg.sender) {
        totalSupply += amount;
        balances[msg.sender] += amount;
        stakingToken.transferFrom(msg.sender, address(this), amount);
    }
    
    function withdraw(uint256 amount) external updateReward(msg.sender) {
        totalSupply -= amount;
        balances[msg.sender] -= amount;
        stakingToken.transfer(msg.sender, amount);
    }
    
    function getReward() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        rewards[msg.sender] = 0;
        rewardsToken.transfer(msg.sender, reward);
    }
}
```

### Automated Market Maker (AMM)

**Constant Product Formula (x * y = k):**
```solidity
contract SimpleAMM {
    IERC20 public tokenA;
    IERC20 public tokenB;
    
    uint256 public reserveA;
    uint256 public reserveB;
    
    function addLiquidity(uint256 amountA, uint256 amountB) external {
        tokenA.transferFrom(msg.sender, address(this), amountA);
        tokenB.transferFrom(msg.sender, address(this), amountB);
        
        reserveA += amountA;
        reserveB += amountB;
    }
    
    function swap(address tokenIn, uint256 amountIn) external returns (uint256) {
        require(
            tokenIn == address(tokenA) || tokenIn == address(tokenB),
            "Invalid token"
        );
        
        bool isTokenA = tokenIn == address(tokenA);
        (IERC20 tokenInContract, IERC20 tokenOutContract, uint256 reserveIn, uint256 reserveOut) = 
            isTokenA 
                ? (tokenA, tokenB, reserveA, reserveB)
                : (tokenB, tokenA, reserveB, reserveA);
        
        tokenInContract.transferFrom(msg.sender, address(this), amountIn);
        
        // Calculate output amount: amountOut = reserveOut * amountIn / (reserveIn + amountIn)
        uint256 amountInWithFee = amountIn * 997 / 1000;  // 0.3% fee
        uint256 amountOut = (reserveOut * amountInWithFee) / (reserveIn + amountInWithFee);
        
        tokenOutContract.transfer(msg.sender, amountOut);
        
        // Update reserves
        if (isTokenA) {
            reserveA += amountIn;
            reserveB -= amountOut;
        } else {
            reserveB += amountIn;
            reserveA -= amountOut;
        }
        
        return amountOut;
    }
}
```

## Testing Patterns

### Mocking External Contracts

**Mock Implementation:**
```solidity
contract MockERC20 is IERC20 {
    mapping(address => uint256) private balances;
    
    function mint(address to, uint256 amount) external {
        balances[to] += amount;
    }
    
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }
    
    function transfer(address to, uint256 amount) external returns (bool) {
        balances[msg.sender] -= amount;
        balances[to] += amount;
        return true;
    }
}
```

### Time Manipulation in Tests

**Hardhat:**
```javascript
await ethers.provider.send("evm_increaseTime", [86400]);  // 1 day
await ethers.provider.send("evm_mine");
```

**Foundry:**
```solidity
vm.warp(block.timestamp + 1 days);
```

## Conclusion

Advanced Solidity patterns enable developers to build secure, efficient, and maintainable smart contracts. Understanding these patterns is crucial for production-grade development, especially in DeFi where security and gas optimization are paramount. Always test thoroughly, conduct audits, and stay updated with evolving best practices.
