# Distributed Training in PyTorch

## Data Parallel vs Distributed Data Parallel

**DataParallel (DP):**
- Single-process, multi-thread
- Limited to single machine
- GIL bottleneck
- Simpler but slower

**DistributedDataParallel (DDP):**
- Multi-process
- Works across multiple machines
- Better performance
- Recommended for production

## DDP Setup

```python
import torch.distributed as dist
import torch.multiprocessing as mp
from torch.nn.parallel import DistributedDataParallel as DDP

def setup(rank, world_size):
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = '12355'
    dist.init_process_group("nccl", rank=rank, world_size=world_size)

def cleanup():
    dist.destroy_process_group()

def train(rank, world_size):
    setup(rank, world_size)
    
    model = MyModel().to(rank)
    ddp_model = DDP(model, device_ids=[rank])
    
    # Training loop
    for data, labels in dataloader:
        outputs = ddp_model(data)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
    
    cleanup()

if __name__ == '__main__':
    world_size = torch.cuda.device_count()
    mp.spawn(train, args=(world_size,), nprocs=world_size, join=True)
```

## FSDP for Large Models

Fully Sharded Data Parallel shards model parameters, gradients, and optimizer states.

```python
from torch.distributed.fsdp import FullyShardedDataParallel as FSDP
from torch.distributed.fsdp.wrap import size_based_auto_wrap_policy

model = MyLargeModel()

auto_wrap_policy = functools.partial(
    size_based_auto_wrap_policy, min_num_params=1e8
)

fsdp_model = FSDP(
    model,
    auto_wrap_policy=auto_wrap_policy,
    device_id=torch.cuda.current_device()
)
```
