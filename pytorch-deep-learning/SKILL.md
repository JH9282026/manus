---
name: pytorch-deep-learning
description: "Build and train deep learning models using PyTorch. Use for: creating custom neural networks with nn.Module, implementing CNNs and RNNs, building transformers and attention mechanisms, developing GANs and autoencoders, custom training loops with autograd, distributed training with DDP and FSDP, model optimization with pruning and quantization, deploying with TorchServe and ONNX, and leveraging dynamic computation graphs for research flexibility."
---

# PyTorch Deep Learning

Build flexible, research-friendly deep learning models using Facebook's PyTorch framework.

## Overview

PyTorch is an open-source deep learning framework emphasizing flexibility, Pythonic syntax, and dynamic computation graphs. Developed by Meta AI, it's the preferred choice for research due to its intuitive API and eager execution model. PyTorch excels in computer vision, NLP, reinforcement learning, and generative AI, with strong support for distributed training and production deployment.

## Core PyTorch Concepts

### Tensors and Operations

```python
import torch

# Creating tensors
x = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
y = torch.zeros(2, 3)
z = torch.randn(3, 4)

# Tensor operations
a = torch.matmul(x, x.T)
b = x + 10
c = x.view(-1)  # Reshape

# GPU acceleration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
x_gpu = x.to(device)
```

### Autograd: Automatic Differentiation

```python
x = torch.tensor([2.0, 3.0], requires_grad=True)
y = x ** 2
z = y.sum()
z.backward()  # Compute gradients
print(x.grad)  # dz/dx = 2x
```

### Building Neural Networks

```python
import torch.nn as nn

class SimpleNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super().__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.5)
        self.fc2 = nn.Linear(hidden_size, num_classes)
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.dropout(x)
        return self.fc2(x)
```

## Computer Vision

### CNNs and Transfer Learning

```python
import torchvision.models as models

# Pretrained ResNet
model = models.resnet50(pretrained=True)
for param in model.parameters():
    param.requires_grad = False

# Replace final layer
model.fc = nn.Linear(model.fc.in_features, num_classes)
```

### Data Augmentation

```python
from torchvision import transforms

train_transform = transforms.Compose([
    transforms.RandomResizedCrop(224),
    transforms.RandomHorizontalFlip(),
    transforms.ColorJitter(brightness=0.2),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])
```

## Natural Language Processing

### LSTM Classifier

```python
class LSTMClassifier(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim, num_classes):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, num_layers=2, 
                           batch_first=True, bidirectional=True)
        self.fc = nn.Linear(hidden_dim * 2, num_classes)
    
    def forward(self, x):
        embedded = self.embedding(x)
        _, (hidden, _) = self.lstm(embedded)
        hidden = torch.cat((hidden[-2,:,:], hidden[-1,:,:]), dim=1)
        return self.fc(hidden)
```

### Transformer Architecture

```python
class TransformerModel(nn.Module):
    def __init__(self, vocab_size, d_model=512, nhead=8, num_layers=6):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.pos_encoder = PositionalEncoding(d_model)
        encoder_layer = nn.TransformerEncoderLayer(d_model, nhead)
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers)
        self.fc = nn.Linear(d_model, vocab_size)
    
    def forward(self, src):
        src = self.embedding(src) * math.sqrt(self.d_model)
        src = self.pos_encoder(src)
        output = self.transformer(src)
        return self.fc(output)
```

## Training and Optimization

### Custom Training Loop

```python
def train_epoch(model, dataloader, criterion, optimizer, device):
    model.train()
    total_loss = 0
    
    for data, target in dataloader:
        data, target = data.to(device), target.to(device)
        
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item()
    
    return total_loss / len(dataloader)
```

### Learning Rate Scheduling

```python
from torch.optim.lr_scheduler import CosineAnnealingLR, ReduceLROnPlateau

scheduler = CosineAnnealingLR(optimizer, T_max=100)
# or
scheduler = ReduceLROnPlateau(optimizer, mode='min', factor=0.5, patience=5)
```

### Mixed Precision Training

```python
from torch.cuda.amp import autocast, GradScaler

scaler = GradScaler()

for data, target in train_loader:
    optimizer.zero_grad()
    
    with autocast():
        output = model(data)
        loss = criterion(output, target)
    
    scaler.scale(loss).backward()
    scaler.step(optimizer)
    scaler.update()
```

## Distributed Training

