---
name: model-optimization
description: "Optimize deep learning models for deployment and inference. Use for: quantizing models to reduce size and latency, pruning unnecessary weights and connections, applying knowledge distillation to compress models, implementing neural architecture search (NAS), optimizing inference with TensorRT and ONNX Runtime, reducing memory footprint with mixed precision, accelerating models with hardware-specific optimizations, and balancing accuracy-efficiency tradeoffs for edge deployment."
---

# Model Optimization

Optimize deep learning models for efficient deployment while maintaining performance.

## Overview

Model optimization reduces computational requirements, memory footprint, and inference latency of deep learning models without significantly sacrificing accuracy. This is crucial for deploying models on resource-constrained devices (mobile, edge, IoT) and reducing cloud infrastructure costs. Key techniques include quantization, pruning, knowledge distillation, and neural architecture search.

## Quantization

Quantization reduces numerical precision of model weights and activations from floating-point to lower bit-width representations.

### Post-Training Quantization (PTQ)

```python
import tensorflow as tf

# TensorFlow Lite quantization
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
quantized_tflite_model = converter.convert()

# With representative dataset for better accuracy
def representative_dataset():
    for data in calibration_dataset.take(100):
        yield [data]

converter.representative_dataset = representative_dataset
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter.inference_input_type = tf.int8
converter.inference_output_type = tf.int8
quantized_model = converter.convert()
```

```python
# PyTorch quantization
import torch
from torch.quantization import quantize_dynamic, quantize_static, prepare, convert

# Dynamic quantization (weights only)
quantized_model = quantize_dynamic(
    model, {torch.nn.Linear, torch.nn.LSTM}, dtype=torch.qint8
)

# Static quantization (weights and activations)
model.qconfig = torch.quantization.get_default_qconfig('fbgemm')
model_prepared = prepare(model, inplace=False)

# Calibrate with representative data
with torch.no_grad():
    for data, _ in calibration_loader:
        model_prepared(data)

model_quantized = convert(model_prepared, inplace=False)
```

### Quantization-Aware Training (QAT)

```python
import tensorflow_model_optimization as tfmot

# TensorFlow QAT
quantize_model = tfmot.quantization.keras.quantize_model
q_aware_model = quantize_model(model)

q_aware_model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

q_aware_model.fit(train_dataset, epochs=10, validation_data=val_dataset)

# Convert to TFLite
converter = tf.lite.TFLiteConverter.from_keras_model(q_aware_model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
quantized_tflite_model = converter.convert()
```

```python
# PyTorch QAT
import torch.quantization as quant

model.qconfig = quant.get_default_qat_qconfig('fbgemm')
model_prepared = quant.prepare_qat(model, inplace=False)

# Train with quantization simulation
for epoch in range(num_epochs):
    train_one_epoch(model_prepared, train_loader, optimizer)

model_quantized = quant.convert(model_prepared, inplace=False)
```

### Mixed Precision Quantization

```python
# Different precision for different layers
def mixed_precision_quantization(model):
    # Sensitive layers: keep FP16
    sensitive_layers = ['attention', 'layer_norm']
    
    # Less sensitive layers: INT8
    for name, module in model.named_modules():
        if any(s in name for s in sensitive_layers):
            module.qconfig = None  # Skip quantization
        else:
            module.qconfig = torch.quantization.get_default_qconfig('fbgemm')
    
    return model
```

## Pruning

Pruning removes unnecessary weights, neurons, or entire layers to reduce model size and computation.

### Magnitude-Based Pruning

```python
import tensorflow_model_optimization as tfmot

# TensorFlow pruning
prune_low_magnitude = tfmot.sparsity.keras.prune_low_magnitude

pruning_params = {
    'pruning_schedule': tfmot.sparsity.keras.PolynomialDecay(
        initial_sparsity=0.0,
        final_sparsity=0.5,
        begin_step=0,
        end_step=1000
    )
}

model_for_pruning = prune_low_magnitude(model, **pruning_params)

model_for_pruning.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

callbacks = [tfmot.sparsity.keras.UpdatePruningStep()]
model_for_pruning.fit(train_dataset, epochs=10, callbacks=callbacks)

# Strip pruning wrappers
model_pruned = tfmot.sparsity.keras.strip_pruning(model_for_pruning)
```

```python
# PyTorch pruning
import torch.nn.utils.prune as prune

# Unstructured pruning (individual weights)
prune.l1_unstructured(model.conv1, name='weight', amount=0.3)
prune.l1_unstructured(model.fc1, name='weight', amount=0.4)

# Structured pruning (entire channels/filters)
prune.ln_structured(model.conv2, name='weight', amount=0.5, n=2, dim=0)

# Global pruning across multiple layers
parameters_to_prune = [
    (model.conv1, 'weight'),
    (model.conv2, 'weight'),
    (model.fc1, 'weight'),
]

prune.global_unstructured(
    parameters_to_prune,
    pruning_method=prune.L1Unstructured,
    amount=0.2
)

# Make pruning permanent
for module, param in parameters_to_prune:
    prune.remove(module, param)
```

