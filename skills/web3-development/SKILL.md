---
name: web3-development
description: "Master Web3 development for building decentralized applications (dApps). Covers Web3 architecture, frontend integration with blockchain, Web3 libraries (Web3.js, Ethers.js, Viem), wallet integration (MetaMask, WalletConnect), decentralized storage (IPFS, Arweave), blockchain data indexing (The Graph, SubQuery), dApp frameworks (Thirdweb, Scaffold-ETH), testing strategies, and deployment. Use for: building dApp frontends, integrating smart contracts with web applications, implementing wallet connections, working with decentralized storage, querying blockchain data, creating NFT marketplaces, developing DeFi interfaces, and deploying full-stack Web3 applications."
---

# Web3 Development

## Overview

Web3 development represents the next evolution of the internet, enabling decentralized applications (dApps) that interact directly with blockchain networks. Unlike traditional Web2 applications that rely on centralized servers, Web3 applications leverage blockchain technology, smart contracts, and decentralized storage to create trustless, transparent, and user-controlled experiences.

## Web3 vs Web2

### Key Differences

**Web2 (Traditional Web):**
- Centralized servers and databases
- Platform-owned user data
- Intermediaries control transactions
- Single points of failure
- Permissioned access

**Web3 (Decentralized Web):**
- Distributed blockchain networks
- User-owned data and assets
- Peer-to-peer transactions
- Resilient, distributed architecture
- Permissionless participation

### Web3 Stack Components

1. **Blockchain Layer**: Ethereum, Polygon, Solana, etc.
2. **Smart Contracts**: On-chain business logic
3. **Storage Layer**: IPFS, Arweave, Filecoin
4. **Indexing Layer**: The Graph, SubQuery
5. **API Layer**: Alchemy, Infura, Moralis
6. **Frontend**: React, Next.js, Vue.js
7. **Web3 Libraries**: Ethers.js, Web3.js, Viem
8. **Wallet Integration**: MetaMask, WalletConnect

## Web3 Libraries

### Ethers.js

**Overview:**
Lightweight, modern library for Ethereum interaction with intuitive API and TypeScript support.

**Installation:**
```bash
npm install ethers
```

**Basic Usage:**
```javascript
import { ethers } from 'ethers';

// Connect to Ethereum
const provider = new ethers.providers.Web3Provider(window.ethereum);
const signer = provider.getSigner();

// Get account
const address = await signer.getAddress();
const balance = await provider.getBalance(address);

// Interact with contract
const contract = new ethers.Contract(contractAddress, abi, signer);
const tx = await contract.transfer(recipient, amount);
await tx.wait();
```

**Key Features:**
- Small bundle size (~88 KB)
- ENS (Ethereum Name Service) support
- Human-readable ABIs
- Extensive documentation
- TypeScript-first design

### Web3.js

**Overview:**
Original Ethereum JavaScript library, widely adopted with comprehensive features.

**Installation:**
```bash
npm install web3
```

**Basic Usage:**
```javascript
import Web3 from 'web3';

const web3 = new Web3(window.ethereum);

// Get accounts
const accounts = await web3.eth.getAccounts();

// Send transaction
await web3.eth.sendTransaction({
  from: accounts[0],
  to: recipient,
  value: web3.utils.toWei('1', 'ether')
});

// Contract interaction
const contract = new web3.eth.Contract(abi, contractAddress);
const result = await contract.methods.balanceOf(address).call();
```

### Viem

**Overview:**
Modern, type-safe alternative with excellent TypeScript support and performance.

**Installation:**
```bash
npm install viem
```

**Basic Usage:**
```typescript
import { createPublicClient, http } from 'viem';
import { mainnet } from 'viem/chains';

const client = createPublicClient({
  chain: mainnet,
  transport: http()
});

const balance = await client.getBalance({ 
  address: '0x...' 
});
```

## Wallet Integration

### MetaMask

**Connection:**
```javascript
// Request account access
async function connectWallet() {
  if (typeof window.ethereum !== 'undefined') {
    try {
      const accounts = await window.ethereum.request({ 
        method: 'eth_requestAccounts' 
      });
      return accounts[0];
    } catch (error) {
      console.error('User rejected connection');
    }
  } else {
    alert('Please install MetaMask!');
  }
}

// Listen for account changes
window.ethereum.on('accountsChanged', (accounts) => {
  console.log('Account changed:', accounts[0]);
});

// Listen for chain changes
window.ethereum.on('chainChanged', (chainId) => {
  window.location.reload();
});
```

**Network Switching:**
```javascript
async function switchNetwork(chainId) {
  try {
    await window.ethereum.request({
      method: 'wallet_switchEthereumChain',
      params: [{ chainId: `0x${chainId.toString(16)}` }]
    });
  } catch (error) {
    // Chain not added, add it
    if (error.code === 4902) {
      await window.ethereum.request({
        method: 'wallet_addEthereumChain',
        params: [{
          chainId: `0x${chainId.toString(16)}`,
          chainName: 'Polygon',
          nativeCurrency: { name: 'MATIC', symbol: 'MATIC', decimals: 18 },
          rpcUrls: ['https://polygon-rpc.com'],
          blockExplorerUrls: ['https://polygonscan.com']
        }]
      });
    }
  }
}
```

