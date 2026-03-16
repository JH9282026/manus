# Solidity Fundamentals

## Complete Language Reference

### Contract Structure

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    // State variable
    uint256 private storedData;
    
    // Event
    event DataStored(uint256 newValue);
    
    // Constructor
    constructor(uint256 initialValue) {
        storedData = initialValue;
    }
    
    // Function to set value
    function set(uint256 x) public {
        storedData = x;
        emit DataStored(x);
    }
    
    // Function to get value
    function get() public view returns (uint256) {
        return storedData;
    }
}
```

### Data Types in Detail

**Value Types:**
- `bool`: Boolean (true/false)
- `uint`: Unsigned integer (uint8 to uint256)
- `int`: Signed integer (int8 to int256)
- `address`: Ethereum address (20 bytes)
- `bytes`: Fixed-size byte arrays (bytes1 to bytes32)
- `string`: Dynamic UTF-8 string

**Reference Types:**
- `arrays`: Fixed or dynamic size
- `struct`: Custom data structures
- `mapping`: Key-value pairs (hash tables)

**Complete Example:**
```solidity
contract DataTypes {
    // Value types
    bool public isActive = true;
    uint256 public count = 0;
    address public owner;
    bytes32 public data;
    string public name;
    
    // Reference types
    uint256[] public numbers;
    mapping(address => uint256) public balances;
    
    struct User {
        string name;
        uint256 age;
        bool active;
    }
    
    User[] public users;
    mapping(address => User) public userMap;
}
```

### Functions Complete Reference

**Visibility Specifiers:**
- `public`: Accessible by anyone, internally and externally
- `private`: Only accessible within the contract
- `internal`: Accessible within contract and derived contracts
- `external`: Only callable from outside the contract

**State Mutability:**
- `view`: Reads state but doesn't modify it
- `pure`: Neither reads nor modifies state
- `payable`: Can receive Ether

**Complete Example:**
```solidity
contract FunctionExamples {
    uint256 private value;
    
    // Public function that modifies state
    function setValue(uint256 _value) public {
        value = _value;
    }
    
    // View function (reads state)
    function getValue() public view returns (uint256) {
        return value;
    }
    
    // Pure function (no state access)
    function add(uint256 a, uint256 b) public pure returns (uint256) {
        return a + b;
    }
    
    // Payable function (receives Ether)
    function deposit() public payable {
        // Function body
    }
    
    // External function (gas efficient for external calls)
    function externalFunction(uint256[] calldata data) external pure returns (uint256) {
        return data.length;
    }
}
```

### Modifiers

```solidity
contract AccessControl {
    address public owner;
    bool public paused;
    
    constructor() {
        owner = msg.sender;
    }
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the owner");
        _;
    }
    
    modifier whenNotPaused() {
        require(!paused, "Contract is paused");
        _;
    }
    
    function restrictedFunction() public onlyOwner whenNotPaused {
        // Only owner can call when not paused
    }
    
    function pause() public onlyOwner {
        paused = true;
    }
}
```

### Events and Logging

```solidity
contract EventExample {
    event Transfer(address indexed from, address indexed to, uint256 amount);
    event Approval(address indexed owner, address indexed spender, uint256 amount);
    
    function transfer(address to, uint256 amount) public {
        // Transfer logic
        emit Transfer(msg.sender, to, amount);
    }
    
    function approve(address spender, uint256 amount) public {
        // Approval logic
        emit Approval(msg.sender, spender, amount);
    }
}
```

### Error Handling

```solidity
contract ErrorHandling {
    mapping(address => uint256) public balances;
    
    // Custom errors (gas efficient)
    error InsufficientBalance(uint256 available, uint256 required);
    error TransferFailed();
    
    function withdraw(uint256 amount) public {
        if (balances[msg.sender] < amount) {
            revert InsufficientBalance(balances[msg.sender], amount);
        }
        
        balances[msg.sender] -= amount;
        
        (bool success, ) = msg.sender.call{value: amount}("");
        if (!success) revert TransferFailed();
    }
    
    function deposit() public payable {
        require(msg.value > 0, "Must send ETH");
        balances[msg.sender] += msg.value;
    }
}
```

See SKILL.md for framework integration and advanced topics.
