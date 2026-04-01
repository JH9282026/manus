# Webpack: Real-World Configurations and Best Practices

## Introduction

Moving from basic webpack configurations to production-ready setups requires understanding real-world patterns, performance optimization, and maintainability strategies. This guide presents practical configurations for common scenarios, from single-page applications to complex multi-page projects, with emphasis on scalability and developer experience.

## Project Structure Best Practices

### Recommended Directory Structure

```
project/
├── config/
│   ├── webpack.common.js
│   ├── webpack.dev.js
│   ├── webpack.prod.js
│   └── paths.js
├── public/
│   ├── index.html
│   ├── favicon.ico
│   └── robots.txt
├── src/
│   ├── assets/
│   │   ├── images/
│   │   ├── fonts/
│   │   └── styles/
│   ├── components/
│   ├── pages/
│   ├── utils/
│   ├── index.js
│   └── App.js
├── dist/
├── node_modules/
├── package.json
├── .babelrc
├── .eslintrc.js
└── tsconfig.json
```

### Path Configuration

**config/paths.js**:
```javascript
const path = require('path');

module.exports = {
  root: path.resolve(__dirname, '..'),
  src: path.resolve(__dirname, '../src'),
  build: path.resolve(__dirname, '../dist'),
  public: path.resolve(__dirname, '../public'),
  nodeModules: path.resolve(__dirname, '../node_modules')
};
```

## Configuration Patterns

### Common Configuration

**config/webpack.common.js**:
```javascript
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const paths = require('./paths');

module.exports = {
  entry: {
    app: path.join(paths.src, 'index.js')
  },
  
  output: {
    path: paths.build,
    filename: '[name].[contenthash].js',
    chunkFilename: '[name].[contenthash].chunk.js',
    publicPath: '/',
    assetModuleFilename: 'assets/[name].[hash][ext]'
  },
  
  resolve: {
    extensions: ['.js', '.jsx', '.ts', '.tsx', '.json'],
    alias: {
      '@': paths.src,
      '@components': path.join(paths.src, 'components'),
      '@utils': path.join(paths.src, 'utils'),
      '@assets': path.join(paths.src, 'assets')
    }
  },
  
  module: {
    rules: [
      // JavaScript/TypeScript
      {
        test: /\.(js|jsx|ts|tsx)$/,
        include: paths.src,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            cacheDirectory: true,
            cacheCompression: false
          }
        }
      },
      
      // Images
      {
        test: /\.(png|jpg|jpeg|gif|svg)$/i,
        type: 'asset',
        parser: {
          dataUrlCondition: {
            maxSize: 8 * 1024 // 8kb
          }
        },
        generator: {
          filename: 'images/[name].[hash][ext]'
        }
      },
      
      // Fonts
      {
        test: /\.(woff|woff2|eot|ttf|otf)$/i,
        type: 'asset/resource',
        generator: {
          filename: 'fonts/[name][ext]'
        }
      }
    ]
  },
  
  plugins: [
    new CleanWebpackPlugin(),
    
    new HtmlWebpackPlugin({
      template: path.join(paths.public, 'index.html'),
      favicon: path.join(paths.public, 'favicon.ico'),
      inject: 'body',
      scriptLoading: 'defer'
    })
  ],
  
  stats: {
    colors: true,
    modules: false,
    children: false,
    chunks: false,
    chunkModules: false
  }
};
```

### Development Configuration

**config/webpack.dev.js**:
```javascript
const { merge } = require('webpack-merge');
const webpack = require('webpack');
const common = require('./webpack.common');
const paths = require('./paths');

module.exports = merge(common, {
  mode: 'development',
  
  devtool: 'eval-source-map',
  
  devServer: {
    static: {
      directory: paths.public,
      watch: true
    },
    historyApiFallback: true,
    hot: true,
    open: true,
    compress: true,
    port: 3000,
    client: {
      overlay: {
        errors: true,
        warnings: false
      },
      progress: true
    },
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        pathRewrite: { '^/api': '' }
      }
    }
  },
  
  module: {
    rules: [
      // CSS
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader', 'postcss-loader']
      },
      
      // SCSS
      {
        test: /\.scss$/,
        use: [
          'style-loader',
          {
            loader: 'css-loader',
            options: {
              sourceMap: true,
              modules: {
                auto: true,
                localIdentName: '[name]__[local]--[hash:base64:5]'
              }
            }
          },
          {
            loader: 'postcss-loader',
            options: { sourceMap: true }
          },
          {
            loader: 'sass-loader',
            options: { sourceMap: true }
          }
        ]
      }
    ]
  },
  
  plugins: [
    new webpack.DefinePlugin({
      'process.env.NODE_ENV': JSON.stringify('development'),
      'process.env.API_URL': JSON.stringify('http://localhost:8000')
    })
  ],
  
  cache: {
    type: 'filesystem',
    buildDependencies: {
      config: [__filename]
    }
  }
});
```