### Iterative Pruning

```python
def iterative_pruning(model, train_loader, val_loader, target_sparsity=0.9):
    sparsity_levels = np.linspace(0, target_sparsity, 10)
    
    for sparsity in sparsity_levels:
        # Prune model
        for name, module in model.named_modules():
            if isinstance(module, torch.nn.Conv2d) or isinstance(module, torch.nn.Linear):
                prune.l1_unstructured(module, name='weight', amount=sparsity)
        
        # Fine-tune
        fine_tune(model, train_loader, epochs=5)
        
        # Evaluate
        accuracy = evaluate(model, val_loader)
        print(f"Sparsity: {sparsity:.2f}, Accuracy: {accuracy:.4f}")
        
        if accuracy < baseline_accuracy * 0.95:
            print("Accuracy dropped too much, stopping pruning")
            break
    
    return model
```

## Knowledge Distillation

Transfer knowledge from a large "teacher" model to a smaller "student" model.

```python
import torch.nn.functional as F

class DistillationLoss(nn.Module):
    def __init__(self, temperature=3.0, alpha=0.5):
        super().__init__()
        self.temperature = temperature
        self.alpha = alpha
    
    def forward(self, student_logits, teacher_logits, labels):
        # Soft targets from teacher
        soft_targets = F.softmax(teacher_logits / self.temperature, dim=1)
        soft_predictions = F.log_softmax(student_logits / self.temperature, dim=1)
        
        # Distillation loss
        distillation_loss = F.kl_div(
            soft_predictions, soft_targets, reduction='batchmean'
        ) * (self.temperature ** 2)
        
        # Student loss
        student_loss = F.cross_entropy(student_logits, labels)
        
        # Combined loss
        return self.alpha * distillation_loss + (1 - self.alpha) * student_loss

def train_with_distillation(student, teacher, train_loader, epochs=10):
    teacher.eval()
    student.train()
    
    criterion = DistillationLoss(temperature=3.0, alpha=0.7)
    optimizer = torch.optim.Adam(student.parameters(), lr=0.001)
    
    for epoch in range(epochs):
        for data, labels in train_loader:
            optimizer.zero_grad()
            
            with torch.no_grad():
                teacher_logits = teacher(data)
            
            student_logits = student(data)
            loss = criterion(student_logits, teacher_logits, labels)
            
            loss.backward()
            optimizer.step()
```

## Neural Architecture Search (NAS)

Automatically discover efficient architectures.

```python
# Example: Simple NAS with random search
class SearchSpace:
    def __init__(self):
        self.layer_types = ['conv', 'depthwise_conv', 'identity']
        self.kernel_sizes = [3, 5, 7]
        self.num_filters = [32, 64, 128]
    
    def sample_architecture(self, num_layers=5):
        architecture = []
        for _ in range(num_layers):
            layer = {
                'type': np.random.choice(self.layer_types),
                'kernel_size': np.random.choice(self.kernel_sizes),
                'filters': np.random.choice(self.num_filters)
            }
            architecture.append(layer)
        return architecture

def build_model_from_architecture(architecture):
    model = nn.Sequential()
    for i, layer_config in enumerate(architecture):
        if layer_config['type'] == 'conv':
            model.add_module(f'conv_{i}', nn.Conv2d(
                in_channels=prev_channels,
                out_channels=layer_config['filters'],
                kernel_size=layer_config['kernel_size'],
                padding='same'
            ))
        # ... other layer types
    return model

def nas_search(search_space, train_loader, val_loader, num_trials=100):
    best_accuracy = 0
    best_architecture = None
    
    for trial in range(num_trials):
        architecture = search_space.sample_architecture()
        model = build_model_from_architecture(architecture)
        
        # Train briefly
        train(model, train_loader, epochs=5)
        
        # Evaluate
        accuracy = evaluate(model, val_loader)
        
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_architecture = architecture
    
    return best_architecture, best_accuracy
```

## Inference Optimization

### TensorRT Optimization

```python
import tensorrt as trt

# Convert ONNX to TensorRT
def build_engine(onnx_file_path, engine_file_path):
    logger = trt.Logger(trt.Logger.WARNING)
    builder = trt.Builder(logger)
    network = builder.create_network(1 << int(trt.NetworkDefinitionCreationFlag.EXPLICIT_BATCH))
    parser = trt.OnnxParser(network, logger)
    
    with open(onnx_file_path, 'rb') as model:
        parser.parse(model.read())
    
    config = builder.create_builder_config()
    config.max_workspace_size = 1 << 30  # 1GB
    config.set_flag(trt.BuilderFlag.FP16)  # Enable FP16
    
    engine = builder.build_engine(network, config)
    
    with open(engine_file_path, 'wb') as f:
        f.write(engine.serialize())
    
    return engine
```

