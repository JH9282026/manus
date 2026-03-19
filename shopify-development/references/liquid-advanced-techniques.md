# Liquid Advanced Techniques

Advanced Liquid templating patterns and techniques for complex Shopify theme development.

---

## Advanced Filtering and Search

### Custom Collection Filtering

Implement multi-faceted filtering without apps:

```liquid
{% liquid
  assign filtered_products = collection.products
  
  if filter_by_vendor
    assign filtered_products = filtered_products | where: 'vendor', filter_by_vendor
  endif
  
  if filter_by_tag
    assign filtered_products = filtered_products | where: 'tags', filter_by_tag
  endif
  
  if sort_by == 'price_low'
    assign filtered_products = filtered_products | sort: 'price'
  elsif sort_by == 'price_high'
    assign filtered_products = filtered_products | sort: 'price' | reverse
  endif
%}

{% for product in filtered_products %}
  {% render 'product-card', product: product %}
{% endfor %}
```

### Search Result Optimization

Enhance search results with custom ranking:

```liquid
{% assign exact_matches = search.results | where: 'title', search.terms %}
{% assign partial_matches = search.results | where_exp: 'item', 'item.title contains search.terms' %}
{% assign other_results = search.results | where_exp: 'item', 'item.title != search.terms' %}

{% for item in exact_matches %}
  {% render 'search-result', item: item, relevance: 'high' %}
{% endfor %}

{% for item in partial_matches %}
  {% unless exact_matches contains item %}
    {% render 'search-result', item: item, relevance: 'medium' %}
  {% endunless %}
{% endfor %}
```

## Metafield Rendering

### Dynamic Metafield Display

Render metafields based on type:

```liquid
{% for metafield in product.metafields.custom %}
  <div class="metafield-{{ metafield.key }}">
    <h4>{{ metafield.key | replace: '_', ' ' | capitalize }}</h4>
    
    {% case metafield.type %}
      {% when 'single_line_text_field' %}
        <p>{{ metafield.value }}</p>
      
      {% when 'multi_line_text_field' %}
        <div class="rich-text">{{ metafield.value | newline_to_br }}</div>
      
      {% when 'product_reference' %}
        {% render 'product-card', product: metafield.value %}
      
      {% when 'file_reference' %}
        {% if metafield.value.content_type contains 'image' %}
          <img src="{{ metafield.value | image_url: width: 800 }}" alt="{{ metafield.value.alt }}">
        {% elsif metafield.value.content_type contains 'video' %}
          <video src="{{ metafield.value.url }}" controls></video>
        {% endif %}
      
      {% when 'list.product_reference' %}
        <div class="product-grid">
          {% for related_product in metafield.value %}
            {% render 'product-card', product: related_product %}
          {% endfor %}
        </div>
    {% endcase %}
  </div>
{% endfor %}
```

### Metafield-Based Product Specifications

```liquid
{% if product.metafields.specs %}
  <table class="product-specifications">
    {% for spec in product.metafields.specs %}
      <tr>
        <th>{{ spec[0] | replace: '_', ' ' | capitalize }}</th>
        <td>{{ spec[1] }}</td>
      </tr>
    {% endfor %}
  </table>
{% endif %}
```

## Advanced Cart Functionality

### Cart Attributes and Notes

Implement custom cart attributes for special instructions:

```liquid
<form action="/cart" method="post">
  <label for="gift-message">Gift Message</label>
  <textarea name="attributes[Gift Message]" id="gift-message"></textarea>
  
  <label for="delivery-date">Preferred Delivery Date</label>
  <input type="date" name="attributes[Delivery Date]" id="delivery-date">
  
  <input type="checkbox" name="attributes[Gift Wrap]" value="Yes" id="gift-wrap">
  <label for="gift-wrap">Add Gift Wrapping (+$5.00)</label>
  
  <button type="submit">Update Cart</button>
</form>

<!-- Display cart attributes -->
{% if cart.attributes.size > 0 %}
  <div class="cart-attributes">
    <h3>Special Instructions</h3>
    {% for attribute in cart.attributes %}
      <p><strong>{{ attribute[0] }}:</strong> {{ attribute[1] }}</p>
    {% endfor %}
  </div>
{% endif %}
```

### Dynamic Cart Upsells

Suggest complementary products based on cart contents:

