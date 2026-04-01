# Webpack Development Server and Hot Module Replacement

## Introduction

Webpack Dev Server provides a development environment with live reloading, Hot Module Replacement (HMR), and other features that streamline the development workflow. This guide covers configuration, HMR implementation, and best practices for an efficient development experience.

## Webpack Dev Server

### What is Webpack Dev Server?

Webpack Dev Server is a development server that:
- Serves bundled files from memory (not disk)
- Provides live reloading on file changes
- Supports Hot Module Replacement
- Offers proxy capabilities for API requests
- Enables HTTPS for local development
- Provides overlay for compilation errors

### Installation

```bash
npm install --save-dev webpack-dev-server
```

### Basic Configuration

**webpack.config.js**:
```javascript
const path = require('path');

module.exports = {
  mode: 'development',
  entry: './src/index.js',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist'),
    publicPath: '/'  // Important for dev server
  },
  devServer: {
    static: {
      directory: path.join(__dirname, 'public')
    },
    port: 3000,
    open: true,  // Open browser automatically
    hot: true    // Enable HMR (default in v4+)
  }
};
```

**package.json**:
```json
{
  "scripts": {
    "start": "webpack serve --mode development",
    "build": "webpack --mode production"
  }
}
```

**Running**:
```bash
npm start
```

### Advanced Configuration

#### Static File Serving

**Single Directory**:
```javascript
module.exports = {
  devServer: {
    static: {
      directory: path.join(__dirname, 'public'),
      publicPath: '/assets',
      watch: true
    }
  }
};
```

**Multiple Directories**:
```javascript
module.exports = {
  devServer: {
    static: [
      {
        directory: path.join(__dirname, 'public'),
        publicPath: '/assets'
      },
      {
        directory: path.join(__dirname, 'data'),
        publicPath: '/data'
      }
    ]
  }
};
```

#### Port and Host

```javascript
module.exports = {
  devServer: {
    host: '0.0.0.0',  // Allow external access
    port: 8080,
    // Or auto-assign port
    port: 'auto'
  }
};
```

#### HTTPS

**Self-Signed Certificate**:
```javascript
module.exports = {
  devServer: {
    https: true
  }
};
```

**Custom Certificate**:
```javascript
const fs = require('fs');

module.exports = {
  devServer: {
    https: {
      key: fs.readFileSync('/path/to/server.key'),
      cert: fs.readFileSync('/path/to/server.crt'),
      ca: fs.readFileSync('/path/to/ca.pem')
    }
  }
};
```

#### Proxy Configuration

**Basic Proxy**:
```javascript
module.exports = {
  devServer: {
    proxy: {
      '/api': 'http://localhost:3001'
    }
  }
};
```

**Advanced Proxy**:
```javascript
module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:3001',
        pathRewrite: { '^/api': '' },  // Remove /api prefix
        changeOrigin: true,            // Change origin header
        secure: false,                 // Accept self-signed certs
        logLevel: 'debug'
      },
      '/auth': {
        target: 'http://localhost:3002',
        bypass: function(req, res, proxyOptions) {
          // Bypass proxy for specific requests
          if (req.headers.accept.indexOf('html') !== -1) {
            return '/index.html';
          }
        }
      }
    }
  }
};
```

**Multiple Targets**:
```javascript
module.exports = {
  devServer: {
    proxy: [
      {
        context: ['/api', '/auth'],
        target: 'http://localhost:3001'
      },
      {
        context: ['/graphql'],
        target: 'http://localhost:4000',
        ws: true  // Proxy WebSocket
      }
    ]
  }
};
```

#### History API Fallback

**For Single-Page Applications**:
```javascript
module.exports = {
  devServer: {
    historyApiFallback: true  // Redirect 404s to index.html
  }
};
```

**Custom Rewrites**:
```javascript
module.exports = {
  devServer: {
    historyApiFallback: {
      rewrites: [
        { from: /^\/admin/, to: '/admin.html' },
        { from: /^\/user/, to: '/user.html' },
        { from: /./, to: '/index.html' }
      ]
    }
  }
};
```

#### Headers

```javascript
module.exports = {
  devServer: {
    headers: {
      'X-Custom-Header': 'value',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, PATCH, OPTIONS'
    }
  }
};
```

#### Compression

