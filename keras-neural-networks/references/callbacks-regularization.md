# Keras Callbacks and Regularization

## Overview

Keras provides powerful mechanisms for controlling and enhancing the training process through callbacks and regularization techniques. Callbacks enable automated actions at various stages of training, while regularization prevents overfitting and improves model generalization. This guide covers both built-in and custom implementations of these essential tools.

## Keras Callbacks

### What are Callbacks?

Callbacks are objects that can perform actions at various stages of training, such as:

- At the start or end of an epoch
- Before or after processing a batch
- At the start or end of training

Callbacks enable:
- **Automation**: Perform actions without manual intervention
- **Monitoring**: Track training progress and metrics
- **Control**: Modify training behavior dynamically
- **Optimization**: Improve resource usage and efficiency

### Using Callbacks

Callbacks are passed to the `fit()` method:

```python
history = model.fit(
    x_train, y_train,
    epochs=50,
    validation_data=(x_val, y_val),
    callbacks=[callback1, callback2, callback3]
)
```

Multiple callbacks can be used simultaneously by passing a list.

## Built-in Keras Callbacks

### 1. ModelCheckpoint

**Purpose**: Save model or weights periodically or when performance improves.

#### Why ModelCheckpoint?

- **Long Training**: Preserve progress in case of interruption
- **Best Model**: Save model with best validation performance
- **Prevent Overfitting**: Keep model from epoch with best generalization
- **Experimentation**: Compare models from different epochs

#### Basic Usage

```python
from keras.callbacks import ModelCheckpoint

checkpoint = ModelCheckpoint(
    filepath='model_checkpoint.keras',
    monitor='val_loss',
    save_best_only=True,
    mode='min',
    verbose=1
)

model.fit(x_train, y_train, callbacks=[checkpoint])
```

#### Advanced Configuration

```python
checkpoint = ModelCheckpoint(
    filepath='models/model_epoch_{epoch:02d}_val_acc_{val_accuracy:.4f}.keras',
    monitor='val_accuracy',
    save_best_only=True,
    save_weights_only=False,  # Save entire model
    mode='max',               # Maximize val_accuracy
    save_freq='epoch',        # Save every epoch (if best)
    verbose=1
)
```

#### Key Parameters

- **filepath**: Path to save model (can include formatting for epoch/metrics)
- **monitor**: Metric to monitor (e.g., 'val_loss', 'val_accuracy')
- **save_best_only**: Only save when monitored metric improves
- **save_weights_only**: Save only weights (True) or entire model (False)
- **mode**: 'min' (for loss) or 'max' (for accuracy)
- **verbose**: 0 (silent) or 1 (messages)

#### Best Practices

- Monitor validation metrics, not training metrics
- Use `save_best_only=True` to avoid saving every epoch
- Include epoch and metric values in filename for tracking
- Save entire model (not just weights) for easier deployment
- Ensure sufficient disk space for checkpoints

### 2. EarlyStopping

**Purpose**: Stop training when monitored metric stops improving.

#### Why EarlyStopping?

- **Prevent Overfitting**: Stop before model starts overfitting
- **Save Time**: Avoid unnecessary training epochs
- **Automatic**: No need to manually monitor and stop
- **Resource Efficiency**: Free up computational resources

#### Basic Usage

```python
from keras.callbacks import EarlyStopping

early_stop = EarlyStopping(
    monitor='val_loss',
    patience=10,
    verbose=1
)

model.fit(x_train, y_train, callbacks=[early_stop])
```

#### Advanced Configuration

```python
early_stop = EarlyStopping(
    monitor='val_loss',
    min_delta=0.001,          # Minimum change to qualify as improvement
    patience=15,              # Epochs to wait before stopping
    mode='min',
    restore_best_weights=True, # Restore weights from best epoch
    verbose=1,
    baseline=None             # Stop if metric doesn't reach baseline
)
```

