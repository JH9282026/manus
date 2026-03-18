# Smart Contract Security

Comprehensive guide to identifying, preventing, and remediating smart contract vulnerabilities across Solidity and EVM-based platforms.

---

## Critical Vulnerability Deep Dive

### Reentrancy Attacks

**Attack Mechanism**:

Reentrancy occurs when a contract makes an external call to another contract before updating its own state. The external contract can then recursively call back into the original function, exploiting the outdated state.

**Classic Example: The DAO Hack (2016)**

```solidity
// VULNERABLE CODE
contract VulnerableBank {
    mapping(address => uint256) public balances;
    
    function withdraw(uint256 amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        
        // VULNERABILITY: External call before state update
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
        
        // State update happens AFTER external call
        balances[msg.sender] -= amount;
    }
}

// ATTACKER CONTRACT
contract Attacker {
    VulnerableBank public bank;
    
    constructor(address _bankAddress) {
        bank = VulnerableBank(_bankAddress);
    }
    
    // Fallback function called when receiving ether
    receive() external payable {
        if (address(bank).balance >= 1 ether) {
            bank.withdraw(1 ether); // Recursive call
        }
    }
    
    function attack() external payable {
        require(msg.value >= 1 ether);
        bank.balances[address(this)] = 1 ether;
        bank.withdraw(1 ether); // Initial call
    }
}
```

**Secure Implementation**:

```solidity
// SECURE CODE: Checks-Effects-Interactions Pattern
contract SecureBank {
    mapping(address => uint256) public balances;
    
    function withdraw(uint256 amount) public {
        // CHECKS: Validate conditions
        require(balances[msg.sender] >= amount, "Insufficient balance");
        
        // EFFECTS: Update state BEFORE external call
        balances[msg.sender] -= amount;
        
        // INTERACTIONS: External call happens last
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
    }
}

// ALTERNATIVE: Using ReentrancyGuard
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract SecureBankWithGuard is ReentrancyGuard {
    mapping(address => uint256) public balances;
    
    function withdraw(uint256 amount) public nonReentrant {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount;
        
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
    }
}
```

**Impact**: The DAO attack resulted in $60+ million in losses and led to the controversial Ethereum hard fork creating Ethereum Classic.

**Detection**:
- Look for external calls (`.call()`, `.transfer()`, `.send()`) before state updates
- Check for state-changing functions without reentrancy guards
- Use static analysis tools: Slither, Mythril, Securify

---

### Integer Overflow and Underflow

**Attack Mechanism**:

Fixed-size integer types can wrap around when arithmetic operations exceed their maximum or minimum values.

**Vulnerable Example**:

```solidity
// VULNERABLE (Solidity < 0.8.0)
contract VulnerableToken {
    mapping(address => uint256) public balances;
    
    function transfer(address to, uint256 amount) public {
        // VULNERABILITY: No overflow check
        require(balances[msg.sender] >= amount);
        balances[msg.sender] -= amount; // Potential underflow
        balances[to] += amount; // Potential overflow
    }
}

// ATTACK SCENARIO
// If balances[attacker] = 0 and amount = 1
// balances[attacker] -= 1 results in:
// 0 - 1 = 2^256 - 1 (maximum uint256 value)
```

**Secure Implementations**:

```solidity
// OPTION 1: Use Solidity 0.8.0+ (automatic checks)
pragma solidity ^0.8.0;

contract SecureToken {
    mapping(address => uint256) public balances;
    
    function transfer(address to, uint256 amount) public {
        require(balances[msg.sender] >= amount);
        balances[msg.sender] -= amount; // Automatic overflow check
        balances[to] += amount; // Automatic overflow check
    }
}

// OPTION 2: Use SafeMath library (Solidity < 0.8.0)
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract SecureTokenLegacy {
    using SafeMath for uint256;
    mapping(address => uint256) public balances;
    
    function transfer(address to, uint256 amount) public {
        require(balances[msg.sender] >= amount);
        balances[msg.sender] = balances[msg.sender].sub(amount);
        balances[to] = balances[to].add(amount);
    }
}
```

**Best Practices**:
- Always use Solidity 0.8.0 or higher for new contracts
- For legacy contracts, use OpenZeppelin's SafeMath library
- Test edge cases: maximum values, zero values, boundary conditions
- Use unchecked blocks only when overflow is intentional and safe

---

### Access Control Vulnerabilities

**Common Flaws**:

1. **Missing Access Controls**
2. **Unprotected Initialization Functions**
3. **Incorrect Modifier Implementation**
4. **Default Visibility Issues**

**Vulnerable Examples**:

