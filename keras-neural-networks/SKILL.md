---
name: keras-neural-networks
description: "Build neural networks using Keras high-level API. Use for: rapid prototyping with Sequential and Functional APIs, creating CNNs for image classification, building RNNs for sequence modeling, implementing transfer learning with pretrained models, custom layers and loss functions, model subclassing for complex architectures, callbacks for training control, hyperparameter tuning with Keras Tuner, and seamless integration with TensorFlow ecosystem."
---

# Keras Neural Networks

Build neural networks rapidly using Keras' intuitive high-level API.

## Overview

Keras is a high-level neural networks API that runs on top of TensorFlow, providing an intuitive interface for building and training deep learning models. It emphasizes user-friendliness, modularity, and extensibility, making it ideal for rapid prototyping and production deployment. Keras supports both Sequential and Functional APIs, custom layers, and seamless integration with the TensorFlow ecosystem.

## Sequential API

The Sequential API is the simplest way to build models with a linear stack of layers.

```python
from tensorflow import keras
from tensorflow.keras import layers

# Create model
model = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=(784,)),
    layers.Dropout(0.2),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(10, activation='softmax')
])

# Compile
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train
history = model.fit(x_train, y_train, epochs=10, validation_split=0.2, batch_size=32)
```

**When to use Sequential:**
- Linear stack of layers
- Single input and output
- No layer sharing or branching
- Simple feedforward networks

## Functional API

The Functional API provides flexibility for complex architectures.

```python
# Multi-input model
input_a = keras.Input(shape=(32,), name='input_a')
input_b = keras.Input(shape=(64,), name='input_b')

x = layers.Dense(64, activation='relu')(input_a)
y = layers.Dense(64, activation='relu')(input_b)

# Concatenate
combined = layers.concatenate([x, y])
z = layers.Dense(32, activation='relu')(combined)
output = layers.Dense(10, activation='softmax')(z)

model = keras.Model(inputs=[input_a, input_b], outputs=output)
```

**When to use Functional:**
- Multiple inputs or outputs
- Shared layers
- Non-linear topology (residual connections, branching)
- Complex architectures (Inception, ResNet)

## Model Subclassing

For maximum flexibility, subclass `keras.Model`.

```python
class CustomModel(keras.Model):
    def __init__(self, num_classes=10):
        super().__init__()
        self.dense1 = layers.Dense(64, activation='relu')
        self.dense2 = layers.Dense(32, activation='relu')
        self.dropout = layers.Dropout(0.5)
        self.classifier = layers.Dense(num_classes, activation='softmax')
    
    def call(self, inputs, training=False):
        x = self.dense1(inputs)
        x = self.dropout(x, training=training)
        x = self.dense2(x)
        return self.classifier(x)

model = CustomModel()
```

## Computer Vision with Keras

### CNN for Image Classification

```python
model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax')
])
```

### Transfer Learning

```python
# Load pretrained model
base_model = keras.applications.MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights='imagenet'
)
base_model.trainable = False

# Add custom head
model = keras.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(num_classes, activation='softmax')
])

# Fine-tune later
base_model.trainable = True
for layer in base_model.layers[:-20]:
    layer.trainable = False
```

### Data Augmentation

```python
data_augmentation = keras.Sequential([
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.1),
    layers.RandomZoom(0.1),
    layers.RandomContrast(0.1)
])

model = keras.Sequential([
    data_augmentation,
    # ... rest of model
])
```

## Natural Language Processing

### Text Classification with Embeddings

```python
model = keras.Sequential([
    layers.Embedding(vocab_size, 128, input_length=max_length),
    layers.Bidirectional(layers.LSTM(64, return_sequences=True)),
    layers.Bidirectional(layers.LSTM(32)),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(num_classes, activation='softmax')
])
```

### Attention Mechanism

```python
class AttentionLayer(layers.Layer):
    def __init__(self, units):
        super().__init__()
        self.W = layers.Dense(units)
        self.V = layers.Dense(1)
    
    def call(self, features):
        score = tf.nn.tanh(self.W(features))
        attention_weights = tf.nn.softmax(self.V(score), axis=1)
        context_vector = attention_weights * features
        context_vector = tf.reduce_sum(context_vector, axis=1)
        return context_vector
```

## Custom Layers

```python
class CustomDense(layers.Layer):
    def __init__(self, units=32):
        super().__init__()
        self.units = units
    
    def build(self, input_shape):
        self.w = self.add_weight(
            shape=(input_shape[-1], self.units),
            initializer='random_normal',
            trainable=True
        )
        self.b = self.add_weight(
            shape=(self.units,),
            initializer='zeros',
            trainable=True
        )
    
    def call(self, inputs):
        return tf.matmul(inputs, self.w) + self.b
```

## Custom Loss Functions

```python
def custom_loss(y_true, y_pred):
    mse = tf.reduce_mean(tf.square(y_true - y_pred))
    mae = tf.reduce_mean(tf.abs(y_true - y_pred))
    return mse + 0.5 * mae

model.compile(optimizer='adam', loss=custom_loss)
```

