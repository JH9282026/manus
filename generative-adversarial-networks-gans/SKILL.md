---
name: generative-adversarial-networks-gans
description: "Implement and train Generative Adversarial Networks (GANs) to generate realistic synthetic data. Use for image generation and synthesis, style transfer and image-to-image translation, data augmentation, creating deepfakes and face generation, text-to-image synthesis, super-resolution, video generation, and implementing GAN variants (DCGAN, StyleGAN, CycleGAN, Pix2Pix, Progressive GAN)."
---

# Generative Adversarial Networks (GANs)

Implement and train GANs to generate realistic synthetic data through adversarial training of generator and discriminator networks.

## Overview

This skill provides comprehensive guidance on Generative Adversarial Networks, covering GAN architecture and training dynamics, implementation of classic and modern GAN variants (DCGAN, WGAN, StyleGAN, CycleGAN), training techniques and stability improvements, conditional generation, and applications in image synthesis, style transfer, super-resolution, and data augmentation. GANs enable generation of highly realistic synthetic data by training two neural networks in competition.

## Quick Start: GAN Variant Selection

| Task | GAN Variant | Key Features | Reference |
|------|-------------|--------------|----------|
| Basic image generation | DCGAN | Convolutional architecture, stable training | `/references/gan-architecture.md` |
| High-quality face generation | StyleGAN2/3 | Style-based generator, high resolution | `/references/gan-variants.md` |
| Image-to-image translation | Pix2Pix | Paired data, conditional GAN | `/references/applications-implementations.md` |
| Unpaired style transfer | CycleGAN | Cycle consistency, no paired data needed | `/references/gan-variants.md` |
| Stable training | WGAN-GP | Wasserstein loss, gradient penalty | `/references/training-techniques.md` |
| Conditional generation | cGAN | Class-conditional generation | `/references/gan-architecture.md` |
| Progressive training | Progressive GAN | Gradual resolution increase | `/references/gan-variants.md` |
| Super-resolution | SRGAN, ESRGAN | Perceptual loss, photo-realistic upscaling | `/references/applications-implementations.md` |
| Text-to-image | AttnGAN, DALL-E | Attention mechanisms, text conditioning | `/references/applications-implementations.md` |

## Core Concepts

### GAN Architecture

GANs consist of two neural networks trained adversarially:

**Generator (G)** — Creates synthetic data from random noise
- Input: Random noise vector z ~ p(z) (typically Gaussian)
- Output: Fake sample G(z) that mimics real data distribution
- Goal: Fool discriminator into classifying fake samples as real

**Discriminator (D)** — Distinguishes real from fake data
- Input: Real sample x ~ p_data(x) or fake sample G(z)
- Output: Probability D(x) that input is real
- Goal: Correctly classify real vs fake samples

### Adversarial Training

Minimax game between generator and discriminator:

```
min_G max_D V(D,G) = E_x[log D(x)] + E_z[log(1 - D(G(z)))]
```

**Discriminator objective:** Maximize ability to distinguish real from fake
```
max_D E_x[log D(x)] + E_z[log(1 - D(G(z)))]
```

**Generator objective:** Minimize discriminator's ability to detect fakes
```
min_G E_z[log(1 - D(G(z)))]  # Original formulation
max_G E_z[log D(G(z))]        # Non-saturating alternative (better gradients)
```

### Training Dynamics

1. **Sample real data** x from training set
2. **Sample noise** z from prior distribution
3. **Generate fake data** G(z)
4. **Update discriminator** to maximize classification accuracy
5. **Update generator** to fool discriminator
6. **Repeat** until convergence

**Nash Equilibrium:** Optimal solution where:
- Generator produces samples indistinguishable from real data
- Discriminator outputs 0.5 (cannot distinguish real from fake)

## Basic GAN Implementation

### Vanilla GAN (Fully Connected)

