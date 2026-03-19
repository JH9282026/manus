# Keras Model Deployment and Production

## Overview

Deploying Keras models to production involves converting trained models into formats suitable for inference, optimizing for performance and size, and integrating with production systems. This guide covers model saving/loading, optimization techniques, deployment strategies, and best practices for production environments.

## Model Saving and Loading

### Keras Native Format (.keras)

**Recommended Format**: The `.keras` format is the modern, recommended way to save Keras models.

#### Saving Models

```python
# Save entire model (architecture + weights + optimizer state)
model.save('my_model.keras')

# Or specify format explicitly
model.save('my_model.keras', save_format='keras')
```

**What's Saved**:
- Model architecture
- Model weights
- Optimizer state
- Training configuration (loss, metrics)
- Custom objects (if registered)

#### Loading Models

```python
import keras

# Load entire model
loaded_model = keras.models.load_model('my_model.keras')

# Model is ready for inference or continued training
predictions = loaded_model.predict(new_data)
```

#### Loading with Custom Objects

```python
# Define custom objects
class CustomLayer(keras.layers.Layer):
    # ... layer implementation
    pass

def custom_loss(y_true, y_pred):
    # ... loss implementation
    return loss

# Load with custom objects
loaded_model = keras.models.load_model(
    'my_model.keras',
    custom_objects={'CustomLayer': CustomLayer, 'custom_loss': custom_loss}
)
```

### Legacy Formats

#### HDF5 Format (.h5)

**Legacy Format**: Still supported but `.keras` is preferred.

```python
# Save
model.save('my_model.h5')

# Load
loaded_model = keras.models.load_model('my_model.h5')
```

#### SavedModel Format (TensorFlow)

**TensorFlow's Format**: For TensorFlow Serving and TensorFlow Lite.

```python
# Save
model.save('saved_model_dir', save_format='tf')

# Load
loaded_model = keras.models.load_model('saved_model_dir')
```

### Saving Weights Only

**Use Case**: When you want to save only weights, not architecture.

```python
# Save weights
model.save_weights('model_weights.weights.h5')

# Load weights (model architecture must be defined first)
model = create_model()  # Define architecture
model.load_weights('model_weights.weights.h5')
```

**Benefits**:
- Smaller file size
- Faster save/load
- Useful for transfer learning

**Limitations**:
- Must recreate architecture manually
- Optimizer state not saved

### Saving Architecture Only

```python
# Save architecture as JSON
architecture_json = model.to_json()
with open('model_architecture.json', 'w') as f:
    f.write(architecture_json)

# Load architecture
from keras.models import model_from_json
with open('model_architecture.json', 'r') as f:
    architecture_json = f.read()
model = model_from_json(architecture_json)
```

## Model Optimization for Deployment

### 1. Pruning

**Purpose**: Remove weights that contribute minimally to model output.

**Benefits**:
- Reduce model size (up to 3x smaller)
- Faster inference
- Lower memory footprint
- Minimal accuracy loss

#### Implementation with TensorFlow Model Optimization Toolkit

```python
import tensorflow_model_optimization as tfmot

# Define pruning schedule
pruning_schedule = tfmot.sparsity.keras.PolynomialDecay(
    initial_sparsity=0.0,
    final_sparsity=0.5,      # 50% of weights will be zero
    begin_step=2000,
    end_step=4000
)

# Apply pruning to model
model_for_pruning = tfmot.sparsity.keras.prune_low_magnitude(
    model,
    pruning_schedule=pruning_schedule
)

# Compile and train
model_for_pruning.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Add pruning callback
callbacks = [
    tfmot.sparsity.keras.UpdatePruningStep()
]

model_for_pruning.fit(
    x_train, y_train,
    epochs=10,
    callbacks=callbacks
)

# Remove pruning wrappers for export
model_for_export = tfmot.sparsity.keras.strip_pruning(model_for_pruning)
```

#### Pruning Best Practices