### Distributed Data Parallel (DDP)

```python
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP

def setup(rank, world_size):
    dist.init_process_group("nccl", rank=rank, world_size=world_size)

def train_ddp(rank, world_size):
    setup(rank, world_size)
    model = MyModel().to(rank)
    ddp_model = DDP(model, device_ids=[rank])
    
    train_sampler = torch.utils.data.distributed.DistributedSampler(train_dataset)
    train_loader = DataLoader(train_dataset, batch_size=32, sampler=train_sampler)
    
    # Training loop
    for epoch in range(num_epochs):
        train_sampler.set_epoch(epoch)
        for data, target in train_loader:
            # Training code
            pass
```

### Fully Sharded Data Parallel (FSDP)

```python
from torch.distributed.fsdp import FullyShardedDataParallel as FSDP

model = MyLargeModel()
fsdp_model = FSDP(model, device_id=torch.cuda.current_device())
```

## Model Optimization

### Quantization

```python
# Post-training quantization
model.eval()
model.qconfig = torch.quantization.get_default_qconfig('fbgemm')
torch.quantization.prepare(model, inplace=True)

# Calibrate
with torch.no_grad():
    for data, _ in calibration_loader:
        model(data)

torch.quantization.convert(model, inplace=True)
```

### Pruning

```python
import torch.nn.utils.prune as prune

# Prune 30% of connections
prune.l1_unstructured(model.conv1, name='weight', amount=0.3)

# Global pruning
parameters_to_prune = (
    (model.conv1, 'weight'),
    (model.fc1, 'weight'),
)
prune.global_unstructured(parameters_to_prune, 
                         pruning_method=prune.L1Unstructured, 
                         amount=0.2)
```

## Deployment

### TorchScript

```python
# Tracing
example_input = torch.rand(1, 3, 224, 224)
traced_model = torch.jit.trace(model, example_input)
traced_model.save('model_traced.pt')

# Scripting
scripted_model = torch.jit.script(model)
scripted_model.save('model_scripted.pt')
```

### ONNX Export

```python
dummy_input = torch.randn(1, 3, 224, 224)
torch.onnx.export(model, dummy_input, "model.onnx", 
                  export_params=True, opset_version=11)
```

### TorchServe

```bash
# Archive model
torch-model-archiver --model-name my_model --version 1.0 \
    --model-file model.py --serialized-file model.pth

# Start server
torchserve --start --model-store model_store --models my_model=my_model.mar
```

## Best Practices

**Model Design:**
- Use `nn.ModuleList` for dynamic layers
- Implement proper weight initialization
- Use `register_buffer` for non-trainable tensors

**Training:**
- Always call `model.train()` and `model.eval()`
- Use `torch.no_grad()` for inference
- Implement gradient clipping for RNNs
- Monitor gradient norms

**Memory Management:**
- Use gradient accumulation for large batches
- Apply gradient checkpointing for large models
- Clear cache with `torch.cuda.empty_cache()`

**Debugging:**
- Use `torch.autograd.set_detect_anomaly(True)`
- Check tensor shapes frequently
- Profile with `torch.profiler`

## Common Challenges

**CUDA Out of Memory:**
- Reduce batch size
- Use mixed precision training
- Apply gradient checkpointing

**Slow Training:**
- Use DataLoader with multiple workers
- Pin memory for GPU transfer
- Profile to identify bottlenecks

**Overfitting:**
- Add dropout and regularization
- Use data augmentation
- Implement early stopping

## Ecosystem Tools

- **torchvision**: Computer vision datasets and models
- **torchaudio**: Audio processing
- **torchtext**: NLP utilities
- **PyTorch Lightning**: High-level training framework
- **Hugging Face Transformers**: Pretrained NLP models
- **timm**: Image models library
- **Captum**: Model interpretability

## Learning Path

1. **Basics**: Tensors, autograd, nn.Module
2. **Computer Vision**: CNNs, transfer learning
3. **NLP**: RNNs, transformers, embeddings
4. **Advanced**: Custom layers, distributed training
5. **Optimization**: Quantization, pruning, TorchScript
6. **Deployment**: TorchServe, ONNX, mobile

See `references/` for advanced techniques, distributed training guides, and deployment strategies.

## Using the Reference Files

- [./references/distributed-training.md](./references/distributed-training.md): Distributed Training

## References

- [Distributed Training](references/distributed-training.md)