```solidity
// VULNERABILITY 1: Missing Access Control
contract VulnerableContract {
    address public owner;
    
    function setOwner(address newOwner) public {
        // VULNERABILITY: Anyone can call this
        owner = newOwner;
    }
}

// VULNERABILITY 2: Unprotected Initialization
contract VulnerableProxy {
    address public implementation;
    
    function initialize(address _implementation) public {
        // VULNERABILITY: Can be called multiple times
        implementation = _implementation;
    }
}

// VULNERABILITY 3: Incorrect Modifier
contract VulnerableModifier {
    address public owner;
    
    modifier onlyOwner() {
        require(msg.sender == owner);
        // VULNERABILITY: Missing underscore (_)
    }
    
    function sensitiveFunction() public onlyOwner {
        // This function has no protection!
    }
}
```

**Secure Implementations**:

```solidity
// SECURE: Using OpenZeppelin Ownable
import "@openzeppelin/contracts/access/Ownable.sol";

contract SecureContract is Ownable {
    function sensitiveFunction() public onlyOwner {
        // Only owner can call this
    }
}

// SECURE: Role-Based Access Control (RBAC)
import "@openzeppelin/contracts/access/AccessControl.sol";

contract SecureRBAC is AccessControl {
    bytes32 public constant ADMIN_ROLE = keccak256("ADMIN_ROLE");
    bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");
    
    constructor() {
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(ADMIN_ROLE, msg.sender);
    }
    
    function mint(address to, uint256 amount) public onlyRole(MINTER_ROLE) {
        // Only minters can call this
    }
    
    function addMinter(address account) public onlyRole(ADMIN_ROLE) {
        grantRole(MINTER_ROLE, account);
    }
}

// SECURE: One-Time Initialization
contract SecureProxy {
    address public implementation;
    bool private initialized;
    
    function initialize(address _implementation) public {
        require(!initialized, "Already initialized");
        implementation = _implementation;
        initialized = true;
    }
}

// ALTERNATIVE: Using OpenZeppelin Initializable
import "@openzeppelin/contracts-upgradeable/proxy/utils/Initializable.sol";

contract SecureProxyUpgradeable is Initializable {
    address public implementation;
    
    function initialize(address _implementation) public initializer {
        implementation = _implementation;
    }
}
```

**Real-World Impact**: KiloEx DEX lost $7 million due to missing access controls on critical functions.

---

### Oracle Manipulation and Flash Loan Attacks

**Attack Mechanism**:

Attackers exploit weak price oracles by manipulating reference prices, often using flash loans to amplify the attack.

**Vulnerable Oracle Implementation**:

```solidity
// VULNERABLE: Using single DEX as price source
contract VulnerableLending {
    IUniswapV2Pair public priceFeed;
    
    function getPrice() public view returns (uint256) {
        (uint112 reserve0, uint112 reserve1, ) = priceFeed.getReserves();
        // VULNERABILITY: Spot price can be manipulated in single transaction
        return (reserve1 * 1e18) / reserve0;
    }
    
    function borrow(uint256 amount) public {
        uint256 collateralValue = getUserCollateral(msg.sender) * getPrice();
        require(collateralValue >= amount * 150 / 100, "Insufficient collateral");
        // Attacker can manipulate getPrice() via flash loan
    }
}
```

**Attack Scenario**:

```
1. Attacker takes flash loan of 10,000 ETH
2. Swaps large amount on DEX to manipulate price oracle
3. Uses manipulated price to borrow under-collateralized
4. Repays flash loan
5. Keeps profit from under-collateralized loan
```

**Secure Oracle Implementations**:

```solidity
// SECURE: Using Chainlink Price Feeds
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract SecureLending {
    AggregatorV3Interface internal priceFeed;
    
    constructor(address _priceFeed) {
        priceFeed = AggregatorV3Interface(_priceFeed);
    }
    
    function getPrice() public view returns (uint256) {
        (
            uint80 roundID,
            int256 price,
            uint256 startedAt,
            uint256 updatedAt,
            uint80 answeredInRound
        ) = priceFeed.latestRoundData();
        
        // Validate oracle data
        require(price > 0, "Invalid price");
        require(updatedAt > 0, "Round not complete");
        require(answeredInRound >= roundID, "Stale price");
        
        return uint256(price);
    }
}

// SECURE: Time-Weighted Average Price (TWAP)
import "@uniswap/v2-periphery/contracts/libraries/UniswapV2OracleLibrary.sol";

contract SecureTWAP {
    IUniswapV2Pair public pair;
    uint256 public price0CumulativeLast;
    uint256 public price1CumulativeLast;
    uint32 public blockTimestampLast;
    uint256 public constant PERIOD = 1 hours;
    
    function update() external {
        (uint256 price0Cumulative, uint256 price1Cumulative, uint32 blockTimestamp) =
            UniswapV2OracleLibrary.currentCumulativePrices(address(pair));
        
        uint32 timeElapsed = blockTimestamp - blockTimestampLast;
        require(timeElapsed >= PERIOD, "Period not elapsed");
        
        // Calculate TWAP (resistant to flash loan manipulation)
        uint256 price0Average = (price0Cumulative - price0CumulativeLast) / timeElapsed;
        uint256 price1Average = (price1Cumulative - price1CumulativeLast) / timeElapsed;
        
        price0CumulativeLast = price0Cumulative;
        price1CumulativeLast = price1Cumulative;
        blockTimestampLast = blockTimestamp;
    }
}

// SECURE: Multiple Oracle Sources
contract MultiOracleLending {
    AggregatorV3Interface public chainlinkFeed;
    IUniswapV2Pair public uniswapPair;
    uint256 public constant MAX_DEVIATION = 5; // 5% max deviation
    
    function getPrice() public view returns (uint256) {
        uint256 chainlinkPrice = getChainlinkPrice();
        uint256 uniswapPrice = getUniswapTWAP();
        
        // Ensure prices are within acceptable deviation
        uint256 deviation = abs(chainlinkPrice - uniswapPrice) * 100 / chainlinkPrice;
        require(deviation <= MAX_DEVIATION, "Price deviation too high");
        
        // Return average of both sources
        return (chainlinkPrice + uniswapPrice) / 2;
    }
}
```

**Flash Loan Defense Strategies**:

1. **Use Time-Weighted Prices**: TWAP cannot be manipulated in single transaction
2. **Multiple Oracle Sources**: Cross-validate prices from independent sources
3. **Slippage Limits**: Reject transactions with excessive price impact
4. **Transaction Delays**: Implement time locks for large operations
5. **Monitoring**: Real-time alerts for unusual price movements

**Real-World Impacts**:
- Abracadabra: $13 million flash loan exploit
- Cream Finance: $130 million flash loan attack
- Harvest Finance: $24 million flash loan manipulation

---

## Additional Vulnerability Classes

### Front-Running Attacks

**Mechanism**: Attackers monitor mempool for pending transactions and submit their own with higher gas fees to execute first.

**Mitigation**:
```solidity
contract FrontRunProtection {
    // Commit-Reveal Scheme
    mapping(address => bytes32) public commitments;
    
    function commit(bytes32 hash) public {
        commitments[msg.sender] = hash;
    }
    
    function reveal(uint256 value, bytes32 salt) public {
        require(keccak256(abi.encodePacked(value, salt)) == commitments[msg.sender]);
        // Execute transaction with revealed value
    }
    
    // Slippage Protection
    function swap(uint256 amountIn, uint256 minAmountOut) public {
        uint256 amountOut = calculateSwap(amountIn);
        require(amountOut >= minAmountOut, "Slippage too high");
    }
}
```

### Timestamp Dependence

**Vulnerability**: Miners can manipulate `block.timestamp` by ~15 seconds.

```solidity
// VULNERABLE
contract VulnerableLottery {
    function pickWinner() public {
        // VULNERABILITY: Miner can manipulate timestamp
        uint256 random = uint256(keccak256(abi.encodePacked(block.timestamp))) % players.length;
    }
}

// SECURE: Use Chainlink VRF
import "@chainlink/contracts/src/v0.8/VRFConsumerBase.sol";

contract SecureLottery is VRFConsumerBase {
    bytes32 internal keyHash;
    uint256 internal fee;
    
    function requestRandomness() public returns (bytes32 requestId) {
        return requestRandomness(keyHash, fee);
    }
    
    function fulfillRandomness(bytes32 requestId, uint256 randomness) internal override {
        uint256 winnerIndex = randomness % players.length;
        // Use cryptographically secure randomness
    }
}
```

### Denial of Service (DoS)

**Gas Limit DoS**:
```solidity
// VULNERABLE: Unbounded loop
contract VulnerableAirdrop {
    address[] public recipients;
    
    function distribute() public {
        // VULNERABILITY: May exceed gas limit as array grows
        for (uint256 i = 0; i < recipients.length; i++) {
            payable(recipients[i]).transfer(1 ether);
        }
    }
}

// SECURE: Batch processing with limits
contract SecureAirdrop {
    address[] public recipients;
    uint256 public lastProcessedIndex;
    uint256 public constant BATCH_SIZE = 100;
    
    function distributeBatch() public {
        uint256 endIndex = min(lastProcessedIndex + BATCH_SIZE, recipients.length);
        
        for (uint256 i = lastProcessedIndex; i < endIndex; i++) {
            payable(recipients[i]).transfer(1 ether);
        }
        
        lastProcessedIndex = endIndex;
    }
}
```

---

## Security Testing Methodology

### Automated Testing Tools

