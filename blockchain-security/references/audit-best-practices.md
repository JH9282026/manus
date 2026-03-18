# Blockchain Security Audit Best Practices

Comprehensive guide to planning, executing, and remediating blockchain security audits for smart contracts, protocols, and infrastructure.

---

## Pre-Audit Preparation

### Documentation Requirements

**Essential Documentation Checklist**:

```
1. Technical Architecture
   ├─ System architecture diagrams
   ├─ Smart contract interaction flows
   ├─ Data flow diagrams
   ├─ External dependency mapping
   └─ Infrastructure topology

2. Business Logic Documentation
   ├─ Protocol economic model
   ├─ Tokenomics and incentive structures
   ├─ Governance mechanisms
   ├─ User roles and permissions
   └─ Expected behavior specifications

3. Technical Specifications
   ├─ Smart contract specifications
   ├─ API documentation
   ├─ State machine diagrams
   ├─ Invariants and assumptions
   └─ Known limitations

4. Code and Deployment
   ├─ Complete source code repository
   ├─ Commit history and version control
   ├─ Deployment scripts and procedures
   ├─ Configuration files
   └─ Environment setup instructions

5. Previous Security Work
   ├─ Prior audit reports
   ├─ Bug bounty submissions
   ├─ Internal security reviews
   ├─ Remediation evidence
   └─ Outstanding known issues

6. Testing and Quality Assurance
   ├─ Test suite and coverage reports
   ├─ Integration test scenarios
   ├─ Fuzzing results
   ├─ Static analysis reports
   └─ Performance benchmarks
```

**Audit Scope Definition Template**:

```markdown
# Security Audit Scope

## In-Scope Components

### Smart Contracts
- Contract Name: TokenContract.sol
  - Lines of Code: 450
  - Commit Hash: abc123...
  - Deployment Address: 0x...
  - Functionality: ERC-20 token with staking

- Contract Name: StakingPool.sol
  - Lines of Code: 680
  - Commit Hash: abc123...
  - Deployment Address: 0x...
  - Functionality: Liquidity staking and rewards

### Infrastructure (if applicable)
- Validator nodes configuration
- RPC endpoint security
- Key management systems

### External Dependencies
- OpenZeppelin Contracts v4.8.0
- Chainlink Price Feeds
- Uniswap V3 integration

## Out-of-Scope
- Frontend application
- Off-chain backend services
- Third-party contract code (unless integration points)

## Audit Objectives
1. Identify critical vulnerabilities (reentrancy, access control, etc.)
2. Verify economic model soundness
3. Assess gas optimization opportunities
4. Review upgrade mechanisms
5. Validate oracle integration security

## Timeline
- Audit Start: [Date]
- Initial Report: [Date] (2 weeks)
- Remediation Period: [Date] (1 week)
- Final Report: [Date]

## Deliverables
1. Detailed audit report with findings
2. Severity classification for each issue
3. Remediation recommendations
4. Re-audit of fixes (if needed)
5. Public summary (optional)
```

---

## Selecting Audit Firms

### Evaluation Criteria

**Audit Firm Assessment Matrix**:

| Criteria | Weight | Evaluation Questions |
|----------|--------|---------------------|
| **Expertise** | 30% | - Years in blockchain security?<br>- Number of audits completed?<br>- Expertise in specific platform (Ethereum, Solana, etc.)?<br>- Team credentials and certifications? |
| **Reputation** | 25% | - Client testimonials and references?<br>- Public audit portfolio?<br>- Track record of finding critical bugs?<br>- Any missed vulnerabilities in past audits? |
| **Methodology** | 20% | - Automated + manual review?<br>- Formal verification capabilities?<br>- Testing approach (fuzzing, symbolic execution)?<br>- Report quality and detail? |
| **Cost & Timeline** | 15% | - Pricing structure (per LOC, fixed, hourly)?<br>- Availability and turnaround time?<br>- Included re-audit of fixes?<br>- Value for money? |
| **Communication** | 10% | - Responsiveness during evaluation?<br>- Clarity of communication?<br>- Availability for questions during audit?<br>- Post-audit support? |

**Top-Tier Audit Firms** (as of 2026):