## Callbacks

```python
# Early stopping
early_stop = keras.callbacks.EarlyStopping(
    monitor='val_loss',
    patience=5,
    restore_best_weights=True
)

# Model checkpoint
checkpoint = keras.callbacks.ModelCheckpoint(
    'best_model.h5',
    monitor='val_accuracy',
    save_best_only=True
)

# Learning rate reduction
reduce_lr = keras.callbacks.ReduceLROnPlateau(
    monitor='val_loss',
    factor=0.5,
    patience=3,
    min_lr=1e-7
)

# TensorBoard
tensorboard = keras.callbacks.TensorBoard(log_dir='logs')

# Custom callback
class CustomCallback(keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
        if logs.get('accuracy') > 0.95:
            print(f"\nReached 95% accuracy, stopping training!")
            self.model.stop_training = True

# Use callbacks
history = model.fit(
    x_train, y_train,
    epochs=50,
    validation_data=(x_val, y_val),
    callbacks=[early_stop, checkpoint, reduce_lr, tensorboard]
)
```

## Hyperparameter Tuning

```python
import keras_tuner as kt

def build_model(hp):
    model = keras.Sequential()
    
    # Tune number of layers
    for i in range(hp.Int('num_layers', 1, 3)):
        model.add(layers.Dense(
            units=hp.Int(f'units_{i}', min_value=32, max_value=512, step=32),
            activation='relu'
        ))
        model.add(layers.Dropout(hp.Float(f'dropout_{i}', 0, 0.5, step=0.1)))
    
    model.add(layers.Dense(10, activation='softmax'))
    
    # Tune learning rate
    model.compile(
        optimizer=keras.optimizers.Adam(
            hp.Choice('learning_rate', values=[1e-2, 1e-3, 1e-4])
        ),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    return model

tuner = kt.Hyperband(
    build_model,
    objective='val_accuracy',
    max_epochs=10,
    factor=3,
    directory='tuner_results'
)

tuner.search(x_train, y_train, epochs=10, validation_data=(x_val, y_val))
best_model = tuner.get_best_models(num_models=1)[0]
```

## Model Saving and Loading

```python
# Save entire model
model.save('my_model.h5')
model.save('my_model')  # SavedModel format

# Load model
loaded_model = keras.models.load_model('my_model.h5')

# Save weights only
model.save_weights('model_weights.h5')
model.load_weights('model_weights.h5')

# Save architecture only
json_config = model.to_json()
model = keras.models.model_from_json(json_config)
```

## Best Practices

**Model Design:**
- Use Functional API for complex architectures
- Apply batch normalization after dense/conv layers
- Use appropriate activation functions (ReLU for hidden, softmax/sigmoid for output)
- Initialize weights properly

**Training:**
- Normalize input data
- Use validation split or separate validation set
- Implement early stopping
- Monitor multiple metrics
- Use appropriate batch size (32-256)

**Regularization:**
- Apply dropout (0.2-0.5)
- Use L1/L2 regularization
- Implement data augmentation
- Use batch normalization

**Optimization:**
- Start with Adam optimizer
- Use learning rate schedules
- Implement gradient clipping for RNNs
- Monitor training curves

## Common Patterns

**Residual Block:**
```python
def residual_block(x, filters):
    shortcut = x
    x = layers.Conv2D(filters, 3, padding='same')(x)
    x = layers.BatchNormalization()(x)
    x = layers.ReLU()(x)
    x = layers.Conv2D(filters, 3, padding='same')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Add()([x, shortcut])
    x = layers.ReLU()(x)
    return x
```

**Inception Module:**
```python
def inception_module(x):
    branch1 = layers.Conv2D(64, 1, activation='relu', padding='same')(x)
    
    branch2 = layers.Conv2D(96, 1, activation='relu', padding='same')(x)
    branch2 = layers.Conv2D(128, 3, activation='relu', padding='same')(branch2)
    
    branch3 = layers.Conv2D(16, 1, activation='relu', padding='same')(x)
    branch3 = layers.Conv2D(32, 5, activation='relu', padding='same')(branch3)
    
    branch4 = layers.MaxPooling2D(3, strides=1, padding='same')(x)
    branch4 = layers.Conv2D(32, 1, activation='relu', padding='same')(branch4)
    
    return layers.concatenate([branch1, branch2, branch3, branch4])
```

## Pretrained Models

Available in `keras.applications`:
- VGG16, VGG19
- ResNet50, ResNet101, ResNet152
- InceptionV3, InceptionResNetV2
- MobileNet, MobileNetV2, MobileNetV3
- EfficientNetB0-B7
- DenseNet121, DenseNet169, DenseNet201
- NASNetLarge, NASNetMobile

## Learning Path

1. **Basics**: Sequential API, layers, compilation
2. **Intermediate**: Functional API, callbacks, custom layers
3. **Advanced**: Model subclassing, custom training loops
4. **Optimization**: Hyperparameter tuning, regularization
5. **Production**: Model saving, deployment, monitoring

See `references/` for advanced patterns, custom training loops, and deployment guides.
