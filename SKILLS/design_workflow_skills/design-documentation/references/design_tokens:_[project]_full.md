## Design Tokens: [PROJECT] (Full)

### Colors

#### Brand Colors

```json
{
  "color": {
    "primary": {
      "50": { "value": "#F5F3FF", "type": "color" },
      "100": { "value": "#EDE9FE", "type": "color" },
      "200": { "value": "#DDD6FE", "type": "color" },
      "300": { "value": "#C4B5FD", "type": "color" },
      "400": { "value": "#A78BFA", "type": "color" },
      "500": { "value": "#8B5CF6", "type": "color" },
      "600": { "value": "#7C3AED", "type": "color" },
      "700": { "value": "#6D28D9", "type": "color" },
      "800": { "value": "#5B21B6", "type": "color" },
      "900": { "value": "#4C1D95", "type": "color" }
    }
  }
}
```

#### Usage

| Token | CSS Variable | Usage |
|-------|--------------|-------|
| primary.500 | --color-primary-500 | Primary buttons, links |
| primary.600 | --color-primary-600 | Hover states |
| primary.100 | --color-primary-100 | Selected backgrounds |

### Typography

```json
{
  "font": {
    "family": {
      "primary": { "value": "'Inter', sans-serif" },
      "mono": { "value": "'JetBrains Mono', monospace" }
    },
    "size": {
      "xs": { "value": "0.75rem" },
      "sm": { "value": "0.875rem" },
      "base": { "value": "1rem" },
      "lg": { "value": "1.125rem" },
      "xl": { "value": "1.25rem" },
      "2xl": { "value": "1.5rem" },
      "3xl": { "value": "1.875rem" },
      "4xl": { "value": "2.25rem" }
    },
    "weight": {
      "normal": { "value": "400" },
      "medium": { "value": "500" },
      "semibold": { "value": "600" },
      "bold": { "value": "700" }
    },
    "lineHeight": {
      "tight": { "value": "1.25" },
      "normal": { "value": "1.5" },
      "relaxed": { "value": "1.75" }
    }
  }
}
```

### Spacing

```json
{
  "spacing": {
    "0": { "value": "0" },
    "1": { "value": "0.25rem" },
    "2": { "value": "0.5rem" },
    "3": { "value": "0.75rem" },
    "4": { "value": "1rem" },
    "5": { "value": "1.25rem" },
    "6": { "value": "1.5rem" },
    "8": { "value": "2rem" },
    "10": { "value": "2.5rem" },
    "12": { "value": "3rem" },
    "16": { "value": "4rem" }
  }
}
```

### Effects

```json
{
  "shadow": {
    "sm": { "value": "0 1px 2px rgba(0,0,0,0.05)" },
    "md": { "value": "0 4px 6px rgba(0,0,0,0.07)" },
    "lg": { "value": "0 10px 15px rgba(0,0,0,0.1)" },
    "xl": { "value": "0 20px 25px rgba(0,0,0,0.15)" }
  },
  "radius": {
    "sm": { "value": "4px" },
    "md": { "value": "8px" },
    "lg": { "value": "12px" },
    "xl": { "value": "16px" },
    "full": { "value": "9999px" }
  },
  "transition": {
    "fast": { "value": "150ms ease-out" },
    "normal": { "value": "200ms ease-out" },
    "slow": { "value": "300ms ease-out" }
  }
}
```
```

### Step 3: Component Documentation

**Component spec template:**

```markdown