### Production Configuration

**config/webpack.prod.js**:
```javascript
const { merge } = require('webpack-merge');
const webpack = require('webpack');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CssMinimizerPlugin = require('css-minimizer-webpack-plugin');
const TerserPlugin = require('terser-webpack-plugin');
const CompressionPlugin = require('compression-webpack-plugin');
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;
const common = require('./webpack.common');

module.exports = merge(common, {
  mode: 'production',
  
  devtool: 'source-map',
  
  output: {
    ...common.output,
    clean: true
  },
  
  module: {
    rules: [
      // CSS
      {
        test: /\.css$/,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
          'postcss-loader'
        ]
      },
      
      // SCSS
      {
        test: /\.scss$/,
        use: [
          MiniCssExtractPlugin.loader,
          {
            loader: 'css-loader',
            options: {
              modules: {
                auto: true,
                localIdentName: '[hash:base64]'
              }
            }
          },
          'postcss-loader',
          'sass-loader'
        ]
      }
    ]
  },
  
  plugins: [
    new webpack.DefinePlugin({
      'process.env.NODE_ENV': JSON.stringify('production'),
      'process.env.API_URL': JSON.stringify('https://api.production.com')
    }),
    
    new MiniCssExtractPlugin({
      filename: 'css/[name].[contenthash].css',
      chunkFilename: 'css/[id].[contenthash].css'
    }),
    
    new CompressionPlugin({
      filename: '[path][base].gz',
      algorithm: 'gzip',
      test: /\.(js|css|html|svg)$/,
      threshold: 10240,
      minRatio: 0.8
    }),
    
    new CompressionPlugin({
      filename: '[path][base].br',
      algorithm: 'brotliCompress',
      test: /\.(js|css|html|svg)$/,
      threshold: 10240,
      minRatio: 0.8
    }),
    
    process.env.ANALYZE && new BundleAnalyzerPlugin({
      analyzerMode: 'static',
      reportFilename: 'bundle-report.html',
      openAnalyzer: false
    })
  ].filter(Boolean),
  
  optimization: {
    minimize: true,
    minimizer: [
      new TerserPlugin({
        terserOptions: {
          compress: {
            drop_console: true,
            drop_debugger: true,
            pure_funcs: ['console.log', 'console.info']
          },
          format: {
            comments: false
          }
        },
        extractComments: false,
        parallel: true
      }),
      new CssMinimizerPlugin({
        minimizerOptions: {
          preset: ['default', {
            discardComments: { removeAll: true }
          }]
        }
      })
    ],
    
    moduleIds: 'deterministic',
    
    runtimeChunk: 'single',
    
    splitChunks: {
      chunks: 'all',
      maxInitialRequests: 25,
      maxAsyncRequests: 25,
      cacheGroups: {
        // React vendor chunk
        react: {
          test: /[\\/]node_modules[\\/](react|react-dom|react-router-dom)[\\/]/,
          name: 'react-vendor',
          priority: 40,
          reuseExistingChunk: true
        },
        
        // Other vendor libraries
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendor',
          priority: 30,
          reuseExistingChunk: true
        },
        
        // Common code shared between chunks
        common: {
          minChunks: 2,
          name: 'common',
          priority: 20,
          reuseExistingChunk: true,
          enforce: true
        }
      }
    }
  },
  
  performance: {
    maxAssetSize: 250000,
    maxEntrypointSize: 400000,
    hints: 'warning'
  }
});
```

## Framework-Specific Configurations

### React Application

**Complete React Setup**:

**Installation**:
```bash
npm install --save react react-dom
npm install --save-dev @babel/preset-react
npm install --save-dev @pmmmwh/react-refresh-webpack-plugin react-refresh
```

**.babelrc**:
```json
{
  "presets": [
    ["@babel/preset-env", {
      "modules": false,
      "useBuiltIns": "usage",
      "corejs": 3
    }],
    ["@babel/preset-react", {
      "runtime": "automatic"
    }]
  ],
  "plugins": [
    "@babel/plugin-proposal-class-properties"
  ],
  "env": {
    "development": {
      "plugins": ["react-refresh/babel"]
    }
  }
}
```

**webpack.dev.js additions**:
```javascript
const ReactRefreshWebpackPlugin = require('@pmmmwh/react-refresh-webpack-plugin');

module.exports = merge(common, {
  // ... other config
  plugins: [
    new ReactRefreshWebpackPlugin()
  ]
});
```

### TypeScript Application

**Installation**:
```bash
npm install --save-dev typescript ts-loader
# or for faster builds
npm install --save-dev esbuild-loader
```

