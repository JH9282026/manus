# Advanced Keras Architectures and Patterns

## Overview

Keras's flexible API enables the construction of sophisticated neural network architectures beyond simple sequential models. This guide explores advanced architectural patterns, including convolutional neural networks (CNNs), recurrent neural networks (RNNs), hybrid architectures, and modern innovations like attention mechanisms and transformers.

## Convolutional Neural Networks (CNNs)

### CNN Fundamentals

CNNs are specialized for processing grid-like data (images, videos, time series) by exploiting spatial hierarchies through:

- **Local Connectivity**: Neurons connect to local regions
- **Parameter Sharing**: Same weights applied across spatial locations
- **Translation Invariance**: Detect features regardless of position
- **Hierarchical Feature Learning**: Low-level to high-level features

### Basic CNN Architecture

```python
import keras
from keras import layers

model = keras.Sequential([
    # First convolutional block
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    
    # Second convolutional block
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    
    # Third convolutional block
    layers.Conv2D(64, (3, 3), activation='relu'),
    
    # Dense layers
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax')
])
```

### CNN Layer Types

#### Convolutional Layers

**Conv2D** (for images):
```python
layers.Conv2D(
    filters=32,           # Number of output filters
    kernel_size=(3, 3),   # Filter size
    strides=(1, 1),       # Stride
    padding='valid',      # 'valid' or 'same'
    activation='relu',
    kernel_initializer='he_normal'
)
```

**Conv1D** (for sequences):
```python
layers.Conv1D(filters=64, kernel_size=5, activation='relu')
```

**Conv3D** (for 3D data like videos):
```python
layers.Conv3D(filters=16, kernel_size=(3, 3, 3), activation='relu')
```

**Depthwise Separable Convolution** (efficient):
```python
layers.SeparableConv2D(filters=64, kernel_size=(3, 3), activation='relu')
```

#### Pooling Layers

**Max Pooling**:
```python
layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2))
```

**Average Pooling**:
```python
layers.AveragePooling2D(pool_size=(2, 2))
```

**Global Pooling**:
```python
layers.GlobalMaxPooling2D()  # Reduces to 1D
layers.GlobalAveragePooling2D()  # Common before final dense layer
```

### Advanced CNN Patterns

#### 1. Residual Connections (ResNet)

**Purpose**: Enable training of very deep networks by addressing vanishing gradients.

**Implementation**:
```python
def residual_block(x, filters, kernel_size=3):
    # Main path
    fx = layers.Conv2D(filters, kernel_size, padding='same')(x)
    fx = layers.BatchNormalization()(fx)
    fx = layers.Activation('relu')(fx)
    fx = layers.Conv2D(filters, kernel_size, padding='same')(fx)
    fx = layers.BatchNormalization()(fx)
    
    # Shortcut path
    if x.shape[-1] != filters:
        x = layers.Conv2D(filters, 1, padding='same')(x)  # 1x1 conv for dimension matching
    
    # Add shortcut to main path
    out = layers.Add()([x, fx])
    out = layers.Activation('relu')(out)
    return out

# Build ResNet-style model
inputs = keras.Input(shape=(32, 32, 3))
x = layers.Conv2D(64, 7, strides=2, padding='same')(inputs)
x = layers.BatchNormalization()(x)
x = layers.Activation('relu')(x)
x = layers.MaxPooling2D(3, strides=2, padding='same')(x)

# Stack residual blocks
x = residual_block(x, 64)
x = residual_block(x, 64)
x = residual_block(x, 128)
x = residual_block(x, 128)

x = layers.GlobalAveragePooling2D()(x)
outputs = layers.Dense(10, activation='softmax')(x)

model = keras.Model(inputs, outputs, name='resnet_style')
```

**Benefits**:
- Enables training of 100+ layer networks
- Addresses vanishing gradient problem
- Improves gradient flow
- Better feature reuse

#### 2. Inception Modules

**Purpose**: Capture features at multiple scales simultaneously.