```
Tier 1 (Premium):
├─ Trail of Bits
│   ├─ Strengths: Deep expertise, formal verification, comprehensive reports
│   ├─ Typical Cost: $50K-$200K+
│   └─ Timeline: 4-8 weeks
│
├─ OpenZeppelin
│   ├─ Strengths: Solidity experts, extensive audit history
│   ├─ Typical Cost: $40K-$150K
│   └─ Timeline: 3-6 weeks
│
├─ Consensys Diligence
│   ├─ Strengths: Ethereum ecosystem focus, MythX integration
│   ├─ Typical Cost: $35K-$120K
│   └─ Timeline: 3-5 weeks
│
└─ Certora
    ├─ Strengths: Formal verification specialists
    ├─ Typical Cost: $60K-$200K+
    └─ Timeline: 4-10 weeks

Tier 2 (High Quality):
├─ Quantstamp
├─ ChainSecurity
├─ Hacken
├─ CertiK
└─ Sigma Prime

Tier 3 (Emerging/Specialized):
├─ Code4rena (competitive audits)
├─ Sherlock (audit marketplace)
├─ Spearbit (expert network)
└─ Various independent auditors
```

**Multi-Audit Strategy**:

```
For High-Value Protocols (>$100M TVL):

1. Primary Audit (Tier 1 firm)
   └─ Comprehensive review, 4-6 weeks

2. Secondary Audit (Different Tier 1 firm)
   └─ Independent verification, 3-4 weeks
   └─ Often finds issues missed by first audit

3. Formal Verification (Certora, Runtime Verification)
   └─ Mathematical proof of critical properties
   └─ 4-8 weeks

4. Competitive Audit (Code4rena, Sherlock)
   └─ Crowdsourced security review
   └─ 1-2 weeks, $50K-$200K prize pool

5. Ongoing Bug Bounty (Immunefi, HackerOne)
   └─ Continuous security testing
   └─ $10K-$1M+ rewards for critical bugs

Total Investment: $200K-$500K+
Timeline: 3-6 months
```

---

## Audit Execution Process

### Automated Analysis Tools

**Static Analysis Tools**:

```bash
# Slither - Comprehensive Solidity analyzer
pip3 install slither-analyzer
slither . --print human-summary
slither . --detect all
slither . --exclude-dependencies

# Common Slither Detectors:
# - reentrancy-eth: Reentrancy vulnerabilities
# - uninitialized-state: Uninitialized state variables
# - suicidal: Functions allowing contract destruction
# - arbitrary-send: Arbitrary send of Ether
# - controlled-delegatecall: Controlled delegatecall

# Mythril - Symbolic execution
pip3 install mythril
myth analyze contracts/MyContract.sol --solv 0.8.19

# Manticore - Symbolic execution with concrete test generation
pip3 install manticore
manticore contracts/MyContract.sol --contract MyContract

# Securify - Automated security verification
# (Web-based: https://securify.chainsecurity.com/)

# Oyente - EVM bytecode analyzer
docker run -v $(pwd):/data luongnguyen/oyente /data/MyContract.sol
```

**Fuzzing Tools**:

```bash
# Echidna - Property-based fuzzing
# Install
wget https://github.com/crytic/echidna/releases/download/v2.2.1/echidna-2.2.1-Linux.tar.gz
tar -xzf echidna-2.2.1-Linux.tar.gz

# Create property tests
# contracts/EchidnaTest.sol
contract EchidnaTest is MyContract {
    // Invariant: Balance should never exceed total supply
    function echidna_balance_under_supply() public view returns (bool) {
        return balanceOf(msg.sender) <= totalSupply();
    }
    
    // Invariant: Total supply should remain constant (if no mint/burn)
    function echidna_supply_constant() public view returns (bool) {
        return totalSupply() == INITIAL_SUPPLY;
    }
}

# Run fuzzing
echidna contracts/EchidnaTest.sol --contract EchidnaTest --config echidna.yaml

# Foundry Fuzzing (integrated with Foundry framework)
forge test --fuzz-runs 10000

# Harvey - Greybox fuzzing
# (Commercial tool, contact Consensys)
```

**Formal Verification**:

