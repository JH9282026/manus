---
name: smart-contracts-development
description: "Master smart contract development with Solidity and other blockchain programming languages. Covers smart contract architecture, Solidity syntax and features, development frameworks (Hardhat, Foundry, Truffle), testing strategies, security best practices, gas optimization, design patterns, ERC standards (ERC-20, ERC-721, ERC-1155), deployment strategies, and auditing. Use for: developing Ethereum smart contracts, creating DeFi protocols, building NFT platforms, implementing DAOs, writing secure blockchain code, optimizing gas costs, testing smart contracts, and deploying decentralized applications."
---

# Smart Contracts Development

## Overview

Smart contracts are self-executing programs that run on blockchain networks, automatically enforcing agreements and executing transactions when predefined conditions are met. They are the foundation of decentralized applications (dApps), enabling trustless interactions without intermediaries. This skill covers comprehensive smart contract development, focusing primarily on Solidity for Ethereum and EVM-compatible chains.

## What Are Smart Contracts?

### Definition and Characteristics

A smart contract is a collection of code (functions) and data (state) residing at a specific address on a blockchain. Once deployed, smart contracts:

- **Execute automatically** when conditions are met
- **Are immutable** (cannot be changed after deployment)
- **Are transparent** (code and execution visible on blockchain)
- **Are deterministic** (same inputs always produce same outputs)
- **Operate trustlessly** (no intermediary required)

### Use Cases

- **Decentralized Finance (DeFi)**: Lending, borrowing, trading, yield farming
- **Non-Fungible Tokens (NFTs)**: Digital art, collectibles, gaming assets
- **Decentralized Autonomous Organizations (DAOs)**: Governance, voting, treasury management
- **Supply Chain**: Tracking, verification, automated payments
- **Insurance**: Automated claims processing
- **Real Estate**: Property transfers, rental agreements
- **Gaming**: In-game economies, provably fair mechanics

## Solidity Programming Language

### Language Basics

**Solidity** is a statically-typed, contract-oriented programming language designed for writing smart contracts on Ethereum and EVM-compatible blockchains.

**Key Features:**
- Object-oriented with inheritance
- JavaScript-like syntax
- Statically typed
- Supports libraries and complex user-defined types

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

### Data Types

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

**Example:**
```solidity
contract DataTypes {
    // Value types
    bool public isActive = true;
    uint256 public count = 0;
    address public owner;
    
    // Reference types
    uint256[] public numbers;
    mapping(address => uint256) public balances;
    
    struct User {
        string name;
        uint256 age;
    }
    
    User[] public users;
}
```

### Functions

**Visibility Specifiers:**
- `public`: Accessible by anyone, internally and externally
- `private`: Only accessible within the contract
- `internal`: Accessible within contract and derived contracts
- `external`: Only callable from outside the contract

**State Mutability:**
- `view`: Reads state but doesn't modify it
- `pure`: Neither reads nor modifies state
- `payable`: Can receive Ether

**Example:**
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
}
```

### Modifiers

Modifiers alter function behavior, commonly used for access control and validation.

```solidity
contract AccessControl {
    address public owner;
    
    constructor() {
        owner = msg.sender;
    }
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the owner");
        _;
    }
    
    function restrictedFunction() public onlyOwner {
        // Only owner can call this
    }
}
```

### Events

Events enable logging for off-chain listeners and provide transaction receipts.

```solidity
contract EventExample {
    event Transfer(address indexed from, address indexed to, uint256 amount);
    
    function transfer(address to, uint256 amount) public {
        // Transfer logic
        emit Transfer(msg.sender, to, amount);
    }
}
```

### Error Handling

**Methods:**
- `require()`: Validate conditions, refund remaining gas
- `assert()`: Check invariants, consume all gas (use sparingly)
- `revert()`: Abort execution with custom error

```solidity
contract ErrorHandling {
    mapping(address => uint256) public balances;
    
    function withdraw(uint256 amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        
        balances[msg.sender] -= amount;
        
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
    }
}
```

## Development Frameworks

### Hardhat

**Features:**
- Local Ethereum network for testing
- Console.log debugging in Solidity
- Extensive plugin ecosystem
- TypeScript support
- Mainnet forking

**Setup:**
```bash
npm install --save-dev hardhat
npx hardhat init
```

**Configuration (hardhat.config.js):**
```javascript
module.exports = {
  solidity: "0.8.20",
  networks: {
    hardhat: {},
    sepolia: {
      url: process.env.SEPOLIA_URL,
      accounts: [process.env.PRIVATE_KEY]
    }
  }
};
```

### Foundry

**Features:**
- Rust-based, extremely fast
- Native Solidity testing
- Built-in fuzzing
- Gas optimization tools
- Forge (build/test), Cast (interact), Anvil (local node)

**Setup:**
```bash
curl -L https://foundry.paradigm.xyz | bash
foundryup
forge init my-project
```

**Testing Example:**
```solidity
// test/Counter.t.sol
import "forge-std/Test.sol";
import "../src/Counter.sol";

