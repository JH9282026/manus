# GAN Architecture

Fundamental GAN architectures, generator and discriminator design, and conditional GANs.

---

## Generator Architecture

The generator creates synthetic data from random noise.

### Fully Connected Generator

```python
class FCGenerator(nn.Module):
    def __init__(self, latent_dim=100, output_dim=784):
        super(FCGenerator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(latent_dim, 256),
            nn.LeakyReLU(0.2),
            nn.BatchNorm1d(256),
            nn.Linear(256, 512),
            nn.LeakyReLU(0.2),
            nn.BatchNorm1d(512),
            nn.Linear(512, 1024),
            nn.LeakyReLU(0.2),
            nn.BatchNorm1d(1024),
            nn.Linear(1024, output_dim),
            nn.Tanh()
        )
    
    def forward(self, z):
        return self.model(z)
```

### Convolutional Generator (DCGAN)

```python
class ConvGenerator(nn.Module):
    def __init__(self, latent_dim=100, channels=3, feature_maps=64):
        super(ConvGenerator, self).__init__()
        self.model = nn.Sequential(
            nn.ConvTranspose2d(latent_dim, feature_maps * 8, 4, 1, 0, bias=False),
            nn.BatchNorm2d(feature_maps * 8),
            nn.ReLU(True),
            
            nn.ConvTranspose2d(feature_maps * 8, feature_maps * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(feature_maps * 4),
            nn.ReLU(True),
            
            nn.ConvTranspose2d(feature_maps * 4, feature_maps * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(feature_maps * 2),
            nn.ReLU(True),
            
            nn.ConvTranspose2d(feature_maps * 2, feature_maps, 4, 2, 1, bias=False),
            nn.BatchNorm2d(feature_maps),
            nn.ReLU(True),
            
            nn.ConvTranspose2d(feature_maps, channels, 4, 2, 1, bias=False),
            nn.Tanh()
        )
    
    def forward(self, z):
        return self.model(z.view(z.size(0), z.size(1), 1, 1))
```

---

## Discriminator Architecture

The discriminator classifies inputs as real or fake.

### Fully Connected Discriminator

```python
class FCDiscriminator(nn.Module):
    def __init__(self, input_dim=784):
        super(FCDiscriminator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(input_dim, 512),
            nn.LeakyReLU(0.2),
            nn.Dropout(0.3),
            nn.Linear(512, 256),
            nn.LeakyReLU(0.2),
            nn.Dropout(0.3),
            nn.Linear(256, 1),
            nn.Sigmoid()
        )
    
    def forward(self, x):
        return self.model(x.view(x.size(0), -1))
```

### Convolutional Discriminator (DCGAN)

```python
class ConvDiscriminator(nn.Module):
    def __init__(self, channels=3, feature_maps=64):
        super(ConvDiscriminator, self).__init__()
        self.model = nn.Sequential(
            nn.Conv2d(channels, feature_maps, 4, 2, 1, bias=False),
            nn.LeakyReLU(0.2, inplace=True),
            
            nn.Conv2d(feature_maps, feature_maps * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(feature_maps * 2),
            nn.LeakyReLU(0.2, inplace=True),
            
            nn.Conv2d(feature_maps * 2, feature_maps * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(feature_maps * 4),
            nn.LeakyReLU(0.2, inplace=True),
            
            nn.Conv2d(feature_maps * 4, feature_maps * 8, 4, 2, 1, bias=False),
            nn.BatchNorm2d(feature_maps * 8),
            nn.LeakyReLU(0.2, inplace=True),
            
            nn.Conv2d(feature_maps * 8, 1, 4, 1, 0, bias=False),
            nn.Sigmoid()
        )
    
    def forward(self, x):
        return self.model(x).view(-1, 1)
```

---

## Conditional GAN

Generate samples conditioned on additional information (class labels, text, etc.).

### Class-Conditional GAN

