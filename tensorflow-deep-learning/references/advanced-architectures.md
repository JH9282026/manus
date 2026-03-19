# Advanced TensorFlow Architectures

## ResNet (Residual Networks)

Residual connections solve vanishing gradient problems in deep networks.

```python
def residual_block(x, filters, kernel_size=3, stride=1):
    shortcut = x
    
    # Main path
    x = tf.keras.layers.Conv2D(filters, kernel_size, strides=stride, padding='same')(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.ReLU()(x)
    
    x = tf.keras.layers.Conv2D(filters, kernel_size, padding='same')(x)
    x = tf.keras.layers.BatchNormalization()(x)
    
    # Adjust shortcut dimensions if needed
    if stride != 1 or shortcut.shape[-1] != filters:
        shortcut = tf.keras.layers.Conv2D(filters, 1, strides=stride)(shortcut)
        shortcut = tf.keras.layers.BatchNormalization()(shortcut)
    
    # Add shortcut
    x = tf.keras.layers.Add()([x, shortcut])
    x = tf.keras.layers.ReLU()(x)
    return x

def build_resnet(input_shape, num_classes):
    inputs = tf.keras.Input(shape=input_shape)
    
    x = tf.keras.layers.Conv2D(64, 7, strides=2, padding='same')(inputs)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.ReLU()(x)
    x = tf.keras.layers.MaxPooling2D(3, strides=2, padding='same')(x)
    
    # Residual blocks
    x = residual_block(x, 64)
    x = residual_block(x, 64)
    x = residual_block(x, 128, stride=2)
    x = residual_block(x, 128)
    x = residual_block(x, 256, stride=2)
    x = residual_block(x, 256)
    
    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    outputs = tf.keras.layers.Dense(num_classes, activation='softmax')(x)
    
    return tf.keras.Model(inputs=inputs, outputs=outputs)
```

## Inception Networks

Multi-scale feature extraction with parallel convolutions.

```python
def inception_module(x, filters_1x1, filters_3x3_reduce, filters_3x3, 
                      filters_5x5_reduce, filters_5x5, filters_pool_proj):
    # 1x1 convolution branch
    conv_1x1 = tf.keras.layers.Conv2D(filters_1x1, 1, activation='relu', padding='same')(x)
    
    # 3x3 convolution branch
    conv_3x3 = tf.keras.layers.Conv2D(filters_3x3_reduce, 1, activation='relu', padding='same')(x)
    conv_3x3 = tf.keras.layers.Conv2D(filters_3x3, 3, activation='relu', padding='same')(conv_3x3)
    
    # 5x5 convolution branch
    conv_5x5 = tf.keras.layers.Conv2D(filters_5x5_reduce, 1, activation='relu', padding='same')(x)
    conv_5x5 = tf.keras.layers.Conv2D(filters_5x5, 5, activation='relu', padding='same')(conv_5x5)
    
    # Max pooling branch
    pool = tf.keras.layers.MaxPooling2D(3, strides=1, padding='same')(x)
    pool = tf.keras.layers.Conv2D(filters_pool_proj, 1, activation='relu', padding='same')(pool)
    
    # Concatenate all branches
    output = tf.keras.layers.concatenate([conv_1x1, conv_3x3, conv_5x5, pool], axis=-1)
    return output
```

## EfficientNet

Compound scaling of depth, width, and resolution.

```python
# Use pre-trained EfficientNet
base_model = tf.keras.applications.EfficientNetB0(
    include_top=False,
    weights='imagenet',
    input_shape=(224, 224, 3)
)

# Fine-tune top layers
for layer in base_model.layers[:-20]:
    layer.trainable = False

model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(num_classes, activation='softmax')
])
```

## Attention Mechanisms

### Self-Attention Layer

```python
class SelfAttention(tf.keras.layers.Layer):
    def __init__(self, d_model):
        super().__init__()
        self.d_model = d_model
        self.wq = tf.keras.layers.Dense(d_model)
        self.wk = tf.keras.layers.Dense(d_model)
        self.wv = tf.keras.layers.Dense(d_model)
        self.dense = tf.keras.layers.Dense(d_model)
    
    def call(self, x):
        q = self.wq(x)
        k = self.wk(x)
        v = self.wv(x)
        
        # Scaled dot-product attention
        matmul_qk = tf.matmul(q, k, transpose_b=True)
        dk = tf.cast(tf.shape(k)[-1], tf.float32)
        scaled_attention_logits = matmul_qk / tf.math.sqrt(dk)
        
        attention_weights = tf.nn.softmax(scaled_attention_logits, axis=-1)
        output = tf.matmul(attention_weights, v)
        
        return self.dense(output)
```

### Squeeze-and-Excitation (SE) Block

```python
def se_block(input_tensor, ratio=16):
    channel_axis = -1
    filters = input_tensor.shape[channel_axis]
    se_shape = (1, 1, filters)
    
    # Squeeze: Global average pooling
    se = tf.keras.layers.GlobalAveragePooling2D()(input_tensor)
    se = tf.keras.layers.Reshape(se_shape)(se)
    
    # Excitation: FC layers
    se = tf.keras.layers.Dense(filters // ratio, activation='relu')(se)
    se = tf.keras.layers.Dense(filters, activation='sigmoid')(se)
    
    # Scale
    return tf.keras.layers.multiply([input_tensor, se])
```

## Vision Transformer (ViT)