**tsconfig.json**:
```json
{
  "compilerOptions": {
    "target": "ES2015",
    "module": "ESNext",
    "lib": ["ES2015", "DOM", "DOM.Iterable"],
    "jsx": "react-jsx",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "allowJs": true,
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@components/*": ["src/components/*"],
      "@utils/*": ["src/utils/*"]
    }
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

**webpack.common.js additions**:
```javascript
module.exports = {
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        exclude: /node_modules/,
        use: {
          loader: 'ts-loader',
          options: {
            transpileOnly: true  // Faster builds, type checking in separate process
          }
        }
      }
    ]
  }
};
```

**With esbuild-loader** (faster):
```javascript
const { ESBuildMinifyPlugin } = require('esbuild-loader');

module.exports = {
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        loader: 'esbuild-loader',
        options: {
          loader: 'tsx',
          target: 'es2015'
        }
      }
    ]
  },
  optimization: {
    minimizer: [
      new ESBuildMinifyPlugin({
        target: 'es2015',
        css: true
      })
    ]
  }
};
```

### Vue Application

**Installation**:
```bash
npm install --save vue
npm install --save-dev vue-loader vue-template-compiler
```

**webpack.common.js**:
```javascript
const { VueLoaderPlugin } = require('vue-loader');

module.exports = {
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader'
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: 'babel-loader'
      }
    ]
  },
  plugins: [
    new VueLoaderPlugin()
  ],
  resolve: {
    alias: {
      'vue$': 'vue/dist/vue.esm.js'
    },
    extensions: ['.js', '.vue', '.json']
  }
};
```

## Multi-Page Application

**Configuration**:
```javascript
const HtmlWebpackPlugin = require('html-webpack-plugin');
const paths = require('./paths');

const pages = ['home', 'about', 'contact'];

module.exports = {
  entry: pages.reduce((entries, page) => {
    entries[page] = path.join(paths.src, `${page}/index.js`);
    return entries;
  }, {}),
  
  plugins: [
    ...pages.map(page => new HtmlWebpackPlugin({
      template: path.join(paths.src, `${page}/index.html`),
      filename: `${page}.html`,
      chunks: [page, 'vendor', 'common'],
      inject: 'body'
    }))
  ],
  
  optimization: {
    splitChunks: {
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendor',
          chunks: 'all'
        },
        common: {
          minChunks: 2,
          name: 'common',
          chunks: 'all',
          priority: -10,
          reuseExistingChunk: true
        }
      }
    }
  }
};
```

## Environment Variables

### Using dotenv

**Installation**:
```bash
npm install --save-dev dotenv-webpack
```

**.env.development**:
```
API_URL=http://localhost:8000
FEATURE_FLAG_NEW_UI=true
ANALYTICS_ID=dev-123
```

**.env.production**:
```
API_URL=https://api.production.com
FEATURE_FLAG_NEW_UI=true
ANALYTICS_ID=prod-456
```

**webpack.config.js**:
```javascript
const Dotenv = require('dotenv-webpack');

module.exports = {
  plugins: [
    new Dotenv({
      path: `./.env.${process.env.NODE_ENV || 'development'}`,
      safe: true,  // Load .env.example to verify required variables
      systemvars: true,  // Load system environment variables
      silent: false
    })
  ]
};
```

**Usage in code**:
```javascript
console.log(process.env.API_URL);
console.log(process.env.FEATURE_FLAG_NEW_UI);
```

## Progressive Web App (PWA)

**Installation**:
```bash
npm install --save-dev workbox-webpack-plugin
```

**webpack.prod.js**:
```javascript
const WorkboxPlugin = require('workbox-webpack-plugin');

module.exports = {
  plugins: [
    new WorkboxPlugin.GenerateSW({
      clientsClaim: true,
      skipWaiting: true,
      maximumFileSizeToCacheInBytes: 5 * 1024 * 1024,
      runtimeCaching: [
        {
          urlPattern: /^https:\/\/api\.example\.com/,
          handler: 'NetworkFirst',
          options: {
            cacheName: 'api-cache',
            expiration: {
              maxEntries: 50,
              maxAgeSeconds: 5 * 60  // 5 minutes
            }
          }
        },
        {
          urlPattern: /\.(?:png|jpg|jpeg|svg|gif)$/,
          handler: 'CacheFirst',
          options: {
            cacheName: 'image-cache',
            expiration: {
              maxEntries: 100,
              maxAgeSeconds: 30 * 24 * 60 * 60  // 30 days
            }
          }
        }
      ]
    })
  ]
};
```

**Register Service Worker**:
```javascript
// src/index.js
if ('serviceWorker' in navigator && process.env.NODE_ENV === 'production') {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/service-worker.js')
      .then(registration => {
        console.log('SW registered:', registration);
      })
      .catch(error => {
        console.log('SW registration failed:', error);
      });
  });
}
```

## Code Splitting Strategies

### Route-Based Splitting

**React Router Example**:
```javascript
import React, { Suspense, lazy } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

