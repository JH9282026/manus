---
name: tensorflow-deep-learning
description: "Build, train, and deploy deep learning models using TensorFlow. Use for: creating custom neural networks with Functional API, implementing CNNs for computer vision, building RNNs/LSTMs for NLP and time series, developing GANs and VAEs for generative AI, applying transfer learning and fine-tuning, distributed training across GPUs/TPUs, optimizing models with mixed precision and quantization, deploying with TensorFlow Serving/Lite, and leveraging TensorBoard for visualization and debugging."
---

# TensorFlow Deep Learning

Build, train, and deploy production-ready deep learning models using Google's TensorFlow framework.

## Overview

TensorFlow is an open-source deep learning framework developed by Google that provides a comprehensive ecosystem for building and deploying machine learning applications. It offers high-level APIs (Keras) for rapid prototyping, low-level APIs for custom implementations, distributed training capabilities, and robust deployment tools. TensorFlow excels in computer vision, natural language processing, time series analysis, and generative AI, with strong support for both research and production environments.

## Core TensorFlow Architecture

### Tensor Fundamentals

**Tensors** are multi-dimensional arrays that flow through computational graphs:

```python
import tensorflow as tf

# Creating tensors
scalar = tf.constant(42)
vector = tf.constant([1, 2, 3])
matrix = tf.constant([[1, 2], [3, 4]])
tensor_3d = tf.constant([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Tensor operations
a = tf.constant([[1, 2], [3, 4]])
b = tf.constant([[5, 6], [7, 8]])
matmul_result = tf.matmul(a, b)
element_wise = a + b
```

**Execution Modes:**
- **Eager Execution** (default): Operations execute immediately, Python-like debugging
- **Graph Mode** (`@tf.function`): Compiles to optimized computational graphs for performance

```python
@tf.function
def fast_computation(x):
    return tf.reduce_sum(x ** 2)

result = fast_computation(tf.constant([1.0, 2.0, 3.0]))
```

### Keras API Levels

**Sequential API** (simplest, linear models):
```python
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])
```

**Functional API** (complex architectures, multiple inputs/outputs):
```python
inputs = tf.keras.Input(shape=(784,))
x = tf.keras.layers.Dense(128, activation='relu')(inputs)
x = tf.keras.layers.Dropout(0.2)(x)
outputs = tf.keras.layers.Dense(10, activation='softmax')(x)
model = tf.keras.Model(inputs=inputs, outputs=outputs)
```

**Subclassing API** (maximum flexibility, custom training loops):
```python
class CustomModel(tf.keras.Model):
    def __init__(self):
        super().__init__()
        self.dense1 = tf.keras.layers.Dense(128, activation='relu')
        self.dropout = tf.keras.layers.Dropout(0.2)
        self.dense2 = tf.keras.layers.Dense(10, activation='softmax')
    
    def call(self, inputs, training=False):
        x = self.dense1(inputs)
        x = self.dropout(x, training=training)
        return self.dense2(x)
```

## Computer Vision with TensorFlow

### Convolutional Neural Networks (CNNs)

**Image Classification:**
```python
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(num_classes, activation='softmax')
])
```

**Transfer Learning with Pre-trained Models:**
```python
base_model = tf.keras.applications.ResNet50(
    weights='imagenet',
    include_top=False,
    input_shape=(224, 224, 3)
)
base_model.trainable = False  # Freeze base layers

model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(num_classes, activation='softmax')
])
```

**Object Detection:**
- Use TensorFlow Object Detection API
- Pre-trained models: SSD, Faster R-CNN, EfficientDet
- Custom training with COCO or custom datasets

**Image Segmentation:**
```python
# U-Net architecture for semantic segmentation
def unet_model(input_shape):
    inputs = tf.keras.Input(shape=input_shape)
    
    # Encoder
    c1 = tf.keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same')(inputs)
    c1 = tf.keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same')(c1)
    p1 = tf.keras.layers.MaxPooling2D((2, 2))(c1)
    
    # ... more encoder layers
    
    # Decoder with skip connections
    u1 = tf.keras.layers.UpSampling2D((2, 2))(bottleneck)
    u1 = tf.keras.layers.concatenate([u1, c1])
    c9 = tf.keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same')(u1)
    
    outputs = tf.keras.layers.Conv2D(num_classes, (1, 1), activation='softmax')(c9)
    return tf.keras.Model(inputs=inputs, outputs=outputs)
```