```python
class PatchEmbedding(tf.keras.layers.Layer):
    def __init__(self, patch_size, embed_dim):
        super().__init__()
        self.patch_size = patch_size
        self.projection = tf.keras.layers.Dense(embed_dim)
    
    def call(self, images):
        batch_size = tf.shape(images)[0]
        patches = tf.image.extract_patches(
            images=images,
            sizes=[1, self.patch_size, self.patch_size, 1],
            strides=[1, self.patch_size, self.patch_size, 1],
            rates=[1, 1, 1, 1],
            padding='VALID'
        )
        patch_dims = patches.shape[-1]
        patches = tf.reshape(patches, [batch_size, -1, patch_dims])
        return self.projection(patches)

class TransformerBlock(tf.keras.layers.Layer):
    def __init__(self, embed_dim, num_heads, ff_dim, dropout=0.1):
        super().__init__()
        self.att = tf.keras.layers.MultiHeadAttention(num_heads=num_heads, key_dim=embed_dim)
        self.ffn = tf.keras.Sequential([
            tf.keras.layers.Dense(ff_dim, activation='gelu'),
            tf.keras.layers.Dense(embed_dim),
        ])
        self.layernorm1 = tf.keras.layers.LayerNormalization(epsilon=1e-6)
        self.layernorm2 = tf.keras.layers.LayerNormalization(epsilon=1e-6)
        self.dropout1 = tf.keras.layers.Dropout(dropout)
        self.dropout2 = tf.keras.layers.Dropout(dropout)
    
    def call(self, inputs, training):
        attn_output = self.att(inputs, inputs)
        attn_output = self.dropout1(attn_output, training=training)
        out1 = self.layernorm1(inputs + attn_output)
        
        ffn_output = self.ffn(out1)
        ffn_output = self.dropout2(ffn_output, training=training)
        return self.layernorm2(out1 + ffn_output)
```

## Neural Style Transfer

```python
def style_transfer_model():
    # Load VGG19 for feature extraction
    vgg = tf.keras.applications.VGG19(include_top=False, weights='imagenet')
    vgg.trainable = False
    
    # Content and style layers
    content_layers = ['block5_conv2']
    style_layers = ['block1_conv1', 'block2_conv1', 'block3_conv1', 'block4_conv1', 'block5_conv1']
    
    outputs = [vgg.get_layer(name).output for name in (style_layers + content_layers)]
    model = tf.keras.Model([vgg.input], outputs)
    return model

def compute_loss(model, loss_weights, init_image, gram_style_features, content_features):
    style_weight, content_weight = loss_weights
    
    model_outputs = model(init_image)
    style_output_features = model_outputs[:len(style_layers)]
    content_output_features = model_outputs[len(style_layers):]
    
    # Style loss
    style_score = 0
    for target_style, comb_style in zip(gram_style_features, style_output_features):
        style_score += tf.reduce_mean((comb_style - target_style)**2)
    style_score *= style_weight / len(style_layers)
    
    # Content loss
    content_score = 0
    for target_content, comb_content in zip(content_features, content_output_features):
        content_score += tf.reduce_mean((comb_content - target_content)**2)
    content_score *= content_weight / len(content_layers)
    
    return style_score + content_score
```

## Siamese Networks

```python
def create_base_network(input_shape):
    inputs = tf.keras.Input(shape=input_shape)
    x = tf.keras.layers.Conv2D(64, (3, 3), activation='relu')(inputs)
    x = tf.keras.layers.MaxPooling2D()(x)
    x = tf.keras.layers.Conv2D(128, (3, 3), activation='relu')(x)
    x = tf.keras.layers.MaxPooling2D()(x)
    x = tf.keras.layers.Flatten()(x)
    x = tf.keras.layers.Dense(128, activation='relu')(x)
    return tf.keras.Model(inputs, x)

def build_siamese_network(input_shape):
    base_network = create_base_network(input_shape)
    
    input_a = tf.keras.Input(shape=input_shape)
    input_b = tf.keras.Input(shape=input_shape)
    
    # Share weights between both inputs
    processed_a = base_network(input_a)
    processed_b = base_network(input_b)
    
    # Compute L1 distance
    distance = tf.keras.layers.Lambda(
        lambda tensors: tf.abs(tensors[0] - tensors[1])
    )([processed_a, processed_b])
    
    outputs = tf.keras.layers.Dense(1, activation='sigmoid')(distance)
    
    return tf.keras.Model([input_a, input_b], outputs)
```

## Memory-Efficient Training

### Gradient Checkpointing

```python
import tensorflow_addons as tfa

# Use gradient checkpointing for memory-intensive models
class CheckpointedModel(tf.keras.Model):
    def __init__(self):
        super().__init__()
        self.layers_list = [create_layer(i) for i in range(num_layers)]
    
    @tf.recompute_grad
    def call(self, inputs):
        x = inputs
        for layer in self.layers_list:
            x = layer(x)
        return x
```

### Mixed Precision with Loss Scaling

```python
policy = tf.keras.mixed_precision.Policy('mixed_float16')
tf.keras.mixed_precision.set_global_policy(policy)

model = create_model()
optimizer = tf.keras.optimizers.Adam()
optimizer = tf.keras.mixed_precision.LossScaleOptimizer(optimizer)

@tf.function
def train_step(x, y):
    with tf.GradientTape() as tape:
        predictions = model(x, training=True)
        loss = loss_fn(y, predictions)
        scaled_loss = optimizer.get_scaled_loss(loss)
    
    scaled_gradients = tape.gradient(scaled_loss, model.trainable_variables)
    gradients = optimizer.get_unscaled_gradients(scaled_gradients)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))
    
    return loss
```