```javascript
module.exports = {
  devServer: {
    compress: true  // Enable gzip compression
  }
};
```

#### Error Overlay

```javascript
module.exports = {
  devServer: {
    client: {
      overlay: {
        errors: true,
        warnings: false
      },
      progress: true,  // Show compilation progress
      reconnect: true  // Auto-reconnect on connection loss
    }
  }
};
```

#### Dev Middleware Options

```javascript
module.exports = {
  devServer: {
    devMiddleware: {
      index: true,
      publicPath: '/',
      serverSideRender: false,
      writeToDisk: false,  // Write files to disk
      stats: 'minimal'
    }
  }
};
```

## Hot Module Replacement (HMR)

### What is HMR?

Hot Module Replacement allows modules to be updated at runtime without a full page refresh, preserving application state during development.

### How HMR Works

1. **Initial Build**: Webpack generates bundle with HMR runtime
2. **File Change**: Developer saves a file
3. **Recompilation**: Webpack recompiles only changed modules
4. **Update Notification**: HMR runtime receives update via WebSocket
5. **Module Replacement**: Runtime replaces old module with new one
6. **State Preservation**: Application state is maintained

### Enabling HMR

**Automatic** (webpack-dev-server v4+):
```javascript
module.exports = {
  devServer: {
    hot: true  // Enabled by default
  }
};
```

**Manual Plugin**:
```javascript
const webpack = require('webpack');

module.exports = {
  plugins: [
    new webpack.HotModuleReplacementPlugin()
  ]
};
```

**Command Line**:
```bash
webpack serve --hot
```

### HMR API

#### Accepting Updates

**Self-Accept**:
```javascript
// module.js
export function render() {
  console.log('Rendering...');
}

if (module.hot) {
  module.hot.accept();  // Accept updates to this module
}
```

**Accept Dependencies**:
```javascript
// index.js
import { render } from './module';

render();

if (module.hot) {
  module.hot.accept('./module', function() {
    console.log('Module updated!');
    render();  // Re-execute with new module
  });
}
```

**Accept Multiple Dependencies**:
```javascript
if (module.hot) {
  module.hot.accept(
    ['./moduleA', './moduleB'],
    function() {
      // Handle updates
    }
  );
}
```

#### Disposing Modules

```javascript
let element = document.getElementById('app');

function render() {
  element.innerHTML = 'Hello World';
}

render();

if (module.hot) {
  module.hot.dispose(function(data) {
    // Clean up before module is replaced
    element.removeEventListener('click', handleClick);
    data.state = getCurrentState();  // Save state
  });
  
  module.hot.accept(function() {
    // Restore state after update
    const data = module.hot.data;
    if (data && data.state) {
      restoreState(data.state);
    }
    render();
  });
}
```

### HMR with Frameworks

#### React

**React Fast Refresh** (recommended):

**Installation**:
```bash
npm install --save-dev @pmmmwh/react-refresh-webpack-plugin react-refresh
```

**Configuration**:
```javascript
const ReactRefreshWebpackPlugin = require('@pmmmwh/react-refresh-webpack-plugin');

module.exports = {
  mode: 'development',
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            plugins: [
              require.resolve('react-refresh/babel')
            ]
          }
        }
      }
    ]
  },
  plugins: [
    new ReactRefreshWebpackPlugin()
  ],
  devServer: {
    hot: true
  }
};
```

**Legacy React Hot Loader**:
```javascript
// App.js
import { hot } from 'react-hot-loader/root';

function App() {
  return <div>Hello World</div>;
}

export default hot(App);
```

#### Vue

**vue-loader** (HMR built-in):
```javascript
const { VueLoaderPlugin } = require('vue-loader');

module.exports = {
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader'
      }
    ]
  },
  plugins: [
    new VueLoaderPlugin()
  ],
  devServer: {
    hot: true
  }
};
```

#### CSS

**style-loader** (HMR automatic):
```javascript
module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']  // HMR works automatically
      }
    ]
  }
};
```

**CSS Modules**:
```javascript
// styles.module.css
.button {
  background: blue;
}

// Component.js
import styles from './styles.module.css';

function Component() {
  return <button className={styles.button}>Click</button>;
}

if (module.hot) {
  module.hot.accept('./styles.module.css', () => {
    // CSS updated, component will re-render
  });
}
```