**Implementation**:
```python
def inception_module(x, filters_1x1, filters_3x3_reduce, filters_3x3, 
                     filters_5x5_reduce, filters_5x5, filters_pool_proj):
    # 1x1 convolution branch
    conv_1x1 = layers.Conv2D(filters_1x1, 1, padding='same', activation='relu')(x)
    
    # 3x3 convolution branch
    conv_3x3 = layers.Conv2D(filters_3x3_reduce, 1, padding='same', activation='relu')(x)
    conv_3x3 = layers.Conv2D(filters_3x3, 3, padding='same', activation='relu')(conv_3x3)
    
    # 5x5 convolution branch
    conv_5x5 = layers.Conv2D(filters_5x5_reduce, 1, padding='same', activation='relu')(x)
    conv_5x5 = layers.Conv2D(filters_5x5, 5, padding='same', activation='relu')(conv_5x5)
    
    # Max pooling branch
    pool = layers.MaxPooling2D(3, strides=1, padding='same')(x)
    pool = layers.Conv2D(filters_pool_proj, 1, padding='same', activation='relu')(pool)
    
    # Concatenate all branches
    output = layers.Concatenate()([conv_1x1, conv_3x3, conv_5x5, pool])
    return output

# Use in model
inputs = keras.Input(shape=(224, 224, 3))
x = layers.Conv2D(64, 7, strides=2, padding='same', activation='relu')(inputs)
x = layers.MaxPooling2D(3, strides=2, padding='same')(x)
x = inception_module(x, 64, 96, 128, 16, 32, 32)
x = inception_module(x, 128, 128, 192, 32, 96, 64)
# ... more layers
```

**Benefits**:
- Multi-scale feature extraction
- Efficient parameter usage
- Improved representational power

#### 3. Dense Connections (DenseNet)

**Purpose**: Connect each layer to every subsequent layer.

**Implementation**:
```python
def dense_block(x, num_layers, growth_rate):
    for i in range(num_layers):
        # Bottleneck layer
        bn = layers.BatchNormalization()(x)
        bn = layers.Activation('relu')(bn)
        bn = layers.Conv2D(4 * growth_rate, 1, padding='same')(bn)
        
        # 3x3 convolution
        bn = layers.BatchNormalization()(bn)
        bn = layers.Activation('relu')(bn)
        conv = layers.Conv2D(growth_rate, 3, padding='same')(bn)
        
        # Concatenate with input
        x = layers.Concatenate()([x, conv])
    return x

def transition_block(x, compression=0.5):
    num_filters = int(x.shape[-1] * compression)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    x = layers.Conv2D(num_filters, 1, padding='same')(x)
    x = layers.AveragePooling2D(2, strides=2)(x)
    return x
```

**Benefits**:
- Alleviates vanishing gradient
- Encourages feature reuse
- Reduces number of parameters

## Recurrent Neural Networks (RNNs)

### RNN Fundamentals

RNNs process sequential data by maintaining internal state (memory):

- **Sequential Processing**: Process one element at a time
- **Memory**: Maintain hidden state across time steps
- **Parameter Sharing**: Same weights across all time steps
- **Variable Length**: Handle sequences of different lengths

### Basic RNN Types

#### Simple RNN

```python
model = keras.Sequential([
    layers.SimpleRNN(64, return_sequences=True, input_shape=(None, input_dim)),
    layers.SimpleRNN(32),
    layers.Dense(output_dim, activation='softmax')
])
```

**Limitations**: Vanishing gradient problem for long sequences.

#### LSTM (Long Short-Term Memory)

**Purpose**: Address vanishing gradient problem with gating mechanisms.

```python
model = keras.Sequential([
    layers.LSTM(128, return_sequences=True, input_shape=(timesteps, features)),
    layers.Dropout(0.2),
    layers.LSTM(64),
    layers.Dropout(0.2),
    layers.Dense(num_classes, activation='softmax')
])
```

**LSTM Gates**:
- **Forget Gate**: Decide what to forget from cell state
- **Input Gate**: Decide what new information to store
- **Output Gate**: Decide what to output

**When to Use**:
- Long sequences (>100 time steps)
- Long-term dependencies important
- Text, speech, time series

#### GRU (Gated Recurrent Unit)

**Purpose**: Simplified LSTM with fewer parameters.

```python
model = keras.Sequential([
    layers.GRU(128, return_sequences=True, input_shape=(timesteps, features)),
    layers.GRU(64),
    layers.Dense(num_classes, activation='softmax')
])
```

**Benefits**:
- Faster training than LSTM
- Fewer parameters
- Often similar performance to LSTM

### Advanced RNN Patterns

#### Bidirectional RNNs

**Purpose**: Process sequence in both forward and backward directions.

```python
model = keras.Sequential([
    layers.Bidirectional(layers.LSTM(64, return_sequences=True), 
                        input_shape=(timesteps, features)),
    layers.Bidirectional(layers.LSTM(32)),
    layers.Dense(num_classes, activation='softmax')
])
```

**Benefits**:
- Access to future context
- Better for tasks where full sequence is available
- Improved performance on many NLP tasks

**Use Cases**:
- Text classification
- Named entity recognition
- Speech recognition
- Machine translation (encoder)