## Natural Language Processing

### Text Processing Pipeline

```python
# Tokenization and vectorization
tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=10000)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
padded = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=100)
```

### RNN/LSTM for Sequence Modeling

```python
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, 128, input_length=max_length),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64, return_sequences=True)),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(num_classes, activation='softmax')
])
```

### Transformer Models

```python
# Multi-head attention layer
class MultiHeadAttention(tf.keras.layers.Layer):
    def __init__(self, d_model, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.d_model = d_model
        self.depth = d_model // num_heads
        
        self.wq = tf.keras.layers.Dense(d_model)
        self.wk = tf.keras.layers.Dense(d_model)
        self.wv = tf.keras.layers.Dense(d_model)
        self.dense = tf.keras.layers.Dense(d_model)
    
    def call(self, q, k, v, mask=None):
        # Implementation of scaled dot-product attention
        # ... attention computation
        return output
```

## Generative Deep Learning

TensorFlow excels at generative models including Autoencoders (AE), Variational Autoencoders (VAE), and Generative Adversarial Networks (GANs). These models can denoise images, generate new data, and create realistic synthetic content. VAEs learn latent representations for generation, while GANs use adversarial training between generator and discriminator networks. See `references/generative-models.md` for complete implementations.

## Advanced Training Techniques

### Custom Training Loops with GradientTape

```python
@tf.function
def train_step(images, labels):
    with tf.GradientTape() as tape:
        predictions = model(images, training=True)
        loss = loss_fn(labels, predictions)
    
    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))
    
    train_accuracy.update_state(labels, predictions)
    return loss

for epoch in range(epochs):
    for images, labels in train_dataset:
        loss = train_step(images, labels)
```

### Mixed Precision Training

```python
# Enable mixed precision for faster training on modern GPUs
policy = tf.keras.mixed_precision.Policy('mixed_float16')
tf.keras.mixed_precision.set_global_policy(policy)

model = create_model()
optimizer = tf.keras.optimizers.Adam()
optimizer = tf.keras.mixed_precision.LossScaleOptimizer(optimizer)
```

### Learning Rate Schedules

```python
# Cosine decay with warmup
initial_learning_rate = 0.001
lr_schedule = tf.keras.optimizers.schedules.CosineDecay(
    initial_learning_rate,
    decay_steps=1000,
    alpha=0.0
)

# Reduce on plateau
reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(
    monitor='val_loss',
    factor=0.5,
    patience=5,
    min_lr=1e-7
)
```

## Distributed Training

### Multi-GPU Training

```python
strategy = tf.distribute.MirroredStrategy()
print(f'Number of devices: {strategy.num_replicas_in_sync}')

with strategy.scope():
    model = create_model()
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

model.fit(train_dataset, epochs=10, validation_data=val_dataset)
```

### TPU Training

```python
resolver = tf.distribute.cluster_resolver.TPUClusterResolver()
tf.config.experimental_connect_to_cluster(resolver)
tf.tpu.experimental.initialize_tpu_system(resolver)
strategy = tf.distribute.TPUStrategy(resolver)

with strategy.scope():
    model = create_model()
    model.compile(...)
```

## Model Optimization and Deployment

### Model Quantization

```python
# Post-training quantization
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()

# Quantization-aware training
model = tf.keras.models.load_model('model.h5')
quantize_model = tfmot.quantization.keras.quantize_model
q_aware_model = quantize_model(model)
q_aware_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
```

### Model Pruning

```python
import tensorflow_model_optimization as tfmot

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
```

### TensorFlow Serving

```python
# Save model for serving
tf.saved_model.save(model, 'saved_model/1')

# Deploy with Docker
# docker run -p 8501:8501 --mount type=bind,source=/path/to/saved_model,target=/models/my_model \
#   -e MODEL_NAME=my_model -t tensorflow/serving
```

### TensorFlow Lite (Mobile/Edge)

