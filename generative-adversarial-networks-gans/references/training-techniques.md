# Training Techniques

Advanced GAN training methods, loss functions, and stability improvements.

## Wasserstein GAN (WGAN)

Uses Wasserstein distance instead of JS divergence for more stable training.

```python
class WGANCritic(nn.Module):
    # Same architecture as discriminator, but no sigmoid
    def forward(self, x):
        return self.model(x)  # Output: unbounded real number

def train_wgan(generator, critic, real_imgs, latent_dim=100, n_critic=5, clip_value=0.01):
    # Train critic more than generator
    for _ in range(n_critic):
        z = torch.randn(batch_size, latent_dim)
        fake_imgs = generator(z)
        
        # Wasserstein loss
        critic_loss = -torch.mean(critic(real_imgs)) + torch.mean(critic(fake_imgs))
        
        critic_optimizer.zero_grad()
        critic_loss.backward()
        critic_optimizer.step()
        
        # Weight clipping
        for p in critic.parameters():
            p.data.clamp_(-clip_value, clip_value)
    
    # Train generator
    z = torch.randn(batch_size, latent_dim)
    fake_imgs = generator(z)
    g_loss = -torch.mean(critic(fake_imgs))
    
    g_optimizer.zero_grad()
    g_loss.backward()
    g_optimizer.step()
```

## WGAN-GP (Gradient Penalty)

Replaces weight clipping with gradient penalty:

```python
def gradient_penalty(critic, real_imgs, fake_imgs, device):
    batch_size = real_imgs.size(0)
    alpha = torch.rand(batch_size, 1, 1, 1).to(device)
    
    # Interpolate between real and fake
    interpolates = (alpha * real_imgs + (1 - alpha) * fake_imgs).requires_grad_(True)
    
    d_interpolates = critic(interpolates)
    
    # Compute gradients
    gradients = torch.autograd.grad(
        outputs=d_interpolates,
        inputs=interpolates,
        grad_outputs=torch.ones_like(d_interpolates),
        create_graph=True,
        retain_graph=True
    )[0]
    
    gradients = gradients.view(batch_size, -1)
    gradient_norm = gradients.norm(2, dim=1)
    penalty = torch.mean((gradient_norm - 1) ** 2)
    
    return penalty

# Training with GP
critic_loss = -torch.mean(critic(real_imgs)) + torch.mean(critic(fake_imgs))
gp = gradient_penalty(critic, real_imgs, fake_imgs, device)
critic_loss += lambda_gp * gp
```

## Spectral Normalization

Stabilize training by normalizing weight matrices:

```python
from torch.nn.utils import spectral_norm

class SpectralNormDiscriminator(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            spectral_norm(nn.Conv2d(3, 64, 4, 2, 1)),
            nn.LeakyReLU(0.2),
            spectral_norm(nn.Conv2d(64, 128, 4, 2, 1)),
            nn.LeakyReLU(0.2),
            spectral_norm(nn.Conv2d(128, 256, 4, 2, 1)),
            nn.LeakyReLU(0.2),
            spectral_norm(nn.Conv2d(256, 1, 4, 1, 0))
        )
```

## Self-Attention GAN (SAGAN)

Add self-attention for better global coherence:

```python
class SelfAttention(nn.Module):
    def __init__(self, in_channels):
        super().__init__()
        self.query = nn.Conv2d(in_channels, in_channels // 8, 1)
        self.key = nn.Conv2d(in_channels, in_channels // 8, 1)
        self.value = nn.Conv2d(in_channels, in_channels, 1)
        self.gamma = nn.Parameter(torch.zeros(1))
    
    def forward(self, x):
        batch, C, H, W = x.size()
        
        # Compute attention
        query = self.query(x).view(batch, -1, H * W).permute(0, 2, 1)
        key = self.key(x).view(batch, -1, H * W)
        attention = torch.softmax(torch.bmm(query, key), dim=-1)
        
        value = self.value(x).view(batch, -1, H * W)
        out = torch.bmm(value, attention.permute(0, 2, 1))
        out = out.view(batch, C, H, W)
        
        return self.gamma * out + x
```

## Progressive Growing

Gradually increase resolution during training:

```python
class ProgressiveGenerator(nn.Module):
    def __init__(self, latent_dim=512, max_resolution=1024):
        super().__init__()
        self.blocks = nn.ModuleList([
            self._make_block(latent_dim, 512, 4),  # 4x4
            self._make_block(512, 512, 8),          # 8x8
            self._make_block(512, 256, 16),         # 16x16
            self._make_block(256, 128, 32),         # 32x32
            # ... up to max_resolution
        ])
    
    def forward(self, z, alpha, depth):
        # alpha: blending factor for smooth transition
        # depth: current resolution level
        x = self.blocks[0](z)
        
        for i in range(1, depth + 1):
            x_prev = F.interpolate(x, scale_factor=2)
            x = self.blocks[i](x_prev)
            
            if i == depth and alpha < 1:
                # Blend with upsampled previous layer
                x = alpha * x + (1 - alpha) * x_prev
        
        return x
```

## Least Squares GAN (LSGAN)

Use least squares loss for more stable gradients:

```python
# Replace BCE with MSE
criterion = nn.MSELoss()

# Discriminator loss
d_loss_real = criterion(discriminator(real_imgs), torch.ones_like(real_output))
d_loss_fake = criterion(discriminator(fake_imgs), torch.zeros_like(fake_output))

# Generator loss
g_loss = criterion(discriminator(fake_imgs), torch.ones_like(fake_output))
```

## Mode Collapse Detection

```python
def detect_mode_collapse(generated_samples, threshold=0.1):
    # Compute pairwise distances
    distances = torch.cdist(generated_samples.view(len(generated_samples), -1),
                           generated_samples.view(len(generated_samples), -1))
    
    # Check if many samples are too similar
    similar_pairs = (distances < threshold).sum().item()
    total_pairs = len(generated_samples) * (len(generated_samples) - 1)
    
    collapse_ratio = similar_pairs / total_pairs
    return collapse_ratio > 0.5  # Threshold for mode collapse
```

## Unrolled GAN

Update generator considering future discriminator updates:

```python
def unrolled_generator_loss(generator, discriminator, z, n_unroll=5):
    # Save discriminator state
    backup = copy.deepcopy(discriminator.state_dict())
    
    # Unroll discriminator updates
    for _ in range(n_unroll):
        fake_imgs = generator(z)
        d_loss = discriminator_loss(discriminator, real_imgs, fake_imgs)
        d_loss.backward()
        d_optimizer.step()
    
    # Compute generator loss with updated discriminator
    fake_imgs = generator(z)
    g_loss = -torch.mean(discriminator(fake_imgs))
    
    # Restore discriminator
    discriminator.load_state_dict(backup)
    
    return g_loss
```
