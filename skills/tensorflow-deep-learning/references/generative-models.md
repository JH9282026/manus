# Generative Models in TensorFlow

## Autoencoders (AE)

Autoencoders learn compressed representations of data for reconstruction, denoising, and dimensionality reduction.

```python
# Convolutional Autoencoder for image denoising
encoder = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
    tf.keras.layers.MaxPooling2D((2, 2))
])

decoder = tf.keras.Sequential([
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
    tf.keras.layers.UpSampling2D((2, 2)),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', padding='same'),
    tf.keras.layers.UpSampling2D((2, 2)),
    tf.keras.layers.Conv2D(1, (3, 3), activation='sigmoid', padding='same')
])

autoencoder = tf.keras.Sequential([encoder, decoder])
autoencoder.compile(optimizer='adam', loss='mse')
```

## Variational Autoencoders (VAE)

VAEs learn probabilistic latent representations for generating new data.

```python
class Sampling(tf.keras.layers.Layer):
    def call(self, inputs):
        mean, log_var = inputs
        epsilon = tf.random.normal(shape=tf.shape(mean))
        return mean + tf.exp(0.5 * log_var) * epsilon

class VAE(tf.keras.Model):
    def __init__(self, latent_dim=2):
        super().__init__()
        self.latent_dim = latent_dim
        
        # Encoder
        self.encoder = tf.keras.Sequential([
            tf.keras.layers.InputLayer(input_shape=(28, 28, 1)),
            tf.keras.layers.Conv2D(32, 3, activation='relu', strides=2, padding='same'),
            tf.keras.layers.Conv2D(64, 3, activation='relu', strides=2, padding='same'),
            tf.keras.layers.Flatten()
        ])
        
        self.mean_layer = tf.keras.layers.Dense(latent_dim)
        self.logvar_layer = tf.keras.layers.Dense(latent_dim)
        self.sampling = Sampling()
        
        # Decoder
        self.decoder = tf.keras.Sequential([
            tf.keras.layers.InputLayer(input_shape=(latent_dim,)),
            tf.keras.layers.Dense(7*7*64, activation='relu'),
            tf.keras.layers.Reshape((7, 7, 64)),
            tf.keras.layers.Conv2DTranspose(64, 3, activation='relu', strides=2, padding='same'),
            tf.keras.layers.Conv2DTranspose(32, 3, activation='relu', strides=2, padding='same'),
            tf.keras.layers.Conv2DTranspose(1, 3, activation='sigmoid', padding='same')
        ])
    
    def call(self, inputs):
        x = self.encoder(inputs)
        mean = self.mean_layer(x)
        logvar = self.logvar_layer(x)
        z = self.sampling([mean, logvar])
        reconstructed = self.decoder(z)
        
        # KL divergence loss
        kl_loss = -0.5 * tf.reduce_mean(1 + logvar - tf.square(mean) - tf.exp(logvar))
        self.add_loss(kl_loss)
        
        return reconstructed

vae = VAE(latent_dim=2)
vae.compile(optimizer='adam', loss='mse')
```

## Generative Adversarial Networks (GANs)

GANs use adversarial training between generator and discriminator.

