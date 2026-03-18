# Applications and Implementations

Practical GAN applications including image-to-image translation, super-resolution, and text-to-image synthesis.

## Pix2Pix (Paired Image Translation)

```python
class Pix2PixGenerator(nn.Module):
    # U-Net architecture
    def __init__(self, in_channels=3, out_channels=3):
        super().__init__()
        
        # Encoder
        self.down1 = self._down_block(in_channels, 64, normalize=False)
        self.down2 = self._down_block(64, 128)
        self.down3 = self._down_block(128, 256)
        self.down4 = self._down_block(256, 512)
        
        # Decoder with skip connections
        self.up1 = self._up_block(512, 256)
        self.up2 = self._up_block(512, 128)  # 512 = 256 + 256 (skip)
        self.up3 = self._up_block(256, 64)
        self.up4 = nn.ConvTranspose2d(128, out_channels, 4, 2, 1)
    
    def forward(self, x):
        d1 = self.down1(x)
        d2 = self.down2(d1)
        d3 = self.down3(d2)
        d4 = self.down4(d3)
        
        u1 = self.up1(d4)
        u2 = self.up2(torch.cat([u1, d3], 1))
        u3 = self.up3(torch.cat([u2, d2], 1))
        return torch.tanh(self.up4(torch.cat([u3, d1], 1)))

class PatchGANDiscriminator(nn.Module):
    # 70x70 PatchGAN
    def __init__(self, in_channels=6):  # Input + target
        super().__init__()
        self.model = nn.Sequential(
            nn.Conv2d(in_channels, 64, 4, 2, 1),
            nn.LeakyReLU(0.2),
            nn.Conv2d(64, 128, 4, 2, 1),
            nn.BatchNorm2d(128),
            nn.LeakyReLU(0.2),
            nn.Conv2d(128, 256, 4, 2, 1),
            nn.BatchNorm2d(256),
            nn.LeakyReLU(0.2),
            nn.Conv2d(256, 1, 4, 1, 1)
        )

# Training with L1 loss
def train_pix2pix(input_img, target_img, generator, discriminator):
    fake_img = generator(input_img)
    
    # Discriminator loss
    real_pair = torch.cat([input_img, target_img], 1)
    fake_pair = torch.cat([input_img, fake_img.detach()], 1)
    
    d_loss = (criterion_GAN(discriminator(real_pair), torch.ones_like(...)) +
              criterion_GAN(discriminator(fake_pair), torch.zeros_like(...)))
    
    # Generator loss
    g_loss_GAN = criterion_GAN(discriminator(torch.cat([input_img, fake_img], 1)), torch.ones_like(...))
    g_loss_L1 = nn.L1Loss()(fake_img, target_img)
    g_loss = g_loss_GAN + 100 * g_loss_L1  # L1 weight = 100
    
    return d_loss, g_loss
```

## SRGAN (Super-Resolution)

```python
class SRGANGenerator(nn.Module):
    def __init__(self, n_residual_blocks=16):
        super().__init__()
        
        # Initial convolution
        self.conv1 = nn.Conv2d(3, 64, 9, padding=4)
        
        # Residual blocks
        self.res_blocks = nn.Sequential(*[ResidualBlock(64) for _ in range(n_residual_blocks)])
        
        # Upsampling
        self.upsample = nn.Sequential(
            nn.Conv2d(64, 256, 3, padding=1),
            nn.PixelShuffle(2),  # 2x upscale
            nn.PReLU(),
            nn.Conv2d(64, 256, 3, padding=1),
            nn.PixelShuffle(2),  # 2x upscale
            nn.PReLU()
        )
        
        # Output
        self.conv2 = nn.Conv2d(64, 3, 9, padding=4)
    
    def forward(self, x):
        out1 = self.conv1(x)
        out = self.res_blocks(out1)
        out2 = self.upsample(out + out1)
        return torch.tanh(self.conv2(out2))

# Perceptual loss using VGG features
class PerceptualLoss(nn.Module):
    def __init__(self):
        super().__init__()
        vgg = torchvision.models.vgg19(pretrained=True).features[:36]
        self.vgg = vgg.eval()
        for param in self.vgg.parameters():
            param.requires_grad = False
    
    def forward(self, sr, hr):
        sr_features = self.vgg(sr)
        hr_features = self.vgg(hr)
        return nn.MSELoss()(sr_features, hr_features)
```

## Text-to-Image (AttnGAN)

```python
class TextEncoder(nn.Module):
    def __init__(self, vocab_size, embed_dim=256, hidden_dim=128):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, bidirectional=True, batch_first=True)
    
    def forward(self, captions, lengths):
        embeddings = self.embedding(captions)
        packed = nn.utils.rnn.pack_padded_sequence(embeddings, lengths, batch_first=True)
        outputs, (hidden, cell) = self.lstm(packed)
        outputs, _ = nn.utils.rnn.pad_packed_sequence(outputs, batch_first=True)
        return outputs, hidden

class AttentionGenerator(nn.Module):
    def __init__(self, text_dim=256, latent_dim=100):
        super().__init__()
        self.text_encoder = TextEncoder(vocab_size=10000)
        
        # Attention mechanism
        self.attention = nn.MultiheadAttention(text_dim, num_heads=8)
        
        # Generator conditioned on text
        self.generator = nn.Sequential(
            nn.Linear(latent_dim + text_dim, 512),
            nn.ReLU(),
            # ... rest of generator
        )
    
    def forward(self, z, captions, lengths):
        text_features, _ = self.text_encoder(captions, lengths)
        
        # Attend to relevant words
        attended_text, _ = self.attention(z.unsqueeze(0), text_features.transpose(0, 1), text_features.transpose(0, 1))
        
        # Generate image
        gen_input = torch.cat([z, attended_text.squeeze(0)], dim=1)
        return self.generator(gen_input)
```

## Data Augmentation with GANs

```python
def augment_dataset_with_gan(generator, original_dataset, n_synthetic=10000):
    synthetic_images = []
    
    generator.eval()
    with torch.no_grad():
        for i in range(n_synthetic):
            z = torch.randn(1, latent_dim)
            fake_img = generator(z)
            synthetic_images.append(fake_img)
    
    # Combine with original dataset
    augmented_dataset = torch.cat([original_dataset, torch.cat(synthetic_images)])
    return augmented_dataset
```