```solidity
// Certora Specification Example
// specs/MyContract.spec

methods {
    balanceOf(address) returns (uint256) envfree
    totalSupply() returns (uint256) envfree
    transfer(address, uint256) returns (bool)
}

// Invariant: Sum of all balances equals total supply
invariant sumOfBalancesEqualsTotalSupply()
    sumOfBalances() == totalSupply()

// Rule: Transfer should preserve total supply
rule transferPreservesTotalSupply(address from, address to, uint256 amount) {
    env e;
    uint256 supplyBefore = totalSupply();
    
    transfer(e, to, amount);
    
    uint256 supplyAfter = totalSupply();
    assert supplyBefore == supplyAfter;
}

// Rule: Transfer should not create tokens
rule transferDoesNotCreateTokens(address to, uint256 amount) {
    env e;
    address from = e.msg.sender;
    
    uint256 fromBalanceBefore = balanceOf(from);
    uint256 toBalanceBefore = balanceOf(to);
    
    transfer(e, to, amount);
    
    uint256 fromBalanceAfter = balanceOf(from);
    uint256 toBalanceAfter = balanceOf(to);
    
    assert fromBalanceBefore - fromBalanceAfter == toBalanceAfter - toBalanceBefore;
}
```

### Manual Review Checklist

**Smart Contract Security Checklist**:

```markdown
## Access Control
- [ ] All privileged functions have appropriate modifiers
- [ ] Ownership transfer is two-step process
- [ ] Role-based access control properly implemented
- [ ] Initialization functions protected against re-initialization
- [ ] Default function visibility explicitly specified
- [ ] No functions accidentally public that should be internal/private

## Reentrancy
- [ ] Checks-Effects-Interactions pattern followed
- [ ] ReentrancyGuard used on state-changing functions
- [ ] No external calls before state updates
- [ ] Cross-function reentrancy considered
- [ ] Read-only reentrancy vulnerabilities checked

## Arithmetic
- [ ] Using Solidity 0.8.0+ or SafeMath
- [ ] Unchecked blocks justified and safe
- [ ] Division by zero checks where needed
- [ ] Rounding errors considered in financial calculations
- [ ] Integer overflow/underflow in loops checked

## External Calls
- [ ] Return values of external calls checked
- [ ] Gas limits for external calls considered
- [ ] Delegatecall used safely (storage layout compatibility)
- [ ] Low-level calls (.call, .delegatecall) justified
- [ ] Reentrancy from callbacks handled

## Oracle & Price Feeds
- [ ] Multiple independent oracle sources
- [ ] Price staleness checks implemented
- [ ] Deviation limits between sources
- [ ] TWAP or manipulation-resistant pricing
- [ ] Oracle failure handling (circuit breakers)

## Randomness
- [ ] No reliance on block.timestamp for randomness
- [ ] No reliance on blockhash for randomness
- [ ] Using Chainlink VRF or equivalent
- [ ] Commit-reveal for user-generated randomness

## Gas Optimization & DoS
- [ ] No unbounded loops
- [ ] Gas costs tested and documented
- [ ] Pull over push payment pattern
- [ ] Batch operations where appropriate
- [ ] Storage operations minimized

## Token Standards
- [ ] ERC-20/721/1155 compliance verified
- [ ] Transfer hooks implemented correctly
- [ ] Approval race condition mitigated
- [ ] Zero-address transfers handled
- [ ] Token burning properly implemented

## Upgradeability
- [ ] Proxy pattern correctly implemented
- [ ] Storage layout compatibility maintained
- [ ] Initialization vs constructor usage correct
- [ ] Upgrade authorization properly restricted
- [ ] Time locks on upgrades

## Economic & Game Theory
- [ ] Incentive alignment verified
- [ ] Flash loan attack vectors considered
- [ ] Front-running vulnerabilities assessed
- [ ] Economic exploits modeled
- [ ] Slippage protection implemented

## Testing
- [ ] >90% code coverage
- [ ] Edge cases tested
- [ ] Integration tests for external interactions
- [ ] Fuzzing performed
- [ ] Gas benchmarks documented
```

---

## Severity Classification

### Standard Severity Levels

**Severity Matrix**:

| Severity | Likelihood | Impact | Examples | Recommended Action |
|----------|-----------|--------|----------|-------------------|
| **Critical** | High | High | - Direct theft of funds<br>- Permanent freezing of funds<br>- Protocol insolvency | Immediate fix required before deployment |
| **High** | High | Medium<br>OR<br>Medium | High | - Theft under specific conditions<br>- Temporary freezing of funds<br>- Manipulation of governance | Fix before deployment or implement mitigation |
| **Medium** | Medium | Medium | - Griefing attacks<br>- Incorrect accounting<br>- Denial of service | Fix recommended, acceptable risk with mitigation |
| **Low** | Low | Low | - Gas inefficiencies<br>- Informational issues<br>- Best practice violations | Fix at convenience, low priority |
| **Informational** | N/A | N/A | - Code quality<br>- Documentation<br>- Style guide violations | Optional improvements |