const Home = lazy(() => import(/* webpackChunkName: "home" */ './pages/Home'));
const About = lazy(() => import(/* webpackChunkName: "about" */ './pages/About'));
const Dashboard = lazy(() => import(/* webpackChunkName: "dashboard" */ './pages/Dashboard'));

function App() {
  return (
    <BrowserRouter>
      <Suspense fallback={<div>Loading...</div>}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </Suspense>
    </BrowserRouter>
  );
}
```

### Vendor Splitting

**Advanced Vendor Splitting**:
```javascript
module.exports = {
  optimization: {
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        // React ecosystem
        react: {
          test: /[\\/]node_modules[\\/](react|react-dom|react-router-dom)[\\/]/,
          name: 'react',
          priority: 40
        },
        
        // UI libraries
        ui: {
          test: /[\\/]node_modules[\\/](@mui|@emotion)[\\/]/,
          name: 'ui',
          priority: 35
        },
        
        // Utilities
        utils: {
          test: /[\\/]node_modules[\\/](lodash|date-fns|axios)[\\/]/,
          name: 'utils',
          priority: 30
        },
        
        // Other vendors
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendor',
          priority: 20
        }
      }
    }
  }
};
```

## Performance Monitoring

### Build Time Analysis

**speed-measure-webpack-plugin**:
```bash
npm install --save-dev speed-measure-webpack-plugin
```

**webpack.config.js**:
```javascript
const SpeedMeasurePlugin = require('speed-measure-webpack-plugin');
const smp = new SpeedMeasurePlugin();

module.exports = smp.wrap({
  // Your webpack config
});
```

### Bundle Size Monitoring

**package.json**:
```json
{
  "scripts": {
    "build": "webpack --config config/webpack.prod.js",
    "build:analyze": "ANALYZE=true npm run build",
    "build:stats": "webpack --config config/webpack.prod.js --json > stats.json"
  }
}
```

## CI/CD Integration

### GitHub Actions Example

**.github/workflows/build.yml**:
```yaml
name: Build and Deploy

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run tests
        run: npm test
      
      - name: Build
        run: npm run build
        env:
          NODE_ENV: production
          API_URL: ${{ secrets.API_URL }}
      
      - name: Upload artifacts
        uses: actions/upload-artifact@v3
        with:
          name: dist
          path: dist/
```

## Troubleshooting Common Issues

### Large Bundle Sizes

**Diagnosis**:
```bash
npm run build:analyze
```

**Solutions**:
1. Enable tree shaking (ES modules, sideEffects: false)
2. Implement code splitting
3. Use lighter alternatives (date-fns vs moment)
4. Remove unused dependencies
5. Enable compression

### Slow Build Times

**Solutions**:
1. Enable caching:
```javascript
module.exports = {
  cache: {
    type: 'filesystem'
  }
};
```

2. Limit loader scope:
```javascript
{
  test: /\.js$/,
  include: paths.src,
  exclude: /node_modules/
}
```

3. Use faster loaders (esbuild-loader vs babel-loader)

4. Parallelize builds:
```javascript
new TerserPlugin({
  parallel: true
})
```

### Memory Issues

**Solutions**:
1. Increase Node memory:
```json
{
  "scripts": {
    "build": "node --max-old-space-size=4096 node_modules/webpack/bin/webpack.js"
  }
}
```

2. Reduce concurrency:
```javascript
module.exports = {
  parallelism: 1
};
```

## Best Practices Summary

### Configuration
- Separate dev/prod configs with webpack-merge
- Use environment variables for configuration
- Implement proper path aliases
- Enable source maps appropriately

### Performance
- Enable tree shaking (ES modules, sideEffects)
- Implement code splitting (routes, vendors)
- Use contenthash for long-term caching
- Enable compression (gzip, brotli)
- Monitor bundle sizes

### Development Experience
- Enable HMR for fast feedback
- Use React Fast Refresh or equivalent
- Implement proper error overlays
- Configure proxies for API calls

### Production
- Minify JS and CSS
- Extract CSS to separate files
- Remove console.log statements
- Generate source maps
- Implement performance budgets

### Maintenance
- Keep webpack and loaders updated
- Document custom configurations
- Use consistent code style
- Implement CI/CD pipelines

## Conclusion

Real-world webpack configurations require balancing performance, developer experience, and maintainability. By following established patterns—separating development and production configs, implementing proper code splitting, enabling caching strategies, and monitoring bundle sizes—teams can build scalable webpack setups that grow with their applications. The key is starting with a solid foundation and iteratively optimizing based on actual metrics and team needs.
