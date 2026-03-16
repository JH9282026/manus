# Web3 Architecture Patterns

## Introduction

This reference covers architectural patterns, best practices, and advanced techniques for building scalable, secure, and user-friendly Web3 applications.

## Application Architecture

### Layered Architecture

**Typical dApp Stack:**
```
┌────────────────────────────────┐
│  Frontend (React/Next.js)      │
├────────────────────────────────┤
│  Web3 Libraries (Ethers/Wagmi) │
├────────────────────────────────┤
│  RPC Provider (Alchemy/Infura)│
├────────────────────────────────┤
│  Blockchain (Ethereum/Polygon) │
├────────────────────────────────┤
│  Smart Contracts              │
└────────────────────────────────┘

Supporting Services:
- IPFS/Arweave (Storage)
- The Graph (Indexing)
- Wallet Providers (MetaMask)
```

### Hybrid Architecture (Web2 + Web3)

**Benefits:**
- Improved performance
- Better UX for non-critical data
- Cost optimization
- Gradual migration path

**Implementation:**
```typescript
interface DataSource {
  onChain: boolean;
  endpoint: string;
}

class HybridDataManager {
  async getData(key: string): Promise<any> {
    const source = this.getDataSource(key);
    
    if (source.onChain) {
      return await this.fetchFromBlockchain(key);
    } else {
      return await this.fetchFromAPI(source.endpoint);
    }
  }
  
  private getDataSource(key: string): DataSource {
    // Critical data: on-chain
    // Metadata, images: off-chain
    const onChainKeys = ['balance', 'ownership', 'votes'];
    return {
      onChain: onChainKeys.includes(key),
      endpoint: onChainKeys.includes(key) ? '' : `https://api.example.com/${key}`
    };
  }
}
```

## State Management

### Context API for Web3

```typescript
import { createContext, useContext, useState, useEffect } from 'react';
import { ethers } from 'ethers';

interface Web3ContextType {
  provider: ethers.providers.Web3Provider | null;
  signer: ethers.Signer | null;
  account: string | null;
  chainId: number | null;
  connect: () => Promise<void>;
  disconnect: () => void;
}

const Web3Context = createContext<Web3ContextType | undefined>(undefined);

export function Web3Provider({ children }: { children: React.ReactNode }) {
  const [provider, setProvider] = useState<ethers.providers.Web3Provider | null>(null);
  const [signer, setSigner] = useState<ethers.Signer | null>(null);
  const [account, setAccount] = useState<string | null>(null);
  const [chainId, setChainId] = useState<number | null>(null);
  
  const connect = async () => {
    if (typeof window.ethereum !== 'undefined') {
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const accounts = await provider.send('eth_requestAccounts', []);
      const signer = provider.getSigner();
      const network = await provider.getNetwork();
      
      setProvider(provider);
      setSigner(signer);
      setAccount(accounts[0]);
      setChainId(network.chainId);
    }
  };
  
  const disconnect = () => {
    setProvider(null);
    setSigner(null);
    setAccount(null);
    setChainId(null);
  };
  
  useEffect(() => {
    if (window.ethereum) {
      window.ethereum.on('accountsChanged', (accounts: string[]) => {
        setAccount(accounts[0] || null);
      });
      
      window.ethereum.on('chainChanged', () => {
        window.location.reload();
      });
    }
  }, []);
  
  return (
    <Web3Context.Provider value={{ provider, signer, account, chainId, connect, disconnect }}>
      {children}
    </Web3Context.Provider>
  );
}

export function useWeb3() {
  const context = useContext(Web3Context);
  if (!context) throw new Error('useWeb3 must be used within Web3Provider');
  return context;
}
```

### Redux for Complex State

```typescript
import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface Web3State {
  account: string | null;
  balance: string;
  transactions: Transaction[];
  loading: boolean;
}

const web3Slice = createSlice({
  name: 'web3',
  initialState: {
    account: null,
    balance: '0',
    transactions: [],
    loading: false
  } as Web3State,
  reducers: {
    setAccount: (state, action: PayloadAction<string>) => {
      state.account = action.payload;
    },
    setBalance: (state, action: PayloadAction<string>) => {
      state.balance = action.payload;
    },
    addTransaction: (state, action: PayloadAction<Transaction>) => {
      state.transactions.push(action.payload);
    },
    setLoading: (state, action: PayloadAction<boolean>) => {
      state.loading = action.payload;
    }
  }
});