**Detailed Severity Definitions**:

```
CRITICAL
├─ Definition: Direct, immediate threat to user funds or protocol solvency
├─ Examples:
│   ├─ Reentrancy allowing unlimited withdrawals
│   ├─ Access control bypass enabling fund theft
│   ├─ Integer overflow draining liquidity pools
│   └─ Oracle manipulation enabling under-collateralized loans
├─ Response: MUST fix before any deployment
└─ Typical Remediation: Code rewrite, architecture change

HIGH
├─ Definition: Significant risk to funds or protocol integrity under specific conditions
├─ Examples:
│   ├─ Flash loan exploits requiring specific market conditions
│   ├─ Front-running enabling unfair advantage
│   ├─ Governance manipulation with high capital requirement
│   └─ Temporary fund freezing requiring admin intervention
├─ Response: Fix before mainnet or implement strong mitigations
└─ Typical Remediation: Logic changes, additional checks, circuit breakers

MEDIUM
├─ Definition: Moderate risk or impact requiring specific conditions
├─ Examples:
│   ├─ Griefing attacks (no direct profit for attacker)
│   ├─ Incorrect fee calculations
│   ├─ DoS requiring significant resources
│   └─ Information disclosure
├─ Response: Fix recommended, acceptable with documented risk
└─ Typical Remediation: Logic improvements, rate limiting, validation

LOW
├─ Definition: Minor issues with minimal impact
├─ Examples:
│   ├─ Gas inefficiencies
│   ├─ Unclear error messages
│   ├─ Missing events
│   └─ Centralization risks (documented)
├─ Response: Fix at convenience, low priority
└─ Typical Remediation: Code optimization, UX improvements

INFORMATIONAL
├─ Definition: No security impact, code quality or best practices
├─ Examples:
│   ├─ Unused variables or functions
│   ├─ Inconsistent naming conventions
│   ├─ Missing NatSpec documentation
│   └─ Solidity version recommendations
├─ Response: Optional improvements
└─ Typical Remediation: Code cleanup, documentation
```

---

## Audit Report Structure

### Comprehensive Report Template