- Start with low sparsity (20-30%)
- Gradually increase to 50-70%
- Fine-tune after pruning
- Monitor accuracy during pruning
- Use structured pruning for hardware acceleration

### 2. Quantization

**Purpose**: Reduce precision of weights and activations.

**Benefits**:
- Smaller model size (up to 4x)
- Faster inference on supported hardware
- Lower memory usage
- Reduced power consumption

#### Post-Training Quantization

**Dynamic Range Quantization**:
```python
import tensorflow as tf

# Convert to TFLite with quantization
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()

# Save quantized model
with open('model_quantized.tflite', 'wb') as f:
    f.write(tflite_model)
```

**Full Integer Quantization**:
```python
def representative_dataset():
    for i in range(100):
        yield [x_train[i:i+1].astype('float32')]

converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.representative_dataset = representative_dataset
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter.inference_input_type = tf.int8
converter.inference_output_type = tf.int8

tflite_model = converter.convert()
```

#### Quantization-Aware Training

**Purpose**: Train model to be robust to quantization.

```python
import tensorflow_model_optimization as tfmot

# Apply quantization-aware training
quantize_model = tfmot.quantization.keras.quantize_model

q_aware_model = quantize_model(model)

# Compile and train
q_aware_model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

q_aware_model.fit(x_train, y_train, epochs=10)

# Convert to TFLite
converter = tf.lite.TFLiteConverter.from_keras_model(q_aware_model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()
```

### 3. Weight Clustering

**Purpose**: Group similar weights and share cluster centroids.

```python
import tensorflow_model_optimization as tfmot

# Apply weight clustering
cluster_weights = tfmot.clustering.keras.cluster_weights
CentroidInitialization = tfmot.clustering.keras.CentroidInitialization

clustering_params = {
    'number_of_clusters': 16,
    'cluster_centroids_init': CentroidInitialization.LINEAR
}

clustered_model = cluster_weights(model, **clustering_params)

# Compile and fine-tune
clustered_model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

clustered_model.fit(x_train, y_train, epochs=5)

# Strip clustering wrappers
final_model = tfmot.clustering.keras.strip_clustering(clustered_model)
```

### 4. Combining Optimization Techniques

**Pruning + Quantization**:

```python
# 1. Prune model
model_for_pruning = tfmot.sparsity.keras.prune_low_magnitude(model, pruning_schedule)
model_for_pruning.fit(x_train, y_train, epochs=10, callbacks=[pruning_callback])
pruned_model = tfmot.sparsity.keras.strip_pruning(model_for_pruning)

# 2. Apply quantization-aware training
q_aware_model = tfmot.quantization.keras.quantize_model(pruned_model)
q_aware_model.fit(x_train, y_train, epochs=5)

# 3. Convert to TFLite with quantization
converter = tf.lite.TFLiteConverter.from_keras_model(q_aware_model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()

# Result: Up to 10x smaller model
```

## Deployment Strategies

### 1. TensorFlow Serving

**Purpose**: Production-ready serving system for TensorFlow models.

#### Exporting for TensorFlow Serving

```python
import tensorflow as tf

# Save in SavedModel format
model.save('saved_model/1', save_format='tf')

# Directory structure:
# saved_model/
#   1/
#     assets/
#     variables/
#     saved_model.pb
```

#### Running TensorFlow Serving

```bash
# Using Docker
docker run -p 8501:8501 \
  --mount type=bind,source=/path/to/saved_model,target=/models/my_model \
  -e MODEL_NAME=my_model \
  -t tensorflow/serving
```

#### Making Predictions

```python
import requests
import json

# Prepare data
data = json.dumps({
    "signature_name": "serving_default",
    "instances": x_test[:5].tolist()
})

# Make request
headers = {"content-type": "application/json"}
response = requests.post(
    'http://localhost:8501/v1/models/my_model:predict',
    data=data,
    headers=headers
)

predictions = response.json()['predictions']
```

### 2. TensorFlow Lite (Mobile/Edge)

**Purpose**: Deploy on mobile and edge devices.

#### Converting to TFLite

