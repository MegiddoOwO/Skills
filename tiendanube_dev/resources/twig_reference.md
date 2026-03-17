# 📘 Referencia Técnica: Twig en Tiendanube

Este documento es una guía rápida sobre los objetos y métodos más utilizados en el desarrollo de temas.

## 📦 Objetos Principales

### `store`
Información general de la tienda.
- `store.name`: Nombre de la tienda.
- `store.logo`: URL del logo.
- `store.url`: URL de la tienda.
- `store.contact_email`: Email de contacto.

### `product`
Disponible en `product.tpl` y loops de productos.
- `product.name`: Nombre del producto.
- `product.url`: URL del producto.
- `product.images`: Lista de imágenes.
- `product.price | money`: Precio formateado.
- `product.compare_at_price | money`: Precio de comparación.
- `product.has_stock`: Booleano de stock.
- `product.variants`: Variantes del producto.

### `category`
Disponible en `category.tpl`.
- `category.name`: Nombre de la categoría.
- `category.products`: Lista de productos en la categoría.
- `category.description`: Descripción.

### `cart`
Información del carrito actual.
- `cart.items`: Productos en el carrito.
- `cart.total | money`: Total del carrito.

---

## 🛠️ Métodos y Filtros Comunes

### Filtros
- `| money`: Formatea números como moneda.
- `| translate`: Traduce un string usando `translations.txt`.
- `| default('valor')`: Valor por defecto si la variable es nula/vacía.
- `| resize(width, height)`: Redimensiona imágenes de Tiendanube.
- `| static_url`: Genera la URL para archivos en `static/`.

### Lógica Condicional
```twig
{% if product.display_price %}
  <span class="price">{{ product.price | money }}</span>
{% endif %}
```

### Bucles (Loops)
```twig
{% for item in cart.items %}
  <div class="cart-item">{{ item.name }}</div>
{% endfor %}
```

---

## 🎨 Tipos de Campos en `settings.txt`
- `text`: Campo de texto simple.
- `textarea`: Área de texto.
- `checkbox`: Interruptor booleano.
- `select`: Menú desplegable.
- `image`: Selector de imágenes (requiere `original`).
- `color`: Selector de color hexadecimal.