```markdown
# Security Audit Report

## Executive Summary

**Project**: [Project Name]
**Audit Period**: [Start Date] - [End Date]
**Auditors**: [Firm Name / Individual Auditors]
**Commit Hash**: [Git commit hash]
**Report Version**: 1.0

### Scope
- [List of contracts audited]
- [Total lines of code]
- [External dependencies]

### Summary of Findings

| Severity | Count | Resolved | Acknowledged | Unresolved |
|----------|-------|----------|--------------|------------|
| Critical | 0 | 0 | 0 | 0 |
| High | 2 | 2 | 0 | 0 |
| Medium | 5 | 4 | 1 | 0 |
| Low | 8 | 6 | 2 | 0 |
| Informational | 12 | 8 | 4 | 0 |

### Key Recommendations
1. [Most important recommendation]
2. [Second most important]
3. [Third most important]

---

## Methodology

### Automated Analysis
- Slither v0.9.3
- Mythril v0.23.15
- Echidna v2.2.1
- Certora Prover v4.10.1

### Manual Review
- Line-by-line code review
- Business logic verification
- Economic model analysis
- Integration testing

### Testing
- Unit test review (95% coverage)
- Integration test execution
- Fuzzing (10,000 runs)
- Gas optimization analysis

---

## Findings

### [H-01] Reentrancy in withdraw() Function

**Severity**: High
**Status**: Resolved
**File**: StakingPool.sol
**Lines**: 145-160

**Description**:
The `withdraw()` function makes an external call to transfer ETH before updating the user's balance, creating a reentrancy vulnerability.

**Impact**:
An attacker could recursively call `withdraw()` to drain the contract of all funds.

**Proof of Concept**:
```solidity
contract Attacker {
    StakingPool pool;
    
    function attack() external payable {
        pool.deposit{value: 1 ether}();
        pool.withdraw(1 ether);
    }
    
    receive() external payable {
        if (address(pool).balance >= 1 ether) {
            pool.withdraw(1 ether);
        }
    }
}
```

**Recommendation**:
Implement Checks-Effects-Interactions pattern:
```solidity
function withdraw(uint256 amount) external {
    require(balances[msg.sender] >= amount);
    
    // EFFECTS: Update state first
    balances[msg.sender] -= amount;
    
    // INTERACTIONS: External call last
    (bool success, ) = msg.sender.call{value: amount}("");
    require(success);
}
```

Alternatively, use OpenZeppelin's ReentrancyGuard.

**Resolution**:
Fixed in commit [hash]. ReentrancyGuard modifier added to all state-changing functions.

---

### [M-03] Oracle Price Manipulation Risk

**Severity**: Medium
**Status**: Acknowledged
**File**: LendingProtocol.sol
**Lines**: 220-235

**Description**:
The protocol uses a single Uniswap V2 pair as a price oracle, which can be manipulated via flash loans.

**Impact**:
Attacker could manipulate the price oracle to borrow under-collateralized or trigger unfair liquidations.

**Recommendation**:
1. Use Chainlink Price Feeds for primary price source
2. Implement TWAP (Time-Weighted Average Price)
3. Add deviation checks between multiple oracle sources
4. Implement circuit breakers for extreme price movements

**Team Response**:
"We acknowledge this risk. For V1, we are implementing a 1-hour TWAP and will transition to Chainlink in V2. We have also added a 10% max price deviation check and emergency pause functionality."

---

## Gas Optimization Opportunities

1. **Use `calldata` instead of `memory` for read-only function parameters**
   - Savings: ~200 gas per call
   - Locations: [List files and lines]

2. **Cache array length in loops**
   - Savings: ~100 gas per iteration
   - Locations: [List files and lines]

3. **Use `unchecked` for safe arithmetic**
   - Savings: ~50 gas per operation
   - Locations: [List files and lines]

---

## Appendix

### A. Automated Tool Output
[Attach Slither, Mythril reports]

### B. Test Coverage Report
[Attach coverage report]

### C. Formal Verification Results
[Attach Certora results]

---

**Disclaimer**: This audit does not guarantee the absence of vulnerabilities. It represents a time-bound review based on the provided scope and methodology.
```

---

## Post-Audit Remediation

### Fix Verification Process

```
Remediation Workflow:

1. Issue Prioritization
   ├─ Critical: Fix immediately
   ├─ High: Fix before deployment
   ├─ Medium: Fix or document mitigation
   └─ Low/Info: Fix at convenience

2. Fix Implementation
   ├─ Developer implements fix
   ├─ Internal code review
   ├─ Unit tests for specific fix
   └─ Regression testing

3. Fix Verification (by auditors)
   ├─ Review fix implementation
   ├─ Verify issue is resolved
   ├─ Check for new issues introduced
   └─ Update audit report status

4. Re-Audit (if significant changes)
   ├─ Scope: Only changed code + affected areas
   ├─ Timeline: 1-2 weeks
   ├─ Cost: Typically 20-40% of original audit
   └─ Deliverable: Updated audit report

5. Final Report
   ├─ All findings with resolution status
   ├─ Verification of fixes
   ├─ Remaining acknowledged risks
   └─ Public summary (optional)
```

**Fix Verification Checklist**:

```markdown
For Each Finding:

- [ ] Fix implemented in code
- [ ] Fix commit hash documented
- [ ] Unit test added for specific vulnerability
- [ ] Regression tests pass
- [ ] No new issues introduced by fix
- [ ] Gas impact of fix assessed
- [ ] Fix verified by auditor
- [ ] Status updated in audit report

For Acknowledged Risks:

- [ ] Risk documented in project documentation
- [ ] Mitigation measures implemented
- [ ] Monitoring in place
- [ ] Users informed (if applicable)
- [ ] Contingency plan prepared
```

---

## Continuous Security

### Bug Bounty Programs

**Immunefi Program Setup**:

