# React Native Performance Guide

Optimization techniques for React Native apps.

---

## List Optimization

```javascript
<FlatList
  data={data}
  renderItem={renderItem}
  keyExtractor={item => item.id}
  getItemLayout={(data, index) => ({
    length: ITEM_HEIGHT,
    offset: ITEM_HEIGHT * index,
    index
  })}
  removeClippedSubviews={true}
  maxToRenderPerBatch={10}
  updateCellsBatchingPeriod={50}
  initialNumToRender={10}
  windowSize={5}
/>
```

## Image Optimization

```javascript
<Image
  source={{ uri: imageUrl }}
  resizeMode="cover"
  style={{ width: 200, height: 200 }}
  defaultSource={require('./placeholder.png')}
/>

// Use FastImage for better performance
import FastImage from 'react-native-fast-image';

<FastImage
  source={{ uri: imageUrl, priority: FastImage.priority.normal }}
  resizeMode={FastImage.resizeMode.cover}
/>
```

## Bundle Size Optimization

- Use Hermes JavaScript engine
- Enable ProGuard/R8 for Android
- Implement code splitting
- Remove unused dependencies
- Use vector icons instead of image assets