contract CounterTest is Test {
    Counter public counter;
    
    function setUp() public {
        counter = new Counter();
    }
    
    function testIncrement() public {
        counter.increment();
        assertEq(counter.count(), 1);
    }
}
```

### Truffle

**Features:**
- Pioneering development framework
- Built-in smart contract compilation
- Automated testing
- Deployment management
- Network management

**Setup:**
```bash
npm install -g truffle
truffle init
```

## Testing Strategies

### Unit Testing

Test individual functions in isolation.

**Hardhat Example:**
```javascript
const { expect } = require("chai");

describe("Token", function () {
  it("Should transfer tokens between accounts", async function () {
    const [owner, addr1] = await ethers.getSigners();
    const Token = await ethers.getContractFactory("Token");
    const token = await Token.deploy();
    
    await token.transfer(addr1.address, 50);
    expect(await token.balanceOf(addr1.address)).to.equal(50);
  });
});
```

### Integration Testing

Test interactions between multiple contracts.

```javascript
describe("DeFi Protocol", function () {
  it("Should allow staking and reward distribution", async function () {
    const token = await deployToken();
    const staking = await deployStaking(token.address);
    
    await token.approve(staking.address, 1000);
    await staking.stake(1000);
    
    // Fast forward time
    await ethers.provider.send("evm_increaseTime", [86400]);
    await ethers.provider.send("evm_mine");
    
    const rewards = await staking.calculateRewards(owner.address);
    expect(rewards).to.be.gt(0);
  });
});
```

### Fuzzing

Test with random inputs to find edge cases.

**Foundry Fuzzing:**
```solidity
function testFuzzTransfer(uint256 amount) public {
    vm.assume(amount <= token.totalSupply());
    token.transfer(address(1), amount);
    assertEq(token.balanceOf(address(1)), amount);
}
```

### Test Coverage

**Hardhat Coverage:**
```bash
npm install --save-dev solidity-coverage
npx hardhat coverage
```

**Target:** Aim for >90% code coverage

## Security Best Practices

### Common Vulnerabilities

**1. Reentrancy**

**Vulnerable:**
```solidity
function withdraw() public {
    uint256 amount = balances[msg.sender];
    (bool success, ) = msg.sender.call{value: amount}("");
    balances[msg.sender] = 0;
}
```

**Secure (Checks-Effects-Interactions):**
```solidity
function withdraw() public {
    uint256 amount = balances[msg.sender];
    balances[msg.sender] = 0;  // Update state first
    (bool success, ) = msg.sender.call{value: amount}("");
    require(success, "Transfer failed");
}
```

**2. Integer Overflow/Underflow**

**Solution:** Use Solidity 0.8.0+ (automatic checks) or SafeMath library

**3. Access Control**

**Use OpenZeppelin's Ownable:**
```solidity
import "@openzeppelin/contracts/access/Ownable.sol";

contract MyContract is Ownable {
    function sensitiveFunction() public onlyOwner {
        // Only owner can call
    }
}
```

**4. Front-Running**

**Mitigation:**
- Commit-reveal schemes
- Batch auctions
- Submarine sends
- Flashbots (MEV protection)

**5. Timestamp Dependence**

**Avoid:**
```solidity
if (block.timestamp % 2 == 0) {  // Miners can manipulate
    // Do something
}
```

**Better:**
```solidity
if (block.number > targetBlock) {  // More reliable
    // Do something
}
```

### Security Tools

**Static Analysis:**
- **Slither**: Python-based analyzer
- **Mythril**: Security analysis tool
- **Solhint**: Linting tool

**Auditing Services:**
- OpenZeppelin
- Trail of Bits
- ConsenSys Diligence
- Certik

## Gas Optimization

### Understanding Gas

**Gas Costs:**
- Storage write: 20,000 gas
- Storage read: 200 gas
- Memory operation: 3 gas
- Addition: 3 gas
- Multiplication: 5 gas

### Optimization Techniques


---

**Note:** This file was automatically condensed to meet the 500-line requirement. Additional content has been moved to the references/ folder.

## Using the Reference Files

- [./references/advanced-solidity-patterns.md](./references/advanced-solidity-patterns.md): Advanced Solidity Patterns
- [./references/solidity-fundamentals.md](./references/solidity-fundamentals.md): Solidity Fundamentals