#### Stacked RNNs

**Purpose**: Create deeper recurrent architectures.

```python
model = keras.Sequential([
    layers.LSTM(128, return_sequences=True, input_shape=(timesteps, features)),
    layers.Dropout(0.2),
    layers.LSTM(128, return_sequences=True),
    layers.Dropout(0.2),
    layers.LSTM(64),
    layers.Dense(num_classes, activation='softmax')
])
```

**Key**: Set `return_sequences=True` for all but last RNN layer.

#### Encoder-Decoder Architecture

**Purpose**: Sequence-to-sequence tasks (translation, summarization).

```python
# Encoder
encoder_inputs = keras.Input(shape=(None, num_encoder_tokens))
encoder_lstm = layers.LSTM(latent_dim, return_state=True)
encoder_outputs, state_h, state_c = encoder_lstm(encoder_inputs)
encoder_states = [state_h, state_c]

# Decoder
decoder_inputs = keras.Input(shape=(None, num_decoder_tokens))
decoder_lstm = layers.LSTM(latent_dim, return_sequences=True, return_state=True)
decoder_outputs, _, _ = decoder_lstm(decoder_inputs, initial_state=encoder_states)
decoder_dense = layers.Dense(num_decoder_tokens, activation='softmax')
decoder_outputs = decoder_dense(decoder_outputs)

# Model
model = keras.Model([encoder_inputs, decoder_inputs], decoder_outputs)
```

## Hybrid Architectures

### CNN + RNN

**Purpose**: Combine spatial feature extraction with temporal modeling.

**Use Cases**:
- Video classification
- Action recognition
- Time series with spatial structure

**Implementation**:
```python
# For video data: (samples, frames, height, width, channels)
inputs = keras.Input(shape=(frames, height, width, channels))

# Apply CNN to each frame using TimeDistributed
x = layers.TimeDistributed(layers.Conv2D(32, 3, activation='relu'))(inputs)
x = layers.TimeDistributed(layers.MaxPooling2D(2))(x)
x = layers.TimeDistributed(layers.Conv2D(64, 3, activation='relu'))(x)
x = layers.TimeDistributed(layers.MaxPooling2D(2))(x)
x = layers.TimeDistributed(layers.Flatten())(x)

# RNN to model temporal dependencies
x = layers.LSTM(128, return_sequences=True)(x)
x = layers.LSTM(64)(x)

# Output
outputs = layers.Dense(num_classes, activation='softmax')(x)

model = keras.Model(inputs, outputs)
```

### Transformer Encoder + LSTM

**Purpose**: Combine attention mechanisms with recurrent processing.

```python
import keras_hub

inputs = keras.Input(shape=(sequence_length, embedding_dim))

# Transformer encoder for global patterns
x = keras_hub.layers.TransformerEncoder(
    intermediate_dim=512,
    num_heads=8,
    dropout=0.1
)(inputs)

# LSTM for sequential processing
x = layers.LSTM(128, return_sequences=True)(x)
x = layers.LSTM(64)(x)

outputs = layers.Dense(num_classes, activation='softmax')(x)
model = keras.Model(inputs, outputs)
```

## Attention Mechanisms

### Self-Attention

**Purpose**: Allow model to focus on relevant parts of input.

**Basic Implementation**:
```python
class SelfAttention(layers.Layer):
    def __init__(self, units):
        super().__init__()
        self.W_q = layers.Dense(units)
        self.W_k = layers.Dense(units)
        self.W_v = layers.Dense(units)
    
    def call(self, inputs):
        # Query, Key, Value
        q = self.W_q(inputs)
        k = self.W_k(inputs)
        v = self.W_v(inputs)
        
        # Attention scores
        scores = keras.ops.matmul(q, keras.ops.transpose(k, [0, 2, 1]))
        scores = scores / keras.ops.sqrt(keras.ops.cast(k.shape[-1], 'float32'))
        
        # Attention weights
        weights = keras.ops.softmax(scores, axis=-1)
        
        # Weighted sum
        output = keras.ops.matmul(weights, v)
        return output
```

### Multi-Head Attention

**Purpose**: Attend to different representation subspaces.

```python
from keras.layers import MultiHeadAttention

# Use built-in multi-head attention
attention_layer = MultiHeadAttention(
    num_heads=8,
    key_dim=64,
    dropout=0.1
)

# In model
x = attention_layer(query=x, value=x, key=x)
```

## Transformer Architecture

### Transformer Encoder