**Static Analysis**:
- **Slither**: Fast, comprehensive vulnerability detection
- **Mythril**: Symbolic execution for deep analysis
- **Securify**: Automated security verification
- **Manticore**: Symbolic execution with concrete test generation

**Fuzzing**:
- **Echidna**: Property-based fuzzing for Solidity
- **Harvey**: Greybox fuzzing for smart contracts
- **Foundry**: Fast fuzzing integrated with testing framework

**Formal Verification**:
- **Certora Prover**: Mathematical proof of correctness
- **K Framework**: Formal semantics and verification
- **Runtime Verification**: Automated theorem proving

### Manual Testing Checklist

**Access Control**:
- [ ] All privileged functions have appropriate modifiers
- [ ] Initialization functions can only be called once
- [ ] Default visibility is explicitly specified
- [ ] Role-based access is properly implemented

**Arithmetic**:
- [ ] Using Solidity 0.8.0+ or SafeMath
- [ ] Edge cases tested (max values, zero, boundaries)
- [ ] Unchecked blocks are justified and safe

**External Calls**:
- [ ] Checks-Effects-Interactions pattern followed
- [ ] Reentrancy guards on state-changing functions
- [ ] Return values of external calls are checked
- [ ] Gas limits considered for external calls

**Randomness**:
- [ ] No reliance on block.timestamp or blockhash for randomness
- [ ] Using Chainlink VRF or similar secure source
- [ ] Commit-reveal schemes for user-generated randomness

**Oracle Security**:
- [ ] Multiple independent oracle sources
- [ ] Price staleness checks
- [ ] Deviation limits between sources
- [ ] TWAP or similar manipulation-resistant pricing

**Gas Optimization**:
- [ ] No unbounded loops
- [ ] Storage operations minimized
- [ ] Batch operations where possible
- [ ] Gas costs tested and documented

---

## Secure Development Patterns

### Pull Over Push Payments

```solidity
// VULNERABLE: Push pattern
contract VulnerablePush {
    function distributeRewards(address[] memory recipients) public {
        for (uint256 i = 0; i < recipients.length; i++) {
            // VULNERABILITY: If one transfer fails, all fail
            payable(recipients[i]).transfer(1 ether);
        }
    }
}

// SECURE: Pull pattern
contract SecurePull {
    mapping(address => uint256) public pendingRewards;
    
    function addRewards(address[] memory recipients) public {
        for (uint256 i = 0; i < recipients.length; i++) {
            pendingRewards[recipients[i]] += 1 ether;
        }
    }
    
    function withdrawReward() public {
        uint256 reward = pendingRewards[msg.sender];
        require(reward > 0, "No pending rewards");
        
        pendingRewards[msg.sender] = 0;
        payable(msg.sender).transfer(reward);
    }
}
```

### Emergency Stop (Circuit Breaker)

```solidity
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract EmergencyStop is Pausable, Ownable {
    function emergencyPause() public onlyOwner {
        _pause();
    }
    
    function resume() public onlyOwner {
        _unpause();
    }
    
    function criticalFunction() public whenNotPaused {
        // Function pauses during emergency
    }
}
```

### Rate Limiting

```solidity
contract RateLimited {
    mapping(address => uint256) public lastActionTime;
    uint256 public constant COOLDOWN = 1 hours;
    
    modifier rateLimit() {
        require(
            block.timestamp >= lastActionTime[msg.sender] + COOLDOWN,
            "Action on cooldown"
        );
        lastActionTime[msg.sender] = block.timestamp;
        _;
    }
    
    function limitedAction() public rateLimit {
        // Can only be called once per hour per address
    }
}
```

---

## Incident Case Studies

### The DAO (2016) - $60M Loss
- **Vulnerability**: Reentrancy
- **Root Cause**: External call before state update
- **Impact**: Led to Ethereum hard fork
- **Lesson**: Always follow Checks-Effects-Interactions pattern

### Parity Wallet (2017) - $150M Frozen
- **Vulnerability**: Unprotected initialization function
- **Root Cause**: Library contract could be initialized by anyone
- **Impact**: Funds permanently frozen
- **Lesson**: Protect all initialization functions

### Poly Network (2021) - $600M Stolen (Returned)
- **Vulnerability**: Access control flaw in cross-chain messaging
- **Root Cause**: Insufficient validation of privileged calls
- **Impact**: Largest DeFi hack (funds returned by hacker)
- **Lesson**: Rigorous access control testing for cross-chain protocols

### Ronin Bridge (2022) - $625M Loss
- **Vulnerability**: Compromised validator keys
- **Root Cause**: Social engineering and insufficient key security
- **Impact**: Largest blockchain hack to date
- **Lesson**: Multi-signature with diverse, secure key management