### ONNX Runtime Optimization

```python
import onnxruntime as ort

# Optimize ONNX model
session_options = ort.SessionOptions()
session_options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
session_options.intra_op_num_threads = 4

# Enable optimizations
session = ort.InferenceSession(
    'model.onnx',
    sess_options=session_options,
    providers=['CUDAExecutionProvider', 'CPUExecutionProvider']
)

# Run inference
outputs = session.run(None, {'input': input_data})
```

### Model Compilation

```python
# PyTorch 2.0 torch.compile
import torch

model = MyModel()
compiled_model = torch.compile(model, mode='reduce-overhead')

# Inference
with torch.no_grad():
    output = compiled_model(input_tensor)
```

## Hardware-Specific Optimizations

### Mobile Optimization

```python
# TensorFlow Lite with GPU delegate
import tensorflow as tf

interpreter = tf.lite.Interpreter(
    model_path='model.tflite',
    experimental_delegates=[tf.lite.experimental.load_delegate('libgpu_delegate.so')]
)
interpreter.allocate_tensors()

# PyTorch Mobile
import torch.utils.mobile_optimizer as mobile_optimizer

model.eval()
scripted_model = torch.jit.script(model)
optimized_model = mobile_optimizer.optimize_for_mobile(scripted_model)
optimized_model._save_for_lite_interpreter('model_mobile.ptl')
```

### Edge TPU Optimization

```python
# Compile for Edge TPU
# edgetpu_compiler model_quant.tflite

# Run on Edge TPU
from pycoral.utils import edgetpu
from pycoral.adapters import common

interpreter = edgetpu.make_interpreter('model_edgetpu.tflite')
interpreter.allocate_tensors()

common.set_input(interpreter, input_data)
interpreter.invoke()
output = common.output_tensor(interpreter, 0)
```

## Benchmarking and Profiling

```python
import time
import numpy as np

def benchmark_model(model, input_shape, num_runs=100):
    model.eval()
    dummy_input = torch.randn(input_shape)
    
    # Warmup
    for _ in range(10):
        _ = model(dummy_input)
    
    # Benchmark
    times = []
    with torch.no_grad():
        for _ in range(num_runs):
            start = time.time()
            _ = model(dummy_input)
            torch.cuda.synchronize()  # For GPU
            times.append(time.time() - start)
    
    return {
        'mean_latency': np.mean(times) * 1000,  # ms
        'std_latency': np.std(times) * 1000,
        'throughput': 1.0 / np.mean(times)  # samples/sec
    }

def profile_model(model, input_data):
    with torch.profiler.profile(
        activities=[
            torch.profiler.ProfilerActivity.CPU,
            torch.profiler.ProfilerActivity.CUDA
        ],
        record_shapes=True
    ) as prof:
        model(input_data)
    
    print(prof.key_averages().table(sort_by="cuda_time_total", row_limit=10))
```

## Best Practices

**Quantization:**
- Use QAT for accuracy-critical applications
- PTQ for quick deployment
- Calibrate with representative data
- Test on target hardware

**Pruning:**
- Start with unstructured, move to structured
- Use iterative pruning with fine-tuning
- Monitor accuracy degradation
- Combine with quantization for maximum compression

**Knowledge Distillation:**
- Use temperature scaling (3-5 typical)
- Balance distillation and student loss
- Consider intermediate layer distillation
- Experiment with different teacher-student architectures


## Learning Path

1. **Basics**: Quantization fundamentals, simple pruning
2. **Intermediate**: QAT, structured pruning, knowledge distillation
3. **Advanced**: NAS, hardware-specific optimization
4. **Expert**: Custom optimization techniques

See `references/` for detailed optimization recipes, hardware-specific guides, and benchmarking tools.

## Using the Reference Files

- [./references/01_pruning_quantization_fundamentals.md](./references/01_pruning_quantization_fundamentals.md): 01 Pruning Quantization Fundamentals
- [./references/02_inference_optimization_techniques.md](./references/02_inference_optimization_techniques.md): 02 Inference Optimization Techniques
- [./references/03_knowledge_distillation_compression.md](./references/03_knowledge_distillation_compression.md): 03 Knowledge Distillation Compression
- [./references/04_deployment_best_practices.md](./references/04_deployment_best_practices.md): 04 Deployment Best Practices
- [./references/05_neural_architecture_optimization.md](./references/05_neural_architecture_optimization.md): 05 Neural Architecture Optimization