```python
def transformer_encoder(inputs, num_heads, ff_dim, dropout=0.1):
    # Multi-head attention
    attention_output = layers.MultiHeadAttention(
        num_heads=num_heads,
        key_dim=inputs.shape[-1] // num_heads,
        dropout=dropout
    )(inputs, inputs)
    attention_output = layers.Dropout(dropout)(attention_output)
    x = layers.LayerNormalization(epsilon=1e-6)(inputs + attention_output)
    
    # Feed-forward network
    ff_output = layers.Dense(ff_dim, activation='relu')(x)
    ff_output = layers.Dense(inputs.shape[-1])(ff_output)
    ff_output = layers.Dropout(dropout)(ff_output)
    output = layers.LayerNormalization(epsilon=1e-6)(x + ff_output)
    
    return output

# Build transformer model
inputs = keras.Input(shape=(sequence_length, embedding_dim))
x = inputs

# Stack transformer encoders
for _ in range(num_transformer_blocks):
    x = transformer_encoder(x, num_heads=8, ff_dim=512)

x = layers.GlobalAveragePooling1D()(x)
x = layers.Dropout(0.1)(x)
outputs = layers.Dense(num_classes, activation='softmax')(x)

model = keras.Model(inputs, outputs)
```

## Autoencoders

### Vanilla Autoencoder

```python
# Encoder
encoder_input = keras.Input(shape=(784,))
encoded = layers.Dense(128, activation='relu')(encoder_input)
encoded = layers.Dense(64, activation='relu')(encoded)
encoded = layers.Dense(32, activation='relu')(encoded)

# Decoder
decoded = layers.Dense(64, activation='relu')(encoded)
decoded = layers.Dense(128, activation='relu')(decoded)
decoded = layers.Dense(784, activation='sigmoid')(decoded)

# Autoencoder
autoencoder = keras.Model(encoder_input, decoded)
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')
```

### Variational Autoencoder (VAE)

```python
class Sampling(layers.Layer):
    def call(self, inputs):
        z_mean, z_log_var = inputs
        batch = keras.ops.shape(z_mean)[0]
        dim = keras.ops.shape(z_mean)[1]
        epsilon = keras.random.normal(shape=(batch, dim))
        return z_mean + keras.ops.exp(0.5 * z_log_var) * epsilon

# Encoder
latent_dim = 2
encoder_inputs = keras.Input(shape=(28, 28, 1))
x = layers.Conv2D(32, 3, activation='relu', strides=2, padding='same')(encoder_inputs)
x = layers.Conv2D(64, 3, activation='relu', strides=2, padding='same')(x)
x = layers.Flatten()(x)
x = layers.Dense(16, activation='relu')(x)
z_mean = layers.Dense(latent_dim, name='z_mean')(x)
z_log_var = layers.Dense(latent_dim, name='z_log_var')(x)
z = Sampling()([z_mean, z_log_var])
encoder = keras.Model(encoder_inputs, [z_mean, z_log_var, z], name='encoder')

# Decoder
latent_inputs = keras.Input(shape=(latent_dim,))
x = layers.Dense(7 * 7 * 64, activation='relu')(latent_inputs)
x = layers.Reshape((7, 7, 64))(x)
x = layers.Conv2DTranspose(64, 3, activation='relu', strides=2, padding='same')(x)
x = layers.Conv2DTranspose(32, 3, activation='relu', strides=2, padding='same')(x)
decoder_outputs = layers.Conv2DTranspose(1, 3, activation='sigmoid', padding='same')(x)
decoder = keras.Model(latent_inputs, decoder_outputs, name='decoder')
```

## Key Takeaways

1. **CNNs**: Specialized for spatial data; use residual connections for deep networks
2. **RNNs**: Process sequential data; LSTM/GRU for long-term dependencies
3. **Bidirectional RNNs**: Access future context; better for offline tasks
4. **Hybrid Architectures**: Combine CNN + RNN for spatiotemporal data
5. **Attention**: Focus on relevant parts; foundation of transformers
6. **Transformers**: State-of-the-art for NLP; parallel processing advantage
7. **Residual Connections**: Enable very deep networks
8. **Inception Modules**: Multi-scale feature extraction
9. **Autoencoders**: Unsupervised learning; dimensionality reduction
10. **Functional API**: Essential for complex architectures

## References

- ResNet Paper: https://arxiv.org/abs/1512.03385
- Inception Paper: https://arxiv.org/abs/1409.4842
- LSTM Paper: https://www.bioinf.jku.at/publications/older/2604.pdf
- Attention Paper: https://arxiv.org/abs/1706.03762
- Transformer Paper: https://arxiv.org/abs/1706.03762
- VAE Paper: https://arxiv.org/abs/1312.6114