#### Key Parameters

- **monitor**: Metric to track
- **patience**: Number of epochs with no improvement before stopping
- **min_delta**: Minimum change to count as improvement
- **mode**: 'min' or 'max'
- **restore_best_weights**: Restore model to best epoch (highly recommended)
- **baseline**: Minimum acceptable value for metric

#### Best Practices

- Set patience based on learning rate schedule (higher patience for scheduled LR)
- Always use `restore_best_weights=True`
- Combine with ModelCheckpoint for safety
- Monitor validation metrics
- Set reasonable `min_delta` to avoid stopping on noise

#### Combining with ModelCheckpoint

```python
checkpoint = ModelCheckpoint('best_model.keras', save_best_only=True, monitor='val_loss')
early_stop = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

model.fit(x_train, y_train, callbacks=[checkpoint, early_stop])
```

### 3. ReduceLROnPlateau

**Purpose**: Reduce learning rate when metric plateaus.

#### Why ReduceLROnPlateau?

- **Escape Plateaus**: Lower LR helps optimizer find better minima
- **Fine-Tuning**: Smaller steps for precise optimization
- **Automatic**: No manual LR adjustment needed
- **Improved Convergence**: Often leads to better final performance

#### Basic Usage

```python
from keras.callbacks import ReduceLROnPlateau

reduce_lr = ReduceLROnPlateau(
    monitor='val_loss',
    factor=0.2,
    patience=5,
    min_lr=1e-7,
    verbose=1
)

model.fit(x_train, y_train, callbacks=[reduce_lr])
```

#### Advanced Configuration

```python
reduce_lr = ReduceLROnPlateau(
    monitor='val_loss',
    factor=0.5,              # Reduce LR by 50%
    patience=5,              # Wait 5 epochs
    min_delta=0.0001,        # Minimum improvement
    cooldown=2,              # Epochs to wait before resuming normal operation
    min_lr=1e-7,             # Minimum learning rate
    mode='min',
    verbose=1
)
```

#### Key Parameters

- **monitor**: Metric to watch
- **factor**: Factor by which to reduce LR (new_lr = lr * factor)
- **patience**: Epochs with no improvement before reducing
- **min_lr**: Lower bound for learning rate
- **min_delta**: Threshold for measuring improvement
- **cooldown**: Epochs to wait before resuming monitoring
- **mode**: 'min' or 'max'

#### Best Practices

- Set patience to allow time for optimization at current LR
- Use factor between 0.1 and 0.5 (commonly 0.2 or 0.5)
- Set reasonable min_lr to prevent infinitesimally small rates
- Monitor validation metrics
- Can combine with learning rate schedules

### 4. TensorBoard

**Purpose**: Log metrics and visualizations for TensorBoard.

#### Basic Usage

```python
from keras.callbacks import TensorBoard
import datetime

log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = TensorBoard(
    log_dir=log_dir,
    histogram_freq=1,
    write_graph=True,
    write_images=True
)

model.fit(x_train, y_train, callbacks=[tensorboard_callback])
```

#### Viewing in TensorBoard

```bash
tensorboard --logdir=logs/fit
```

Then open browser to http://localhost:6006

#### What TensorBoard Shows

- **Scalars**: Loss and metrics over time
- **Graphs**: Model architecture visualization
- **Histograms**: Weight and bias distributions
- **Images**: Input images and predictions
- **Embeddings**: High-dimensional data visualization

### 5. CSVLogger

**Purpose**: Stream epoch results to CSV file.

```python
from keras.callbacks import CSVLogger

csv_logger = CSVLogger('training_log.csv', append=True)
model.fit(x_train, y_train, callbacks=[csv_logger])
```

**Use Cases**:
- Simple logging without TensorBoard
- Easy analysis in spreadsheets
- Lightweight alternative to TensorBoard

### 6. LearningRateScheduler

**Purpose**: Apply custom learning rate schedule.