```python
class ConditionalGenerator(nn.Module):
    def __init__(self, latent_dim=100, n_classes=10, embed_dim=50, channels=1):
        super(ConditionalGenerator, self).__init__()
        self.label_embedding = nn.Embedding(n_classes, embed_dim)
        
        self.model = nn.Sequential(
            nn.Linear(latent_dim + embed_dim, 256),
            nn.LeakyReLU(0.2),
            nn.BatchNorm1d(256),
            nn.Linear(256, 512),
            nn.LeakyReLU(0.2),
            nn.BatchNorm1d(512),
            nn.Linear(512, 1024),
            nn.LeakyReLU(0.2),
            nn.BatchNorm1d(1024),
            nn.Linear(1024, channels * 28 * 28),
            nn.Tanh()
        )
    
    def forward(self, z, labels):
        label_embed = self.label_embedding(labels)
        gen_input = torch.cat([z, label_embed], dim=1)
        img = self.model(gen_input)
        return img.view(img.size(0), channels, 28, 28)

class ConditionalDiscriminator(nn.Module):
    def __init__(self, n_classes=10, embed_dim=50, channels=1):
        super(ConditionalDiscriminator, self).__init__()
        self.label_embedding = nn.Embedding(n_classes, embed_dim)
        
        self.model = nn.Sequential(
            nn.Linear(channels * 28 * 28 + embed_dim, 512),
            nn.LeakyReLU(0.2),
            nn.Dropout(0.3),
            nn.Linear(512, 256),
            nn.LeakyReLU(0.2),
            nn.Dropout(0.3),
            nn.Linear(256, 1),
            nn.Sigmoid()
        )
    
    def forward(self, img, labels):
        img_flat = img.view(img.size(0), -1)
        label_embed = self.label_embedding(labels)
        d_input = torch.cat([img_flat, label_embed], dim=1)
        return self.model(d_input)
```

### Projection-Based Conditional Discriminator

More efficient conditioning method:

```python
class ProjectionDiscriminator(nn.Module):
    def __init__(self, n_classes=10, channels=3, feature_maps=64):
        super(ProjectionDiscriminator, self).__init__()
        
        # Feature extractor
        self.features = nn.Sequential(
            nn.Conv2d(channels, feature_maps, 4, 2, 1),
            nn.LeakyReLU(0.2),
            nn.Conv2d(feature_maps, feature_maps * 2, 4, 2, 1),
            nn.BatchNorm2d(feature_maps * 2),
            nn.LeakyReLU(0.2),
            nn.Conv2d(feature_maps * 2, feature_maps * 4, 4, 2, 1),
            nn.BatchNorm2d(feature_maps * 4),
            nn.LeakyReLU(0.2),
            nn.Conv2d(feature_maps * 4, feature_maps * 8, 4, 2, 1),
            nn.BatchNorm2d(feature_maps * 8),
            nn.LeakyReLU(0.2)
        )
        
        # Unconditional output
        self.fc = nn.Linear(feature_maps * 8 * 4 * 4, 1)
        
        # Label embedding for projection
        self.label_embedding = nn.Embedding(n_classes, feature_maps * 8 * 4 * 4)
    
    def forward(self, img, labels):
        features = self.features(img)
        features_flat = features.view(features.size(0), -1)
        
        # Unconditional score
        output = self.fc(features_flat)
        
        # Projection: inner product with label embedding
        label_embed = self.label_embedding(labels)
        projection = torch.sum(features_flat * label_embed, dim=1, keepdim=True)
        
        return output + projection
```

---

## Auxiliary Classifier GAN (AC-GAN)

Discriminator also predicts class labels:

```python
class ACGANDiscriminator(nn.Module):
    def __init__(self, n_classes=10, channels=3, feature_maps=64):
        super(ACGANDiscriminator, self).__init__()
        
        # Shared feature extractor
        self.features = nn.Sequential(
            nn.Conv2d(channels, feature_maps, 4, 2, 1),
            nn.LeakyReLU(0.2),
            nn.Conv2d(feature_maps, feature_maps * 2, 4, 2, 1),
            nn.BatchNorm2d(feature_maps * 2),
            nn.LeakyReLU(0.2),
            nn.Conv2d(feature_maps * 2, feature_maps * 4, 4, 2, 1),
            nn.BatchNorm2d(feature_maps * 4),
            nn.LeakyReLU(0.2),
            nn.Conv2d(feature_maps * 4, feature_maps * 8, 4, 2, 1),
            nn.BatchNorm2d(feature_maps * 8),
            nn.LeakyReLU(0.2)
        )
        
        # Real/fake classification
        self.adv_layer = nn.Sequential(
            nn.Linear(feature_maps * 8 * 4 * 4, 1),
            nn.Sigmoid()
        )
        
        # Class classification
        self.aux_layer = nn.Sequential(
            nn.Linear(feature_maps * 8 * 4 * 4, n_classes),
            nn.Softmax(dim=1)
        )
    
    def forward(self, img):
        features = self.features(img)
        features_flat = features.view(features.size(0), -1)
        
        validity = self.adv_layer(features_flat)
        label = self.aux_layer(features_flat)
        
        return validity, label

# Training with AC-GAN
def train_acgan_step(real_imgs, labels, generator, discriminator, 
                      g_optimizer, d_optimizer, latent_dim=100):
    batch_size = real_imgs.size(0)
    device = real_imgs.device
    
    # Adversarial and auxiliary losses
    adversarial_loss = nn.BCELoss()
    auxiliary_loss = nn.CrossEntropyLoss()
    
    # Train Discriminator
    d_optimizer.zero_grad()
    
    # Real images
    real_validity, real_pred_labels = discriminator(real_imgs)
    d_real_loss = (adversarial_loss(real_validity, torch.ones(batch_size, 1).to(device)) +
                   auxiliary_loss(real_pred_labels, labels))
    
    # Fake images
    z = torch.randn(batch_size, latent_dim).to(device)
    gen_labels = torch.randint(0, 10, (batch_size,)).to(device)
    fake_imgs = generator(z, gen_labels)
    fake_validity, fake_pred_labels = discriminator(fake_imgs.detach())
    d_fake_loss = (adversarial_loss(fake_validity, torch.zeros(batch_size, 1).to(device)) +
                   auxiliary_loss(fake_pred_labels, gen_labels))
    
    d_loss = (d_real_loss + d_fake_loss) / 2
    d_loss.backward()
    d_optimizer.step()
    
    # Train Generator
    g_optimizer.zero_grad()
    
    fake_validity, fake_pred_labels = discriminator(fake_imgs)
    g_loss = (adversarial_loss(fake_validity, torch.ones(batch_size, 1).to(device)) +
              auxiliary_loss(fake_pred_labels, gen_labels))
    
    g_loss.backward()
    g_optimizer.step()
    
    return d_loss.item(), g_loss.item()
```

---

## InfoGAN

Learn interpretable latent representations:

```python
class InfoGANGenerator(nn.Module):
    def __init__(self, latent_dim=62, code_dim=10, channels=1):
        super(InfoGANGenerator, self).__init__()
        input_dim = latent_dim + code_dim
        
        self.model = nn.Sequential(
            nn.Linear(input_dim, 256),
            nn.LeakyReLU(0.2),
            nn.BatchNorm1d(256),
            nn.Linear(256, 512),
            nn.LeakyReLU(0.2),
            nn.BatchNorm1d(512),
            nn.Linear(512, 1024),
            nn.LeakyReLU(0.2),
            nn.BatchNorm1d(1024),
            nn.Linear(1024, channels * 28 * 28),
            nn.Tanh()
        )
    
    def forward(self, z, code):
        gen_input = torch.cat([z, code], dim=1)
        img = self.model(gen_input)
        return img.view(img.size(0), channels, 28, 28)

class InfoGANDiscriminator(nn.Module):
    def __init__(self, code_dim=10, channels=1):
        super(InfoGANDiscriminator, self).__init__()
        
        # Shared layers
        self.shared = nn.Sequential(
            nn.Linear(channels * 28 * 28, 1024),
            nn.LeakyReLU(0.2),
            nn.Dropout(0.3),
            nn.Linear(1024, 512),
            nn.LeakyReLU(0.2),
            nn.Dropout(0.3)
        )
        
        # Discriminator head
        self.adv_layer = nn.Sequential(
            nn.Linear(512, 1),
            nn.Sigmoid()
        )
        
        # Q network (predicts latent code)
        self.q_layer = nn.Sequential(
            nn.Linear(512, 128),
            nn.LeakyReLU(0.2),
            nn.Linear(128, code_dim)
        )
    
    def forward(self, img):
        img_flat = img.view(img.size(0), -1)
        shared_out = self.shared(img_flat)
        
        validity = self.adv_layer(shared_out)
        code_pred = self.q_layer(shared_out)
        
        return validity, code_pred

# Mutual information loss
def mutual_info_loss(code, code_pred):
    # For discrete codes: cross-entropy
    # For continuous codes: MSE
    return nn.MSELoss()(code_pred, code)
```
