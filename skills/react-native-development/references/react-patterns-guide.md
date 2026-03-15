# React Patterns Guide

Advanced React patterns for React Native development.

---

## Custom Hooks

```javascript
function useDebounce(value, delay) {
  const [debouncedValue, setDebouncedValue] = useState(value);
  
  useEffect(() => {
    const handler = setTimeout(() => setDebouncedValue(value), delay);
    return () => clearTimeout(handler);
  }, [value, delay]);
  
  return debouncedValue;
}

// Usage
const debouncedSearch = useDebounce(searchTerm, 500);
```

## Context Pattern

```javascript
const ThemeContext = createContext();

export const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState('light');
  
  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};

export const useTheme = () => useContext(ThemeContext);
```

## Compound Components

```javascript
const Accordion = ({ children }) => {
  const [openIndex, setOpenIndex] = useState(null);
  
  return (
    <AccordionContext.Provider value={{ openIndex, setOpenIndex }}>
      {children}
    </AccordionContext.Provider>
  );
};

Accordion.Item = ({ index, title, children }) => {
  const { openIndex, setOpenIndex } = useContext(AccordionContext);
  const isOpen = openIndex === index;
  
  return (
    <View>
      <TouchableOpacity onPress={() => setOpenIndex(isOpen ? null : index)}>
        <Text>{title}</Text>
      </TouchableOpacity>
      {isOpen && <View>{children}</View>}
    </View>
  );
};
```
