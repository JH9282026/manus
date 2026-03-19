# React Navigation Guide

Comprehensive guide to React Navigation.

---

## Stack Navigation

```javascript
const Stack = createNativeStackNavigator();

<Stack.Navigator
  screenOptions={{
    headerStyle: { backgroundColor: '#f4511e' },
    headerTintColor: '#fff'
  }}
>
  <Stack.Screen 
    name="Home" 
    component={HomeScreen}
    options={{ title: 'My Home' }}
  />
</Stack.Navigator>
```

## Tab Navigation

```javascript
const Tab = createBottomTabNavigator();

<Tab.Navigator
  screenOptions={({ route }) => ({
    tabBarIcon: ({ focused, color, size }) => {
      let iconName;
      if (route.name === 'Home') {
        iconName = focused ? 'home' : 'home-outline';
      }
      return <Icon name={iconName} size={size} color={color} />;
    }
  })}
>
  <Tab.Screen name="Home" component={HomeScreen} />
  <Tab.Screen name="Settings" component={SettingsScreen} />
</Tab.Navigator>
```

## Deep Linking

```javascript
const linking = {
  prefixes: ['myapp://', 'https://myapp.com'],
  config: {
    screens: {
      Home: 'home',
      Profile: 'user/:id'
    }
  }
};

<NavigationContainer linking={linking}>
  {/* navigators */}
</NavigationContainer>
```