```python
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.target_spec.supported_types = [tf.float16]
tflite_model = converter.convert()

with open('model.tflite', 'wb') as f:
    f.write(tflite_model)
```

## Monitoring and Debugging

### TensorBoard Integration

```python
tensorboard_callback = tf.keras.callbacks.TensorBoard(
    log_dir='logs',
    histogram_freq=1,
    write_graph=True,
    write_images=True,
    update_freq='epoch',
    profile_batch='500,520'
)

model.fit(train_dataset, epochs=10, callbacks=[tensorboard_callback])

# Launch TensorBoard: tensorboard --logdir=logs
```

### Model Checkpointing

```python
checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath='checkpoints/model_{epoch:02d}_{val_loss:.2f}.h5',
    save_best_only=True,
    monitor='val_loss',
    mode='min',
    save_weights_only=False
)
```

## Best Practices

### Data Pipeline Optimization

```python
# Efficient data loading with tf.data
train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
train_dataset = train_dataset.shuffle(buffer_size=10000)
train_dataset = train_dataset.batch(batch_size)
train_dataset = train_dataset.prefetch(tf.data.AUTOTUNE)
train_dataset = train_dataset.cache()  # Cache in memory
```

### Regularization Techniques

- **Dropout**: Randomly drop neurons during training
- **L1/L2 Regularization**: Add penalty to loss function
- **Batch Normalization**: Normalize layer inputs
- **Data Augmentation**: Increase training data diversity
- **Early Stopping**: Stop training when validation loss plateaus

### Hyperparameter Tuning

```python
import keras_tuner as kt

def build_model(hp):
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(
        units=hp.Int('units', min_value=32, max_value=512, step=32),
        activation='relu'
    ))
    model.add(tf.keras.layers.Dense(10, activation='softmax'))
    
    model.compile(
        optimizer=tf.keras.optimizers.Adam(
            hp.Choice('learning_rate', values=[1e-2, 1e-3, 1e-4])
        ),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    return model

tuner = kt.Hyperband(build_model, objective='val_accuracy', max_epochs=10)
tuner.search(train_dataset, validation_data=val_dataset)
```

## Common Challenges and Solutions

**Overfitting:**
- Use dropout, regularization, and data augmentation
- Reduce model complexity
- Collect more training data
- Apply early stopping

**Vanishing/Exploding Gradients:**
- Use batch normalization
- Apply gradient clipping
- Use residual connections (ResNet)
- Choose appropriate activation functions (ReLU, LeakyReLU)

**Slow Training:**
- Enable mixed precision training
- Use distributed training strategies
- Optimize data pipeline with prefetching and caching
- Profile with TensorBoard to identify bottlenecks

**Memory Issues:**
- Reduce batch size
- Use gradient accumulation
- Apply model parallelism
- Enable memory growth for GPUs

## Ecosystem and Tools

- **TensorFlow Hub**: Pre-trained models and embeddings
- **TensorFlow Extended (TFX)**: Production ML pipelines
- **TensorFlow.js**: Browser and Node.js deployment
- **TensorFlow Probability**: Probabilistic reasoning and statistical analysis
- **TensorFlow Datasets**: Ready-to-use datasets
- **Keras Tuner**: Hyperparameter optimization
- **TensorFlow Model Optimization**: Quantization, pruning, clustering

## Learning Path

1. **Foundations**: Tensors, operations, basic neural networks
2. **Computer Vision**: CNNs, transfer learning, object detection
3. **NLP**: RNNs, LSTMs, Transformers, embeddings
4. **Advanced Architectures**: GANs, VAEs, attention mechanisms
5. **Optimization**: Custom training loops, distributed training
6. **Deployment**: TensorFlow Serving, TFLite, optimization techniques
7. **Production**: TFX pipelines, monitoring, versioning

See `references/` for detailed guides on advanced techniques, architecture patterns, and deployment strategies.

## Using the Reference Files

- [./references/advanced-architectures.md](./references/advanced-architectures.md): Advanced Architectures
- [./references/generative-models.md](./references/generative-models.md): Generative Models

## References

- [Advanced Architectures](references/advanced-architectures.md)
- [Generative Models](references/generative-models.md)