### WalletConnect

**Setup:**
```bash
npm install @walletconnect/web3-provider
```

**Implementation:**
```javascript
import WalletConnectProvider from '@walletconnect/web3-provider';

const provider = new WalletConnectProvider({
  infuraId: 'YOUR_INFURA_ID',
  qrcode: true
});

await provider.enable();

const web3 = new Web3(provider);
```

### RainbowKit (Modern Solution)

**Installation:**
```bash
npm install @rainbow-me/rainbowkit wagmi viem
```

**Setup:**
```typescript
import '@rainbow-me/rainbowkit/styles.css';
import { getDefaultWallets, RainbowKitProvider } from '@rainbow-me/rainbowkit';
import { configureChains, createConfig, WagmiConfig } from 'wagmi';
import { mainnet, polygon } from 'wagmi/chains';

const { chains, publicClient } = configureChains(
  [mainnet, polygon],
  [/* providers */]
);

const { connectors } = getDefaultWallets({
  appName: 'My dApp',
  projectId: 'YOUR_PROJECT_ID',
  chains
});

const wagmiConfig = createConfig({
  autoConnect: true,
  connectors,
  publicClient
});

function App() {
  return (
    <WagmiConfig config={wagmiConfig}>
      <RainbowKitProvider chains={chains}>
        {/* Your app */}
      </RainbowKitProvider>
    </WagmiConfig>
  );
}
```

## Decentralized Storage

### IPFS (InterPlanetary File System)

**Overview:**
Peer-to-peer distributed file system for decentralized storage.

**Using IPFS HTTP Client:**
```bash
npm install ipfs-http-client
```

```javascript
import { create } from 'ipfs-http-client';

const client = create({ url: 'https://ipfs.infura.io:5001' });

// Upload file
async function uploadToIPFS(file) {
  const added = await client.add(file);
  const url = `https://ipfs.io/ipfs/${added.path}`;
  return url;
}

// Upload JSON metadata
async function uploadMetadata(metadata) {
  const added = await client.add(JSON.stringify(metadata));
  return added.path;
}
```

**Using Pinata (IPFS Pinning Service):**
```javascript
const pinataSDK = require('@pinata/sdk');
const pinata = new pinataSDK(apiKey, apiSecret);

const result = await pinata.pinFileToIPFS(readableStream, {
  pinataMetadata: { name: 'MyFile' }
});

console.log('IPFS Hash:', result.IpfsHash);
```

### Arweave

**Overview:**
Permanent, decentralized storage with one-time payment model.

**Installation:**
```bash
npm install arweave
```

**Usage:**
```javascript
import Arweave from 'arweave';

const arweave = Arweave.init({
  host: 'arweave.net',
  port: 443,
  protocol: 'https'
});

// Upload data
const transaction = await arweave.createTransaction({
  data: 'Hello, Arweave!'
}, wallet);

await arweave.transactions.sign(transaction, wallet);
await arweave.transactions.post(transaction);

console.log('Transaction ID:', transaction.id);
```

## Blockchain Data Indexing

### The Graph

**Overview:**
Decentralized protocol for indexing and querying blockchain data using GraphQL.

**Subgraph Definition (subgraph.yaml):**
```yaml
specVersion: 0.0.4
schema:
  file: ./schema.graphql
dataSources:
  - kind: ethereum
    name: MyContract
    network: mainnet
    source:
      address: "0x..."
      abi: MyContract
      startBlock: 12345678
    mapping:
      kind: ethereum/events
      apiVersion: 0.0.6
      language: wasm/assemblyscript
      entities:
        - Transfer
      abis:
        - name: MyContract
          file: ./abis/MyContract.json
      eventHandlers:
        - event: Transfer(indexed address,indexed address,uint256)
          handler: handleTransfer
      file: ./src/mapping.ts
```

**Schema (schema.graphql):**
```graphql
type Transfer @entity {
  id: ID!
  from: Bytes!
  to: Bytes!
  amount: BigInt!
  timestamp: BigInt!
}
```

**Querying:**
```javascript
import { ApolloClient, InMemoryCache, gql } from '@apollo/client';

const client = new ApolloClient({
  uri: 'https://api.thegraph.com/subgraphs/name/username/subgraph',
  cache: new InMemoryCache()
});

const TRANSFERS_QUERY = gql`
  query GetTransfers($first: Int!) {
    transfers(first: $first, orderBy: timestamp, orderDirection: desc) {
      id
      from
      to
      amount
      timestamp
    }
  }
`;

const { data } = await client.query({
  query: TRANSFERS_QUERY,
  variables: { first: 10 }
});
```

## Full-Stack dApp Frameworks

### Thirdweb

**Overview:**
Comprehensive Web3 development platform with pre-built contracts and SDKs.

**Installation:**
```bash
npx thirdweb create app
```

**Usage:**
```typescript
import { ThirdwebProvider, useContract, useContractRead } from '@thirdweb-dev/react';