```python
import tensorflow as tf

# Convert model
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()

# Save
with open('model.tflite', 'wb') as f:
    f.write(tflite_model)
```

#### Running Inference (Python)

```python
import numpy as np
import tensorflow as tf

# Load TFLite model
interpreter = tf.lite.Interpreter(model_path='model.tflite')
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Prepare input
input_data = np.array(x_test[0:1], dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], input_data)

# Run inference
interpreter.invoke()

# Get output
output_data = interpreter.get_tensor(output_details[0]['index'])
print(output_data)
```

### 3. ONNX (Cross-Framework)

**Purpose**: Deploy across different frameworks and platforms.

#### Converting to ONNX

```python
import tf2onnx
import onnx

# Convert Keras model to ONNX
onnx_model, _ = tf2onnx.convert.from_keras(
    model,
    input_signature=[tf.TensorSpec(shape=(None, 28, 28, 1), dtype=tf.float32)],
    opset=13
)

# Save ONNX model
onnx.save(onnx_model, 'model.onnx')
```

#### Running Inference with ONNX Runtime

```python
import onnxruntime as ort
import numpy as np

# Load ONNX model
session = ort.InferenceSession('model.onnx')

# Get input name
input_name = session.get_inputs()[0].name

# Run inference
result = session.run(None, {input_name: x_test[0:1].astype('float32')})
print(result[0])
```

### 4. Web Deployment (TensorFlow.js)

**Purpose**: Run models in web browsers.

#### Converting to TensorFlow.js

```bash
# Install tensorflowjs converter
pip install tensorflowjs

# Convert model
tensorflowjs_converter \
  --input_format=keras \
  my_model.keras \
  tfjs_model/
```

#### Loading in Browser

```javascript
// Load model
const model = await tf.loadLayersModel('tfjs_model/model.json');

// Prepare input
const input = tf.tensor2d([[...inputData]]);

// Make prediction
const prediction = model.predict(input);
prediction.print();
```

### 5. Cloud Deployment

#### AWS SageMaker

```python
import sagemaker
from sagemaker.tensorflow import TensorFlowModel

# Create SageMaker model
model = TensorFlowModel(
    model_data='s3://bucket/model.tar.gz',
    role=role,
    framework_version='2.12'
)

# Deploy
predictor = model.deploy(
    initial_instance_count=1,
    instance_type='ml.m5.large'
)

# Make predictions
result = predictor.predict(data)
```

#### Google Cloud AI Platform

```bash
# Upload model to Cloud Storage
gsutil cp -r saved_model gs://bucket/models/my_model/

# Create model version
gcloud ai-platform versions create v1 \
  --model=my_model \
  --origin=gs://bucket/models/my_model/ \
  --runtime-version=2.12 \
  --framework=tensorflow \
  --python-version=3.9
```

#### Azure ML

```python
from azureml.core import Workspace, Model
from azureml.core.webservice import AciWebservice, Webservice

# Register model
model = Model.register(
    workspace=ws,
    model_path='my_model.keras',
    model_name='my_model'
)

# Deploy
deployment_config = AciWebservice.deploy_configuration(
    cpu_cores=1,
    memory_gb=1
)

service = Model.deploy(
    workspace=ws,
    name='my-model-service',
    models=[model],
    deployment_config=deployment_config
)
```

## Production Best Practices

### 1. Model Versioning

```python
import datetime

# Include version in filename
version = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
model.save(f'models/my_model_v{version}.keras')

# Or use semantic versioning
model.save('models/my_model_v1.2.3.keras')
```

### 2. Input Validation

```python
def validate_input(data):
    # Check shape
    if data.shape[1:] != expected_shape:
        raise ValueError(f"Expected shape {expected_shape}, got {data.shape[1:]}")
    
    # Check data type
    if data.dtype != np.float32:
        data = data.astype(np.float32)
    
    # Check value range
    if data.min() < 0 or data.max() > 1:
        raise ValueError("Input values must be in range [0, 1]")
    
    return data

# Use in prediction
def predict(data):
    validated_data = validate_input(data)
    return model.predict(validated_data)
```