```python
from keras.callbacks import LearningRateScheduler
import numpy as np

def scheduler(epoch, lr):
    if epoch < 10:
        return lr
    else:
        return lr * np.exp(-0.1)

lr_scheduler = LearningRateScheduler(scheduler, verbose=1)
model.fit(x_train, y_train, callbacks=[lr_scheduler])
```

### 7. TerminateOnNaN

**Purpose**: Stop training if loss becomes NaN.

```python
from keras.callbacks import TerminateOnNaN

model.fit(x_train, y_train, callbacks=[TerminateOnNaN()])
```

**When to Use**:
- Debugging training instabilities
- Preventing wasted computation on failed runs
- Hyperparameter search

## Custom Callbacks

### Creating Custom Callbacks

Create custom callbacks by subclassing `keras.callbacks.Callback`:

```python
import keras

class CustomCallback(keras.callbacks.Callback):
    def on_train_begin(self, logs=None):
        print("Training is starting")
    
    def on_train_end(self, logs=None):
        print("Training has ended")
    
    def on_epoch_begin(self, epoch, logs=None):
        print(f"Epoch {epoch} is starting")
    
    def on_epoch_end(self, epoch, logs=None):
        print(f"Epoch {epoch} ended. Loss: {logs['loss']:.4f}")
    
    def on_batch_begin(self, batch, logs=None):
        pass  # Called before each batch
    
    def on_batch_end(self, batch, logs=None):
        pass  # Called after each batch
```

### Available Callback Methods

**Training Level**:
- `on_train_begin(logs)`: Called at start of training
- `on_train_end(logs)`: Called at end of training

**Epoch Level**:
- `on_epoch_begin(epoch, logs)`: Called at start of epoch
- `on_epoch_end(epoch, logs)`: Called at end of epoch

**Batch Level**:
- `on_batch_begin(batch, logs)`: Called before processing batch
- `on_batch_end(batch, logs)`: Called after processing batch

**Prediction/Test**:
- `on_predict_begin(logs)`: Called at start of prediction
- `on_predict_end(logs)`: Called at end of prediction
- `on_test_begin(logs)`: Called at start of evaluation
- `on_test_end(logs)`: Called at end of evaluation

### Example: Custom Metric Logger

```python
class MetricLogger(keras.callbacks.Callback):
    def __init__(self):
        self.metrics = []
    
    def on_epoch_end(self, epoch, logs=None):
        self.metrics.append({
            'epoch': epoch,
            'loss': logs['loss'],
            'accuracy': logs.get('accuracy'),
            'val_loss': logs.get('val_loss'),
            'val_accuracy': logs.get('val_accuracy')
        })
        
        # Print summary every 10 epochs
        if (epoch + 1) % 10 == 0:
            print(f"\nEpoch {epoch + 1} Summary:")
            print(f"  Train Loss: {logs['loss']:.4f}")
            print(f"  Val Loss: {logs.get('val_loss', 'N/A')}")
```

### Example: Learning Rate Warmup

```python
class WarmUpLearningRate(keras.callbacks.Callback):
    def __init__(self, warmup_epochs=5, initial_lr=1e-6, target_lr=1e-3):
        super().__init__()
        self.warmup_epochs = warmup_epochs
        self.initial_lr = initial_lr
        self.target_lr = target_lr
    
    def on_epoch_begin(self, epoch, logs=None):
        if epoch < self.warmup_epochs:
            lr = self.initial_lr + (self.target_lr - self.initial_lr) * (epoch / self.warmup_epochs)
            keras.backend.set_value(self.model.optimizer.learning_rate, lr)
            print(f"\nEpoch {epoch}: Learning rate is {lr:.6f}")
```

## Regularization in Keras

### What is Regularization?

Regularization techniques prevent overfitting by:
- Adding constraints to the model
- Reducing model complexity
- Improving generalization to unseen data

### Types of Regularization

