# GAN Variants

Advanced GAN architectures including StyleGAN, CycleGAN, and Progressive GAN.

## StyleGAN

Style-based generator for high-quality image synthesis.

```python
class StyleGANGenerator(nn.Module):
    def __init__(self, latent_dim=512, style_dim=512):
        super().__init__()
        
        # Mapping network: z -> w
        self.mapping = nn.Sequential(
            nn.Linear(latent_dim, style_dim),
            nn.LeakyReLU(0.2),
            nn.Linear(style_dim, style_dim),
            nn.LeakyReLU(0.2),
            nn.Linear(style_dim, style_dim)
        )
        
        # Synthesis network with AdaIN
        self.synthesis = SynthesisNetwork(style_dim)
    
    def forward(self, z):
        w = self.mapping(z)
        return self.synthesis(w)

class AdaptiveInstanceNorm(nn.Module):
    def __init__(self, in_channels, style_dim):
        super().__init__()
        self.norm = nn.InstanceNorm2d(in_channels, affine=False)
        self.style_scale = nn.Linear(style_dim, in_channels)
        self.style_bias = nn.Linear(style_dim, in_channels)
    
    def forward(self, x, w):
        normalized = self.norm(x)
        style_scale = self.style_scale(w).unsqueeze(2).unsqueeze(3)
        style_bias = self.style_bias(w).unsqueeze(2).unsqueeze(3)
        return style_scale * normalized + style_bias
```

## CycleGAN

Unpaired image-to-image translation:

```python
class CycleGAN:
    def __init__(self):
        self.G_AB = Generator()  # A -> B
        self.G_BA = Generator()  # B -> A
        self.D_A = Discriminator()
        self.D_B = Discriminator()
        
        self.criterion_GAN = nn.MSELoss()
        self.criterion_cycle = nn.L1Loss()
        self.criterion_identity = nn.L1Loss()
    
    def train_step(self, real_A, real_B):
        # Generate fake images
        fake_B = self.G_AB(real_A)
        fake_A = self.G_BA(real_B)
        
        # Cycle consistency
        reconstructed_A = self.G_BA(fake_B)
        reconstructed_B = self.G_AB(fake_A)
        
        # Generator losses
        loss_GAN_AB = self.criterion_GAN(self.D_B(fake_B), torch.ones_like(self.D_B(fake_B)))
        loss_GAN_BA = self.criterion_GAN(self.D_A(fake_A), torch.ones_like(self.D_A(fake_A)))
        
        loss_cycle_A = self.criterion_cycle(reconstructed_A, real_A)
        loss_cycle_B = self.criterion_cycle(reconstructed_B, real_B)
        
        # Identity loss (optional)
        loss_identity_A = self.criterion_identity(self.G_BA(real_A), real_A)
        loss_identity_B = self.criterion_identity(self.G_AB(real_B), real_B)
        
        # Total generator loss
        loss_G = (loss_GAN_AB + loss_GAN_BA + 
                  10 * (loss_cycle_A + loss_cycle_B) +
                  5 * (loss_identity_A + loss_identity_B))
        
        return loss_G
```

## BigGAN

Large-scale GAN with class conditioning:

```python
class BigGANGenerator(nn.Module):
    def __init__(self, latent_dim=128, n_classes=1000):
        super().__init__()
        self.class_embedding = nn.Embedding(n_classes, latent_dim)
        
        # Hierarchical latent space
        self.blocks = nn.ModuleList([
            BigGANBlock(latent_dim, 1024, 512),
            BigGANBlock(latent_dim, 512, 256),
            BigGANBlock(latent_dim, 256, 128),
            BigGANBlock(latent_dim, 128, 64)
        ])
    
    def forward(self, z, class_labels):
        class_embed = self.class_embedding(class_labels)
        h = z + class_embed  # Combine noise and class
        
        for block in self.blocks:
            h = block(h, class_embed)
        
        return h
```