```markdown
# Bug Bounty Program

## Rewards

| Severity | Reward |
|----------|--------|
| Critical | $50,000 - $500,000 |
| High | $10,000 - $50,000 |
| Medium | $2,000 - $10,000 |
| Low | $500 - $2,000 |

## Scope

### In-Scope
- Smart contracts: [List addresses]
- Infrastructure: Validator nodes, RPC endpoints
- Frontend: [URL] (XSS, CSRF only)

### Out-of-Scope
- Testnet contracts
- Known issues from audit reports
- Social engineering
- Physical attacks

## Rules

1. **Responsible Disclosure**
   - Report privately via Immunefi
   - Do not exploit on mainnet
   - Allow 90 days for fix before public disclosure

2. **Proof of Concept Required**
   - Detailed description
   - Steps to reproduce
   - Code or transaction demonstrating vulnerability

3. **Eligibility**
   - First reporter of unique vulnerability
   - Vulnerability must be in-scope
   - Must follow responsible disclosure

## Submission Process

1. Submit via Immunefi platform
2. Team reviews within 48 hours
3. Severity assessment and reward determination
4. Fix implementation
5. Reward payout upon fix verification
```

### Ongoing Monitoring

**Security Monitoring Stack**:

```yaml
# Forta Network - Real-time threat detection

forta_agents:
  - name: "Large Transfer Detection"
    alert_threshold: 100 ETH
    notification: slack, pagerduty
  
  - name: "Unusual Contract Interaction"
    monitor: admin_functions
    notification: slack, pagerduty
  
  - name: "Flash Loan Detection"
    monitor: large_borrows
    notification: slack
  
  - name: "Price Oracle Deviation"
    threshold: 10%
    notification: slack, pagerduty

# OpenZeppelin Defender - Automated operations

defender_sentinels:
  - name: "Admin Action Monitor"
    contracts: [governance, timelock]
    events: [ProposalCreated, ProposalExecuted]
    notification: email, telegram
  
  - name: "Pause Monitor"
    contracts: [all_pausable]
    functions: [pause, unpause]
    notification: pagerduty

# Tenderly - Transaction simulation and monitoring

tenderly_alerts:
  - name: "Failed Transaction Alert"
    condition: transaction_status == "failed"
    notification: slack
  
  - name: "High Gas Usage"
    threshold: 5000000
    notification: email
```

---

## Audit Cost and Timeline Planning

### Cost Estimation

**Pricing Models**:

```
1. Per Line of Code
   ├─ Range: $100-$300 per LOC
   ├─ Example: 1,000 LOC × $200 = $200,000
   └─ Pros: Predictable, scales with complexity

2. Fixed Price
   ├─ Range: $20K-$200K+ depending on scope
   ├─ Example: Standard DeFi protocol = $50K-$80K
   └─ Pros: Budget certainty, clear deliverables

3. Time & Materials
   ├─ Range: $200-$500 per hour
   ├─ Example: 200 hours × $300 = $60,000
   └─ Pros: Flexible scope, pay for actual work

4. Retainer
   ├─ Range: $10K-$50K per month
   ├─ Example: Ongoing security partnership
   └─ Pros: Continuous support, priority access
```

**Budget Allocation Example** (Total: $150K):

```
Primary Audit (Tier 1 firm): $70,000
├─ Smart contract review
├─ Economic model analysis
└─ Initial report + fix verification

Secondary Audit (Tier 2 firm): $30,000
├─ Independent review
└─ Catch issues missed by first audit

Formal Verification: $25,000
├─ Critical invariants
└─ Mathematical proofs

Competitive Audit: $15,000
├─ Code4rena contest
└─ Prize pool

Bug Bounty (Annual): $10,000
├─ Immunefi program
└─ Ongoing rewards
```

### Timeline Planning

```
Typical Audit Timeline (8 weeks total):

Week 1-2: Preparation
├─ Finalize code freeze
├─ Prepare documentation
├─ Onboard audit team
└─ Kick-off meeting

Week 3-5: Audit Execution
├─ Automated analysis
├─ Manual review
├─ Testing and verification
└─ Draft report preparation

Week 6: Initial Report
├─ Receive initial findings
├─ Clarification discussions
└─ Prioritize fixes

Week 7: Remediation
├─ Implement fixes
├─ Internal testing
└─ Submit fixes to auditors

Week 8: Final Report
├─ Fix verification
├─ Final report delivery
└─ Public summary (optional)

Post-Audit:
├─ Deploy to mainnet
├─ Launch bug bounty
└─ Ongoing monitoring
```