```python
# Generator
def build_generator(latent_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(7*7*256, input_shape=(latent_dim,)),
        tf.keras.layers.Reshape((7, 7, 256)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Conv2DTranspose(128, (5, 5), strides=(1, 1), padding='same', activation='relu'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Conv2DTranspose(64, (5, 5), strides=(2, 2), padding='same', activation='relu'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Conv2DTranspose(1, (5, 5), strides=(2, 2), padding='same', activation='tanh')
    ])
    return model

# Discriminator
def build_discriminator():
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(64, (5, 5), strides=(2, 2), padding='same', input_shape=(28, 28, 1)),
        tf.keras.layers.LeakyReLU(0.2),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Conv2D(128, (5, 5), strides=(2, 2), padding='same'),
        tf.keras.layers.LeakyReLU(0.2),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    return model

# Training loop
@tf.function
def train_step(images, latent_dim, generator, discriminator, g_optimizer, d_optimizer):
    batch_size = tf.shape(images)[0]
    noise = tf.random.normal([batch_size, latent_dim])
    
    # Train discriminator
    with tf.GradientTape() as disc_tape:
        generated_images = generator(noise, training=True)
        
        real_output = discriminator(images, training=True)
        fake_output = discriminator(generated_images, training=True)
        
        d_loss = tf.keras.losses.binary_crossentropy(tf.ones_like(real_output), real_output) + \
                 tf.keras.losses.binary_crossentropy(tf.zeros_like(fake_output), fake_output)
    
    d_gradients = disc_tape.gradient(d_loss, discriminator.trainable_variables)
    d_optimizer.apply_gradients(zip(d_gradients, discriminator.trainable_variables))
    
    # Train generator
    with tf.GradientTape() as gen_tape:
        generated_images = generator(noise, training=True)
        fake_output = discriminator(generated_images, training=True)
        g_loss = tf.keras.losses.binary_crossentropy(tf.ones_like(fake_output), fake_output)
    
    g_gradients = gen_tape.gradient(g_loss, generator.trainable_variables)
    g_optimizer.apply_gradients(zip(g_gradients, generator.trainable_variables))
    
    return g_loss, d_loss
```

## Conditional GANs (cGAN)

Generate specific outputs based on conditional inputs.

```python
def build_conditional_generator(latent_dim, num_classes):
    noise = tf.keras.Input(shape=(latent_dim,))
    label = tf.keras.Input(shape=(1,), dtype='int32')
    
    label_embedding = tf.keras.layers.Embedding(num_classes, latent_dim)(label)
    label_embedding = tf.keras.layers.Flatten()(label_embedding)
    
    model_input = tf.keras.layers.Concatenate()([noise, label_embedding])
    
    x = tf.keras.layers.Dense(7*7*256)(model_input)
    x = tf.keras.layers.Reshape((7, 7, 256))(x)
    x = tf.keras.layers.Conv2DTranspose(128, (5, 5), strides=(1, 1), padding='same', activation='relu')(x)
    x = tf.keras.layers.Conv2DTranspose(64, (5, 5), strides=(2, 2), padding='same', activation='relu')(x)
    output = tf.keras.layers.Conv2DTranspose(1, (5, 5), strides=(2, 2), padding='same', activation='tanh')(x)
    
    return tf.keras.Model([noise, label], output)
```

## StyleGAN Concepts

While full StyleGAN is complex, key concepts include:
- Progressive growing of networks
- Style-based generator architecture
- Adaptive instance normalization (AdaIN)
- Mapping network for latent space

## Diffusion Models

Emerging generative approach using iterative denoising.

```python
class DiffusionModel(tf.keras.Model):
    def __init__(self, timesteps=1000):
        super().__init__()
        self.timesteps = timesteps
        self.beta = tf.linspace(1e-4, 0.02, timesteps)
        self.alpha = 1 - self.beta
        self.alpha_bar = tf.math.cumprod(self.alpha)
        
        self.denoising_network = self.build_unet()
    
    def forward_diffusion(self, x0, t):
        noise = tf.random.normal(shape=tf.shape(x0))
        alpha_bar_t = tf.gather(self.alpha_bar, t)
        alpha_bar_t = tf.reshape(alpha_bar_t, [-1, 1, 1, 1])
        
        xt = tf.sqrt(alpha_bar_t) * x0 + tf.sqrt(1 - alpha_bar_t) * noise
        return xt, noise
    
    def train_step(self, x0):
        batch_size = tf.shape(x0)[0]
        t = tf.random.uniform([batch_size], 0, self.timesteps, dtype=tf.int32)
        
        with tf.GradientTape() as tape:
            xt, noise = self.forward_diffusion(x0, t)
            predicted_noise = self.denoising_network([xt, t])
            loss = tf.reduce_mean(tf.square(noise - predicted_noise))
        
        gradients = tape.gradient(loss, self.trainable_variables)
        self.optimizer.apply_gradients(zip(gradients, self.trainable_variables))
        return loss
```