```python
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader

class Generator(nn.Module):
    def __init__(self, latent_dim=100, img_shape=(1, 28, 28)):
        super(Generator, self).__init__()
        self.img_shape = img_shape
        self.model = nn.Sequential(
            nn.Linear(latent_dim, 128),
            nn.LeakyReLU(0.2),
            nn.Linear(128, 256),
            nn.BatchNorm1d(256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 512),
            nn.BatchNorm1d(512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, int(torch.prod(torch.tensor(img_shape)))),
            nn.Tanh()  # Output in [-1, 1]
        )
    
    def forward(self, z):
        img = self.model(z)
        return img.view(img.size(0), *self.img_shape)

class Discriminator(nn.Module):
    def __init__(self, img_shape=(1, 28, 28)):
        super(Discriminator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(int(torch.prod(torch.tensor(img_shape))), 512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, 256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 1),
            nn.Sigmoid()  # Output probability
        )
    
    def forward(self, img):
        img_flat = img.view(img.size(0), -1)
        return self.model(img_flat)

# Training loop
def train_gan(generator, discriminator, dataloader, n_epochs=100, latent_dim=100):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    generator.to(device)
    discriminator.to(device)
    
    # Optimizers
    g_optimizer = optim.Adam(generator.parameters(), lr=0.0002, betas=(0.5, 0.999))
    d_optimizer = optim.Adam(discriminator.parameters(), lr=0.0002, betas=(0.5, 0.999))
    
    # Loss function
    criterion = nn.BCELoss()
    
    for epoch in range(n_epochs):
        for i, (real_imgs, _) in enumerate(dataloader):
            batch_size = real_imgs.size(0)
            real_imgs = real_imgs.to(device)
            
            # Labels
            real_labels = torch.ones(batch_size, 1).to(device)
            fake_labels = torch.zeros(batch_size, 1).to(device)
            
            # ---------------------
            #  Train Discriminator
            # ---------------------
            d_optimizer.zero_grad()
            
            # Real images
            real_output = discriminator(real_imgs)
            d_loss_real = criterion(real_output, real_labels)
            
            # Fake images
            z = torch.randn(batch_size, latent_dim).to(device)
            fake_imgs = generator(z)
            fake_output = discriminator(fake_imgs.detach())
            d_loss_fake = criterion(fake_output, fake_labels)
            
            # Total discriminator loss
            d_loss = d_loss_real + d_loss_fake
            d_loss.backward()
            d_optimizer.step()
            
            # -----------------
            #  Train Generator
            # -----------------
            g_optimizer.zero_grad()
            
            # Generate fake images
            z = torch.randn(batch_size, latent_dim).to(device)
            fake_imgs = generator(z)
            fake_output = discriminator(fake_imgs)
            
            # Generator loss (fool discriminator)
            g_loss = criterion(fake_output, real_labels)
            g_loss.backward()
            g_optimizer.step()
            
            if i % 100 == 0:
                print(f"Epoch [{epoch}/{n_epochs}] Batch [{i}/{len(dataloader)}] "
                      f"D_loss: {d_loss.item():.4f} G_loss: {g_loss.item():.4f}")
```

### Deep Convolutional GAN (DCGAN)

More stable architecture using convolutional layers:

```python
class DCGANGenerator(nn.Module):
    def __init__(self, latent_dim=100, channels=3):
        super(DCGANGenerator, self).__init__()
        self.model = nn.Sequential(
            # Input: latent_dim x 1 x 1
            nn.ConvTranspose2d(latent_dim, 512, 4, 1, 0, bias=False),
            nn.BatchNorm2d(512),
            nn.ReLU(True),
            # State: 512 x 4 x 4
            nn.ConvTranspose2d(512, 256, 4, 2, 1, bias=False),
            nn.BatchNorm2d(256),
            nn.ReLU(True),
            # State: 256 x 8 x 8
            nn.ConvTranspose2d(256, 128, 4, 2, 1, bias=False),
            nn.BatchNorm2d(128),
            nn.ReLU(True),
            # State: 128 x 16 x 16
            nn.ConvTranspose2d(128, 64, 4, 2, 1, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(True),
            # State: 64 x 32 x 32
            nn.ConvTranspose2d(64, channels, 4, 2, 1, bias=False),
            nn.Tanh()
            # Output: channels x 64 x 64
        )
    
    def forward(self, z):
        return self.model(z.view(z.size(0), z.size(1), 1, 1))

class DCGANDiscriminator(nn.Module):
    def __init__(self, channels=3):
        super(DCGANDiscriminator, self).__init__()
        self.model = nn.Sequential(
            # Input: channels x 64 x 64
            nn.Conv2d(channels, 64, 4, 2, 1, bias=False),
            nn.LeakyReLU(0.2, inplace=True),
            # State: 64 x 32 x 32
            nn.Conv2d(64, 128, 4, 2, 1, bias=False),
            nn.BatchNorm2d(128),
            nn.LeakyReLU(0.2, inplace=True),
            # State: 128 x 16 x 16
            nn.Conv2d(128, 256, 4, 2, 1, bias=False),
            nn.BatchNorm2d(256),
            nn.LeakyReLU(0.2, inplace=True),
            # State: 256 x 8 x 8
            nn.Conv2d(256, 512, 4, 2, 1, bias=False),
            nn.BatchNorm2d(512),
            nn.LeakyReLU(0.2, inplace=True),
            # State: 512 x 4 x 4
            nn.Conv2d(512, 1, 4, 1, 0, bias=False),
            nn.Sigmoid()
            # Output: 1 x 1 x 1
        )
    
    def forward(self, img):
        return self.model(img).view(-1, 1)
```