### 3. Batch Prediction

```python
def batch_predict(data, batch_size=32):
    predictions = []
    for i in range(0, len(data), batch_size):
        batch = data[i:i+batch_size]
        batch_predictions = model.predict(batch, verbose=0)
        predictions.append(batch_predictions)
    return np.concatenate(predictions)
```

### 4. Monitoring and Logging

```python
import logging
import time

logger = logging.getLogger(__name__)

def predict_with_logging(data):
    start_time = time.time()
    
    try:
        predictions = model.predict(data)
        inference_time = time.time() - start_time
        
        logger.info(f"Prediction successful. Time: {inference_time:.3f}s, Batch size: {len(data)}")
        return predictions
    
    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}")
        raise
```

### 5. A/B Testing

```python
import random

class ModelABTest:
    def __init__(self, model_a, model_b, traffic_split=0.5):
        self.model_a = model_a
        self.model_b = model_b
        self.traffic_split = traffic_split
    
    def predict(self, data):
        if random.random() < self.traffic_split:
            model_used = 'A'
            predictions = self.model_a.predict(data)
        else:
            model_used = 'B'
            predictions = self.model_b.predict(data)
        
        # Log which model was used
        logger.info(f"Model {model_used} used for prediction")
        return predictions
```

### 6. Caching

```python
from functools import lru_cache
import hashlib

class CachedPredictor:
    def __init__(self, model, cache_size=1000):
        self.model = model
        self.cache = {}
        self.cache_size = cache_size
    
    def _hash_input(self, data):
        return hashlib.md5(data.tobytes()).hexdigest()
    
    def predict(self, data):
        input_hash = self._hash_input(data)
        
        if input_hash in self.cache:
            logger.info("Cache hit")
            return self.cache[input_hash]
        
        predictions = self.model.predict(data)
        
        if len(self.cache) >= self.cache_size:
            # Remove oldest entry
            self.cache.pop(next(iter(self.cache)))
        
        self.cache[input_hash] = predictions
        return predictions
```

## Performance Optimization

### 1. Mixed Precision Inference

```python
from keras import mixed_precision

# Enable mixed precision
policy = mixed_precision.Policy('mixed_float16')
mixed_precision.set_global_policy(policy)

# Load or build model
model = keras.models.load_model('my_model.keras')

# Inference will use float16 where possible
predictions = model.predict(data)
```

### 2. GPU Optimization

```python
import tensorflow as tf

# Configure GPU memory growth
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)

# Or set memory limit
tf.config.set_logical_device_configuration(
    gpus[0],
    [tf.config.LogicalDeviceConfiguration(memory_limit=4096)]  # 4GB
)
```

### 3. Multi-Threading

```python
import tensorflow as tf

# Configure threading
tf.config.threading.set_inter_op_parallelism_threads(4)
tf.config.threading.set_intra_op_parallelism_threads(4)
```

## Key Takeaways

1. **Save Format**: Use `.keras` format for modern Keras models
2. **Optimization**: Apply pruning and quantization for smaller, faster models
3. **TensorFlow Serving**: Production-ready serving for scalable deployments
4. **TFLite**: Optimize for mobile and edge devices
5. **ONNX**: Cross-framework compatibility
6. **Versioning**: Always version models in production
7. **Validation**: Validate inputs before inference
8. **Monitoring**: Log predictions and performance metrics
9. **Batch Prediction**: Process multiple samples efficiently
10. **Cloud Deployment**: Leverage cloud platforms for scalability

## References

- Keras Saving Guide: https://keras.io/guides/serialization_and_saving/
- TensorFlow Model Optimization: https://www.tensorflow.org/model_optimization
- TensorFlow Serving: https://www.tensorflow.org/tfx/guide/serving
- TensorFlow Lite: https://www.tensorflow.org/lite
- ONNX: https://onnx.ai/
- TensorFlow.js: https://www.tensorflow.org/js