#### 1. L1 and L2 Regularization

**L1 Regularization (Lasso)**:
- Adds sum of absolute values of weights to loss
- Promotes sparsity (many weights become exactly zero)
- Feature selection effect

**L2 Regularization (Ridge)**:
- Adds sum of squared weights to loss
- Encourages small weights
- Prevents any single weight from dominating
- Most common regularization

**Implementation**:

```python
from keras import regularizers
from keras.layers import Dense

# L1 regularization
layer = Dense(64, activation='relu',
              kernel_regularizer=regularizers.L1(0.01))

# L2 regularization
layer = Dense(64, activation='relu',
              kernel_regularizer=regularizers.L2(0.01))

# L1 + L2 (Elastic Net)
layer = Dense(64, activation='relu',
              kernel_regularizer=regularizers.L1L2(l1=0.01, l2=0.01))

# Bias regularization
layer = Dense(64, activation='relu',
              kernel_regularizer=regularizers.L2(0.01),
              bias_regularizer=regularizers.L2(0.01))
```

**Choosing Regularization Strength**:
- Start with small values (0.001 to 0.01)
- Increase if still overfitting
- Decrease if underfitting
- Use validation set to tune

#### 2. Dropout Layers

Covered in detail in training optimization guide. Quick reference:

```python
from keras.layers import Dropout, SpatialDropout2D, GaussianDropout

# Standard dropout
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))

# Spatial dropout for CNNs
model.add(Conv2D(64, 3, activation='relu'))
model.add(SpatialDropout2D(0.2))

# Gaussian dropout
model.add(Dense(64, activation='relu'))
model.add(GaussianDropout(0.3))
```

#### 3. Batch Normalization

While primarily for training stability, BatchNorm also has regularization effects:

```python
from keras.layers import BatchNormalization

model.add(Dense(64))
model.add(BatchNormalization())
model.add(Activation('relu'))
```

#### 4. Activity Regularization

**Purpose**: Regularize layer outputs (activations) instead of weights.

```python
from keras.layers import ActivityRegularization

model.add(Dense(64, activation='relu'))
model.add(ActivityRegularization(l1=0.01, l2=0.01))
```

**When to Use**:
- Sparse representations desired
- Autoencoders
- Feature learning

#### 5. Gaussian Noise

**Purpose**: Add Gaussian noise to inputs for robustness.

```python
from keras.layers import GaussianNoise

model.add(GaussianNoise(0.1))  # stddev=0.1
model.add(Dense(64, activation='relu'))
```

**Benefits**:
- Improves robustness to input noise
- Acts as regularization
- Useful for denoising autoencoders

### Custom Regularization

#### Custom Regularizer Class

```python
import keras

class CustomRegularizer(keras.regularizers.Regularizer):
    def __init__(self, strength=0.01):
        self.strength = strength
    
    def __call__(self, x):
        # Custom penalty: sum of absolute values
        return self.strength * keras.ops.sum(keras.ops.abs(x))
    
    def get_config(self):
        return {'strength': self.strength}

# Use custom regularizer
layer = Dense(64, kernel_regularizer=CustomRegularizer(0.01))
```

#### Dynamic Regularization with Callbacks

Change regularization strength during training:

```python
class DynamicRegularization(keras.callbacks.Callback):
    def __init__(self, layer_name, initial_strength=0.01, decay=0.9):
        super().__init__()
        self.layer_name = layer_name
        self.strength = initial_strength
        self.decay = decay
    
    def on_epoch_end(self, epoch, logs=None):
        # Decay regularization strength
        self.strength *= self.decay
        
        # Update regularizer in target layer
        for layer in self.model.layers:
            if layer.name == self.layer_name:
                if hasattr(layer, 'kernel_regularizer'):
                    # Update regularizer strength
                    # (Implementation depends on regularizer type)
                    pass
```

### Regularization Best Practices