**DCGAN Guidelines:**
- Replace pooling with strided convolutions (discriminator) and transposed convolutions (generator)
- Use batch normalization in both networks
- Remove fully connected hidden layers
- Use ReLU in generator (except output: Tanh)
- Use LeakyReLU in discriminator

## Conditional GAN (cGAN)

Generate samples conditioned on class labels:

```python
class ConditionalGenerator(nn.Module):
    def __init__(self, latent_dim=100, n_classes=10, img_shape=(1, 28, 28)):
        super(ConditionalGenerator, self).__init__()
        self.label_embedding = nn.Embedding(n_classes, n_classes)
        self.img_shape = img_shape
        
        self.model = nn.Sequential(
            nn.Linear(latent_dim + n_classes, 128),
            nn.LeakyReLU(0.2),
            nn.Linear(128, 256),
            nn.BatchNorm1d(256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 512),
            nn.BatchNorm1d(512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, int(torch.prod(torch.tensor(img_shape)))),
            nn.Tanh()
        )
    
    def forward(self, z, labels):
        # Concatenate noise and label embedding
        label_input = self.label_embedding(labels)
        gen_input = torch.cat([z, label_input], dim=1)
        img = self.model(gen_input)
        return img.view(img.size(0), *self.img_shape)

class ConditionalDiscriminator(nn.Module):
    def __init__(self, n_classes=10, img_shape=(1, 28, 28)):
        super(ConditionalDiscriminator, self).__init__()
        self.label_embedding = nn.Embedding(n_classes, n_classes)
        
        self.model = nn.Sequential(
            nn.Linear(int(torch.prod(torch.tensor(img_shape))) + n_classes, 512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, 256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 1),
            nn.Sigmoid()
        )
    
    def forward(self, img, labels):
        # Concatenate image and label embedding
        img_flat = img.view(img.size(0), -1)
        label_input = self.label_embedding(labels)
        d_input = torch.cat([img_flat, label_input], dim=1)
        return self.model(d_input)

# Generate specific class
z = torch.randn(16, 100)
labels = torch.tensor([3] * 16)  # Generate digit '3'
generated_images = generator(z, labels)
```

## Training Techniques

### Label Smoothing

```python
# Instead of hard labels (0, 1), use soft labels
real_labels = torch.ones(batch_size, 1) * 0.9  # 0.9 instead of 1.0
fake_labels = torch.zeros(batch_size, 1) + 0.1  # 0.1 instead of 0.0
```

### One-Sided Label Smoothing

```python
# Only smooth real labels (more stable)
real_labels = torch.rand(batch_size, 1) * 0.1 + 0.9  # [0.9, 1.0]
fake_labels = torch.zeros(batch_size, 1)  # 0.0
```

### Noisy Labels

```python
# Occasionally flip labels (5% of time)
if np.random.random() < 0.05:
    real_labels, fake_labels = fake_labels, real_labels
```

### Feature Matching

```python
# Match statistics of intermediate discriminator features
def feature_matching_loss(real_imgs, fake_imgs, discriminator):
    # Extract features from intermediate layer
    real_features = discriminator.get_features(real_imgs)
    fake_features = discriminator.get_features(fake_imgs)
    return torch.mean((real_features.mean(0) - fake_features.mean(0)) ** 2)
```

## Using the Reference Files

### When to Read Each Reference

**`/references/gan-architecture.md`** — Read when understanding GAN fundamentals, implementing basic GANs, learning about generator and discriminator architectures, or working with conditional GANs.

**`/references/training-techniques.md`** — Read when facing training instability, implementing advanced loss functions (WGAN, LSGAN), applying regularization techniques, or debugging mode collapse and convergence issues.

**`/references/gan-variants.md`** — Read when implementing specific GAN variants (StyleGAN, CycleGAN, Progressive GAN), working on style transfer, or generating high-resolution images.

**`/references/applications-implementations.md`** — Read when applying GANs to specific tasks (image-to-image translation, super-resolution, text-to-image), implementing Pix2Pix or SRGAN, or working on data augmentation and practical applications.