export const { setAccount, setBalance, addTransaction, setLoading } = web3Slice.actions;
export default web3Slice.reducer;
```

## Caching Strategies

### React Query for Blockchain Data

```typescript
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { ethers } from 'ethers';

function useTokenBalance(address: string, tokenAddress: string) {
  return useQuery(
    ['tokenBalance', address, tokenAddress],
    async () => {
      const contract = new ethers.Contract(tokenAddress, ERC20_ABI, provider);
      const balance = await contract.balanceOf(address);
      return ethers.utils.formatEther(balance);
    },
    {
      staleTime: 30000, // 30 seconds
      cacheTime: 300000, // 5 minutes
      refetchInterval: 60000, // Refetch every minute
      enabled: !!address && !!tokenAddress
    }
  );
}

function useTransfer() {
  const queryClient = useQueryClient();
  
  return useMutation(
    async ({ to, amount }: { to: string; amount: string }) => {
      const tx = await contract.transfer(to, ethers.utils.parseEther(amount));
      return await tx.wait();
    },
    {
      onSuccess: () => {
        // Invalidate and refetch balance
        queryClient.invalidateQueries(['tokenBalance']);
      }
    }
  );
}
```

### Local Storage for User Preferences

```typescript
class PreferencesManager {
  private static STORAGE_KEY = 'dapp_preferences';
  
  static save(preferences: UserPreferences): void {
    localStorage.setItem(this.STORAGE_KEY, JSON.stringify(preferences));
  }
  
  static load(): UserPreferences | null {
    const data = localStorage.getItem(this.STORAGE_KEY);
    return data ? JSON.parse(data) : null;
  }
  
  static clear(): void {
    localStorage.removeItem(this.STORAGE_KEY);
  }
}

interface UserPreferences {
  theme: 'light' | 'dark';
  defaultSlippage: number;
  preferredWallet: string;
  notifications: boolean;
}
```

## Error Handling

### Comprehensive Error Handler

```typescript
class Web3ErrorHandler {
  static handle(error: any): { message: string; code?: number } {
    // User rejected transaction
    if (error.code === 4001) {
      return { message: 'Transaction rejected by user', code: 4001 };
    }
    
    // Insufficient funds
    if (error.code === 'INSUFFICIENT_FUNDS') {
      return { message: 'Insufficient funds for transaction', code: -32000 };
    }
    
    // Network error
    if (error.code === 'NETWORK_ERROR') {
      return { message: 'Network connection failed. Please try again.', code: -32603 };
    }
    
    // Contract revert
    if (error.code === 'CALL_EXCEPTION') {
      const reason = error.reason || 'Transaction would fail';
      return { message: `Contract error: ${reason}`, code: -32015 };
    }
    
    // Gas estimation failed
    if (error.code === 'UNPREDICTABLE_GAS_LIMIT') {
      return { message: 'Cannot estimate gas. Transaction may fail.', code: -32016 };
    }
    
    // Generic error
    return { message: error.message || 'An unknown error occurred' };
  }
  
  static async withRetry<T>(
    fn: () => Promise<T>,
    maxRetries: number = 3,
    delay: number = 1000
  ): Promise<T> {
    for (let i = 0; i < maxRetries; i++) {
      try {
        return await fn();
      } catch (error) {
        if (i === maxRetries - 1) throw error;
        await new Promise(resolve => setTimeout(resolve, delay * (i + 1)));
      }
    }
    throw new Error('Max retries exceeded');
  }
}

// Usage
try {
  const tx = await contract.transfer(to, amount);
  await tx.wait();
} catch (error) {
  const { message, code } = Web3ErrorHandler.handle(error);
  toast.error(message);
  console.error('Transaction failed:', code, error);
}
```

## Performance Optimization

### Batch RPC Calls

```typescript
class BatchProvider {
  private provider: ethers.providers.JsonRpcProvider;
  private batchQueue: any[] = [];
  private batchTimeout: NodeJS.Timeout | null = null;
  
  constructor(rpcUrl: string) {
    this.provider = new ethers.providers.JsonRpcProvider(rpcUrl);
  }
  