**1. Start Simple**:
- Begin without regularization
- Add if overfitting occurs
- Start with small regularization strength

**2. Combine Techniques**:
- Dropout + L2 regularization
- Batch Normalization + Dropout
- Data augmentation + regularization

**3. Monitor Validation Performance**:
- Track train vs. validation metrics
- Adjust regularization based on gap
- Use callbacks for automatic adjustment

**4. Layer-Specific Regularization**:
- Apply stronger regularization to larger layers
- Less regularization on final layers
- Experiment with different strengths per layer

**5. Validation Loss Includes Regularization**:
- Keras adds regularization term to reported loss
- Account for this when comparing losses
- Regularization only applied during training

## Callback and Regularization Strategies

### Strategy 1: Comprehensive Training Setup

```python
from keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau, TensorBoard
from keras import regularizers
import datetime

# Build model with regularization
model = Sequential([
    Dense(128, activation='relu', 
          kernel_regularizer=regularizers.L2(0.01),
          input_shape=(input_dim,)),
    Dropout(0.5),
    BatchNormalization(),
    Dense(64, activation='relu',
          kernel_regularizer=regularizers.L2(0.01)),
    Dropout(0.3),
    Dense(num_classes, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Setup callbacks
checkpoint = ModelCheckpoint('best_model.keras', save_best_only=True, monitor='val_loss')
early_stop = EarlyStopping(monitor='val_loss', patience=15, restore_best_weights=True)
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=5, min_lr=1e-7)
tensorboard = TensorBoard(log_dir=f"logs/{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}")

# Train
history = model.fit(
    x_train, y_train,
    validation_data=(x_val, y_val),
    epochs=100,
    batch_size=32,
    callbacks=[checkpoint, early_stop, reduce_lr, tensorboard]
)
```

### Strategy 2: Progressive Regularization

Start with light regularization and increase if needed:

```python
class ProgressiveRegularization(keras.callbacks.Callback):
    def __init__(self, target_layer_names, initial_strength=0.001, max_strength=0.1):
        super().__init__()
        self.target_layer_names = target_layer_names
        self.initial_strength = initial_strength
        self.max_strength = max_strength
        self.best_val_loss = float('inf')
        self.patience_counter = 0
    
    def on_epoch_end(self, epoch, logs=None):
        val_loss = logs.get('val_loss')
        
        if val_loss < self.best_val_loss:
            self.best_val_loss = val_loss
            self.patience_counter = 0
        else:
            self.patience_counter += 1
        
        # Increase regularization if validation loss not improving
        if self.patience_counter >= 5:
            # Increase regularization strength
            # (Implementation would modify layer regularizers)
            print(f"\nIncreasing regularization strength at epoch {epoch}")
            self.patience_counter = 0
```

## Key Takeaways

1. **ModelCheckpoint**: Essential for saving best model during training
2. **EarlyStopping**: Prevents overfitting and saves time; always use `restore_best_weights=True`
3. **ReduceLROnPlateau**: Automatic learning rate adjustment for better convergence
4. **TensorBoard**: Powerful visualization for monitoring training
5. **Custom Callbacks**: Create specialized training control logic
6. **L1/L2 Regularization**: Add to layer definitions to prevent overfitting
7. **Dropout**: Effective regularization; use rates of 0.2-0.5
8. **Combine Techniques**: Use multiple callbacks and regularization methods together
9. **Monitor Validation**: Always track validation metrics for regularization tuning
10. **Start Simple**: Add complexity (callbacks/regularization) as needed

## References

- Keras Callbacks API: https://keras.io/api/callbacks/
- Keras Regularizers: https://keras.io/api/layers/regularizers/
- Keras Regularization Layers: https://keras.io/api/layers/regularization_layers/
- Dropout Paper: http://jmlr.org/papers/v15/srivastava14a.html
- Batch Normalization Paper: https://arxiv.org/abs/1502.03167