function App() {
  return (
    <ThirdwebProvider activeChain="ethereum">
      <MyComponent />
    </ThirdwebProvider>
  );
}

function MyComponent() {
  const { contract } = useContract(contractAddress);
  const { data, isLoading } = useContractRead(contract, "balanceOf", [address]);
  
  return <div>Balance: {data?.toString()}</div>;
}
```

### Scaffold-ETH

**Overview:**
Rapid prototyping framework with pre-configured stack (Hardhat, React, Ethers.js).

**Setup:**
```bash
git clone https://github.com/scaffold-eth/scaffold-eth-2.git
cd scaffold-eth-2
yarn install
yarn chain  # Start local blockchain
yarn deploy # Deploy contracts
yarn start  # Start frontend
```

## React Hooks for Web3

### Wagmi Hooks

**Installation:**
```bash
npm install wagmi viem
```

**Common Hooks:**
```typescript
import { useAccount, useBalance, useContractRead, useContractWrite } from 'wagmi';

function MyComponent() {
  // Get connected account
  const { address, isConnected } = useAccount();
  
  // Get balance
  const { data: balance } = useBalance({ address });
  
  // Read from contract
  const { data: tokenBalance } = useContractRead({
    address: contractAddress,
    abi: contractABI,
    functionName: 'balanceOf',
    args: [address]
  });
  
  // Write to contract
  const { write: transfer } = useContractWrite({
    address: contractAddress,
    abi: contractABI,
    functionName: 'transfer'
  });
  
  return (
    <div>
      <p>Address: {address}</p>
      <p>Balance: {balance?.formatted} ETH</p>
      <button onClick={() => transfer({ args: [recipient, amount] })}>
        Transfer
      </button>
    </div>
  );
}
```

## Testing dApps

### Frontend Testing

**Jest + React Testing Library:**
```javascript
import { render, screen, waitFor } from '@testing-library/react';
import { WagmiConfig } from 'wagmi';
import MyComponent from './MyComponent';

test('displays wallet connection', async () => {
  render(
    <WagmiConfig config={mockConfig}>
      <MyComponent />
    </WagmiConfig>
  );
  
  await waitFor(() => {
    expect(screen.getByText(/connected/i)).toBeInTheDocument();
  });
});
```

### E2E Testing with Synpress

**Installation:**
```bash
npm install --save-dev @synthetixio/synpress
```

**Test:**
```javascript
describe('dApp E2E', () => {
  it('connects wallet and interacts with contract', () => {
    cy.visit('/');
    cy.get('[data-testid="connect-wallet"]').click();
    cy.acceptMetamaskAccess();
    cy.get('[data-testid="transfer-button"]').click();
    cy.confirmMetamaskTransaction();
  });
});
```

## Deployment

### Frontend Deployment

**Vercel:**
```bash
npm install -g vercel
vercel
```

**IPFS (Decentralized):**
```bash
npm run build
ipfs add -r build/
```

**Fleek (IPFS + CDN):**
```bash
fleek site:deploy
```

### Environment Variables

```env
REACT_APP_INFURA_ID=your_infura_id
REACT_APP_CONTRACT_ADDRESS=0x...
REACT_APP_CHAIN_ID=1
```

## Best Practices

### Security
1. **Validate user inputs** before sending transactions
2. **Use environment variables** for sensitive data
3. **Implement transaction confirmations** before UI updates
4. **Handle errors gracefully** with user-friendly messages
5. **Verify contract addresses** to prevent phishing

### Performance
1. **Cache blockchain data** to reduce RPC calls
2. **Use The Graph** for complex queries
3. **Implement pagination** for large datasets
4. **Optimize bundle size** (tree-shaking, code splitting)
5. **Use React.memo** for expensive components

### User Experience
1. **Show loading states** during transactions
2. **Display transaction status** (pending, confirmed, failed)
3. **Provide clear error messages**
4. **Support multiple wallets**
5. **Implement mobile-responsive design**

## Common Patterns

### Transaction Flow
```typescript
const [txStatus, setTxStatus] = useState('idle');

async function handleTransaction() {
  try {
    setTxStatus('pending');
    const tx = await contract.transfer(recipient, amount);
    setTxStatus('confirming');
    await tx.wait();
    setTxStatus('success');
  } catch (error) {
    setTxStatus('error');
    console.error(error);
  }
}
```

### Gas Estimation
```javascript
const gasEstimate = await contract.estimateGas.transfer(recipient, amount);
const gasPrice = await provider.getGasPrice();
const totalCost = gasEstimate.mul(gasPrice);
```

### Event Listening
```javascript
contract.on('Transfer', (from, to, amount, event) => {
  console.log(`Transfer: ${from} -> ${to}: ${amount}`);
  // Update UI
});

// Cleanup
return () => {
  contract.removeAllListeners('Transfer');
};
```

## Conclusion

Web3 development combines traditional web development skills with blockchain technology, creating decentralized applications that empower users with ownership and control. Mastering Web3 libraries, wallet integration, decentralized storage, and blockchain data indexing is essential for building production-ready dApps. As the ecosystem matures, new tools and frameworks continue to emerge, making Web3 development more accessible and powerful.