### HMR Best Practices

**1. Conditional HMR Code**:
```javascript
if (module.hot) {
  // HMR code only in development
  module.hot.accept();
}
```

This code is removed in production builds by minifiers.

**2. Handle Side Effects**:
```javascript
let subscription;

function init() {
  subscription = eventEmitter.subscribe(handler);
}

init();

if (module.hot) {
  module.hot.dispose(() => {
    // Clean up subscriptions
    subscription.unsubscribe();
  });
  
  module.hot.accept(() => {
    init();  // Re-initialize
  });
}
```

**3. State Management**:
```javascript
// Store state before disposal
if (module.hot) {
  module.hot.dispose((data) => {
    data.state = store.getState();
  });
  
  module.hot.accept(() => {
    if (module.hot.data && module.hot.data.state) {
      store.setState(module.hot.data.state);
    }
  });
}
```

**4. Debugging HMR**:
```javascript
if (module.hot) {
  module.hot.accept((err) => {
    if (err) {
      console.error('HMR error:', err);
    }
  });
  
  module.hot.addStatusHandler((status) => {
    console.log('HMR status:', status);
  });
}
```

### HMR Limitations

**What HMR Cannot Do**:
- Update entry point modules (requires full reload)
- Update modules that export non-function values without accept handler
- Recover from syntax errors (requires manual reload)

**Fallback to Live Reload**:
```javascript
module.exports = {
  devServer: {
    hot: 'only'  // Don't reload on HMR failure
    // or
    hot: true,   // Fallback to full reload on HMR failure
    liveReload: true
  }
};
```

## Development vs. Production

### Separate Configurations

**webpack.dev.js**:
```javascript
const { merge } = require('webpack-merge');
const common = require('./webpack.common.js');

module.exports = merge(common, {
  mode: 'development',
  devtool: 'eval-source-map',
  devServer: {
    hot: true,
    port: 3000,
    open: true
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']  // Inline CSS for HMR
      }
    ]
  }
});
```

**webpack.prod.js**:
```javascript
const { merge } = require('webpack-merge');
const common = require('./webpack.common.js');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = merge(common, {
  mode: 'production',
  devtool: 'source-map',
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [MiniCssExtractPlugin.loader, 'css-loader']  // Extract CSS
      }
    ]
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: '[name].[contenthash].css'
    })
  ]
});
```

**package.json**:
```json
{
  "scripts": {
    "start": "webpack serve --config webpack.dev.js",
    "build": "webpack --config webpack.prod.js"
  }
}
```

## Troubleshooting

### Common Issues

**1. HMR Not Working**:

**Check**:
- `hot: true` in devServer config
- Module has `module.hot.accept()` call
- No syntax errors in updated module
- Browser console for HMR messages

**2. Full Page Reload Instead of HMR**:

**Cause**: Module doesn't accept updates

**Solution**: Add accept handler:
```javascript
if (module.hot) {
  module.hot.accept();
}
```

**3. State Lost on Update**:

**Solution**: Implement dispose handler to save/restore state

**4. CORS Errors with Proxy**:

**Solution**:
```javascript
module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:3001',
        changeOrigin: true
      }
    }
  }
};
```

**5. WebSocket Connection Failed**:

**Solution**: Check firewall, ensure correct host/port, verify WebSocket support

## Performance Optimization

### Faster Rebuilds

**1. Cache**:
```javascript
module.exports = {
  cache: {
    type: 'filesystem',
    buildDependencies: {
      config: [__filename]
    }
  }
};
```

**2. Limit Scope**:
```javascript
module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        include: path.resolve(__dirname, 'src'),
        exclude: /node_modules/,
        use: 'babel-loader'
      }
    ]
  }
};
```

**3. Use Faster Loaders**:
```javascript
module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        use: 'esbuild-loader'  // Much faster than babel-loader
      }
    ]
  }
};
```

## Conclusion

Webpack Dev Server with Hot Module Replacement provides a powerful development environment that significantly improves developer productivity. By understanding HMR's capabilities and limitations, properly configuring the dev server, and implementing framework-specific HMR integrations, developers can achieve near-instant feedback on code changes while preserving application state. The key is balancing convenience with proper cleanup and state management to ensure HMR works reliably across the entire application.