  async call(method: string, params: any[]): Promise<any> {
    return new Promise((resolve, reject) => {
      this.batchQueue.push({ method, params, resolve, reject });
      
      if (!this.batchTimeout) {
        this.batchTimeout = setTimeout(() => this.executeBatch(), 50);
      }
    });
  }
  
  private async executeBatch(): void {
    const batch = this.batchQueue.splice(0);
    this.batchTimeout = null;
    
    const requests = batch.map((item, index) => ({
      jsonrpc: '2.0',
      id: index,
      method: item.method,
      params: item.params
    }));
    
    try {
      const responses = await this.provider.send('eth_batch', requests);
      
      responses.forEach((response: any, index: number) => {
        if (response.error) {
          batch[index].reject(response.error);
        } else {
          batch[index].resolve(response.result);
        }
      });
    } catch (error) {
      batch.forEach(item => item.reject(error));
    }
  }
}
```

### Lazy Loading Components

```typescript
import { lazy, Suspense } from 'react';

const NFTGallery = lazy(() => import('./components/NFTGallery'));
const TokenSwap = lazy(() => import('./components/TokenSwap'));

function App() {
  return (
    <Suspense fallback={<LoadingSpinner />}>
      <Routes>
        <Route path="/nfts" element={<NFTGallery />} />
        <Route path="/swap" element={<TokenSwap />} />
      </Routes>
    </Suspense>
  );
}
```

## Security Best Practices

### Input Validation

```typescript
class InputValidator {
  static isValidAddress(address: string): boolean {
    return ethers.utils.isAddress(address);
  }
  
  static isValidAmount(amount: string, decimals: number = 18): boolean {
    try {
      const parsed = ethers.utils.parseUnits(amount, decimals);
      return parsed.gt(0);
    } catch {
      return false;
    }
  }
  
  static sanitizeInput(input: string): string {
    return input.trim().replace(/[^a-zA-Z0-9.]/g, '');
  }
}

// Usage in component
function TransferForm() {
  const [recipient, setRecipient] = useState('');
  const [amount, setAmount] = useState('');
  const [errors, setErrors] = useState<string[]>([]);
  
  const validate = () => {
    const newErrors: string[] = [];
    
    if (!InputValidator.isValidAddress(recipient)) {
      newErrors.push('Invalid recipient address');
    }
    
    if (!InputValidator.isValidAmount(amount)) {
      newErrors.push('Invalid amount');
    }
    
    setErrors(newErrors);
    return newErrors.length === 0;
  };
  
  const handleSubmit = async () => {
    if (!validate()) return;
    // Proceed with transaction
  };
}
```

### Transaction Simulation

```typescript
async function simulateTransaction(
  contract: ethers.Contract,
  method: string,
  args: any[]
): Promise<{ success: boolean; error?: string }> {
  try {
    // Estimate gas to check if transaction would succeed
    await contract.estimateGas[method](...args);
    
    // Call statically to get return value
    const result = await contract.callStatic[method](...args);
    
    return { success: true };
  } catch (error: any) {
    return {
      success: false,
      error: Web3ErrorHandler.handle(error).message
    };
  }
}

// Usage
const simulation = await simulateTransaction(contract, 'transfer', [to, amount]);
if (!simulation.success) {
  alert(`Transaction would fail: ${simulation.error}`);
  return;
}

// Proceed with actual transaction
const tx = await contract.transfer(to, amount);
```

## Testing Strategies

### Mock Provider for Unit Tests

```typescript
import { MockProvider } from '@ethereum-waffle/provider';

describe('TokenBalance Component', () => {
  let provider: MockProvider;
  let wallets: Wallet[];
  
  beforeEach(() => {
    provider = new MockProvider();
    wallets = provider.getWallets();
  });
  
  it('displays correct balance', async () => {
    const balance = await provider.getBalance(wallets[0].address);
    
    render(
      <Web3Provider value={{ provider, account: wallets[0].address }}>
        <TokenBalance />
      </Web3Provider>
    );
    
    expect(screen.getByText(ethers.utils.formatEther(balance))).toBeInTheDocument();
  });
});
```

## Conclusion

Building production-ready Web3 applications requires careful architectural decisions, robust error handling, performance optimization, and security best practices. These patterns provide a foundation for creating scalable, maintainable, and user-friendly dApps.