```liquid
{% assign cart_tags = '' %}
{% for item in cart.items %}
  {% assign cart_tags = cart_tags | append: item.product.tags | join: ',' | append: ',' %}
{% endfor %}
{% assign cart_tags = cart_tags | split: ',' | uniq %}

{% assign upsell_products = collections.all.products 
  | where_exp: 'product', 'product.tags contains cart_tags[0]' 
  | where_exp: 'product', 'cart.items contains product == false' 
  | limit: 4 %}

{% if upsell_products.size > 0 %}
  <div class="cart-upsells">
    <h3>You might also like</h3>
    {% for product in upsell_products %}
      {% render 'product-card-mini', product: product %}
    {% endfor %}
  </div>
{% endif %}
```

## Performance Optimization Patterns

### Lazy Loading Images

Implement native lazy loading with fallback:

```liquid
{% assign loading = 'lazy' %}
{% if section.index == 1 %}
  {% assign loading = 'eager' %}
{% endif %}

<img 
  src="{{ product.featured_image | image_url: width: 800 }}"
  srcset="
    {{ product.featured_image | image_url: width: 400 }} 400w,
    {{ product.featured_image | image_url: width: 800 }} 800w,
    {{ product.featured_image | image_url: width: 1200 }} 1200w
  "
  sizes="(max-width: 768px) 100vw, 50vw"
  loading="{{ loading }}"
  alt="{{ product.featured_image.alt | escape }}"
  width="800"
  height="{{ 800 | divided_by: product.featured_image.aspect_ratio | round }}"
>
```

### Efficient Pagination

Implement pagination with minimal queries:

```liquid
{% paginate collection.products by 24 %}
  <div class="product-grid">
    {% for product in collection.products %}
      {% render 'product-card', product: product %}
    {% endfor %}
  </div>
  
  {% if paginate.pages > 1 %}
    <nav class="pagination" aria-label="Pagination">
      {% if paginate.previous %}
        <a href="{{ paginate.previous.url }}" rel="prev">Previous</a>
      {% endif %}
      
      {% for part in paginate.parts %}
        {% if part.is_link %}
          <a href="{{ part.url }}">{{ part.title }}</a>
        {% else %}
          {% if part.title == paginate.current_page %}
            <span aria-current="page">{{ part.title }}</span>
          {% else %}
            <span>{{ part.title }}</span>
          {% endif %}
        {% endif %}
      {% endfor %}
      
      {% if paginate.next %}
        <a href="{{ paginate.next.url }}" rel="next">Next</a>
      {% endif %}
    </nav>
  {% endif %}
{% endpaginate %}
```

## Dynamic Content Generation

### Conditional Section Rendering

Render sections based on template or product type:

```liquid
{% case template.name %}
  {% when 'product' %}
    {% if product.type == 'Apparel' %}
      {% section 'size-guide' %}
      {% section 'fabric-care' %}
    {% elsif product.type == 'Electronics' %}
      {% section 'tech-specs' %}
      {% section 'warranty-info' %}
    {% endif %}
    
    {% section 'product-reviews' %}
    {% section 'related-products' %}
  
  {% when 'collection' %}
    {% section 'collection-filters' %}
    {% section 'collection-banner' %}
  
  {% when 'page' %}
    {% if page.handle == 'about' %}
      {% section 'team-members' %}
      {% section 'company-timeline' %}
    {% endif %}
{% endcase %}
```

### Dynamic Menu Generation

Create menus from collections or metafields:

```liquid
<nav class="mega-menu">
  {% for link in linklists.main-menu.links %}
    <div class="menu-item">
      <a href="{{ link.url }}">{{ link.title }}</a>
      
      {% if link.links.size > 0 %}
        <div class="submenu">
          {% for child_link in link.links %}
            <a href="{{ child_link.url }}">{{ child_link.title }}</a>
            
            {% if child_link.object.type == 'collection' %}
              {% assign featured_products = child_link.object.products | limit: 3 %}
              <div class="featured-products">
                {% for product in featured_products %}
                  {% render 'product-card-mini', product: product %}
                {% endfor %}
              </div>
            {% endif %}
          {% endfor %}
        </div>
      {% endif %}
    </div>
  {% endfor %}
</nav>
```

## Variant Selection and Inventory

### Advanced Variant Selector

Implement smart variant selection with availability:

```liquid
<form action="/cart/add" method="post" class="product-form">
  {% for option in product.options_with_values %}
    <div class="option-selector">
      <label>{{ option.name }}</label>
      <div class="option-values">
        {% for value in option.values %}
          {% assign option_available = false %}
          
          {% for variant in product.variants %}
            {% if variant.available %}
              {% case option.position %}
                {% when 1 %}
                  {% if variant.option1 == value %}
                    {% assign option_available = true %}
                  {% endif %}
                {% when 2 %}
                  {% if variant.option2 == value %}
                    {% assign option_available = true %}
                  {% endif %}
                {% when 3 %}
                  {% if variant.option3 == value %}
                    {% assign option_available = true %}
                  {% endif %}
              {% endcase %}
            {% endif %}
          {% endfor %}
          
          <input 
            type="radio" 
            name="option{{ option.position }}" 
            value="{{ value | escape }}"
            id="option-{{ option.position }}-{{ value | handle }}"
            {% unless option_available %}disabled{% endunless %}
          >
          <label 
            for="option-{{ option.position }}-{{ value | handle }}"
            class="{% unless option_available %}unavailable{% endunless %}"
          >
            {{ value }}
          </label>
        {% endfor %}
      </div>
    </div>
  {% endfor %}
  
  <select name="id" class="variant-select" style="display:none;">
    {% for variant in product.variants %}
      <option 
        value="{{ variant.id }}"
        {% unless variant.available %}disabled{% endunless %}
      >
        {{ variant.title }} - {{ variant.price | money }}
      </option>
    {% endfor %}
  </select>
  
  <button type="submit" name="add">Add to Cart</button>
</form>

<script>
  // JavaScript to sync option selectors with variant select
  // and update price, availability, and images
</script>
```

### Low Stock Indicators

```liquid
{% if product.selected_or_first_available_variant.inventory_quantity <= 5 
   and product.selected_or_first_available_variant.inventory_quantity > 0 %}
  <p class="low-stock-warning">
    Only {{ product.selected_or_first_available_variant.inventory_quantity }} left in stock!
  </p>
{% elsif product.selected_or_first_available_variant.inventory_quantity == 0 %}
  <p class="out-of-stock">Out of Stock</p>
  <button type="button" class="notify-me">Notify When Available</button>
{% endif %}
```

## Internationalization and Localization

### Multi-Currency Support

```liquid
{% if shop.enabled_currencies.size > 1 %}
  <form class="currency-selector">
    <label for="currency">Currency</label>
    <select id="currency" name="currency">
      {% for currency in shop.enabled_currencies %}
        <option 
          value="{{ currency.iso_code }}"
          {% if currency.iso_code == cart.currency.iso_code %}selected{% endif %}
        >
          {{ currency.iso_code }} {{ currency.symbol }}
        </option>
      {% endfor %}
    </select>
  </form>
{% endif %}

<!-- Display prices with currency -->
<span class="price">
  {{ product.price | money_with_currency }}
</span>
```

### Multi-Language Content

```liquid
{% if localization.available_languages.size > 1 %}
  <form class="language-selector">
    <label for="language">Language</label>
    <select id="language" name="language">
      {% for language in localization.available_languages %}
        <option 
          value="{{ language.iso_code }}"
          {% if language.iso_code == localization.language.iso_code %}selected{% endif %}
        >
          {{ language.endonym_name }}
        </option>
      {% endfor %}
    </select>
  </form>
{% endif %}

<!-- Use translation keys -->
<button type="submit">{{ 'products.product.add_to_cart' | t }}</button>
<p>{{ 'cart.general.shipping_at_checkout' | t }}</p>
```

## Schema and Settings

### Advanced Section Schema

```json
{
  "name": "Featured Collection",
  "settings": [
    {
      "type": "collection",
      "id": "collection",
      "label": "Collection"
    },
    {
      "type": "range",
      "id": "products_to_show",
      "min": 2,
      "max": 12,
      "step": 2,
      "default": 4,
      "label": "Products to show"
    },
    {
      "type": "select",
      "id": "layout",
      "label": "Layout",
      "options": [
        { "value": "grid", "label": "Grid" },
        { "value": "carousel", "label": "Carousel" },
        { "value": "list", "label": "List" }
      ],
      "default": "grid"
    },
    {
      "type": "checkbox",
      "id": "show_vendor",
      "label": "Show vendor",
      "default": false
    },
    {
      "type": "color",
      "id": "background_color",
      "label": "Background color",
      "default": "#ffffff"
    }
  ],
  "blocks": [
    {
      "type": "heading",
      "name": "Heading",
      "settings": [
        {
          "type": "text",
          "id": "title",
          "label": "Heading",
          "default": "Featured Collection"
        },
        {
          "type": "select",
          "id": "heading_size",
          "label": "Heading size",
          "options": [
            { "value": "small", "label": "Small" },
            { "value": "medium", "label": "Medium" },
            { "value": "large", "label": "Large" }
          ],
          "default": "medium"
        }
      ]
    }
  ],
  "presets": [
    {
      "name": "Featured Collection",
      "blocks": [
        { "type": "heading" }
      ]
    }
  ]
}
```