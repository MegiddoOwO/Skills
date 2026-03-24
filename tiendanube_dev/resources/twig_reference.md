# Referencia Técnica: Twig en Tiendanube

Twig es el motor de plantillas utilizado por Tiendanube. Esta guía detalla los objetos globales, filtros de sistema y métodos de inclusión para el desarrollo de temas profesionales.

## 📦 Objetos Globales y Propiedades

### 🏪 `store` (La Tienda)
- `store.name`: Nombre comercial.
- `store.url`: URL base de la tienda.
- `store.logo`: URL del logo cargado en el admin.
- `store.contact_email`, `store.address`, `store.phone`.
- `store.social_networks`: Objeto con enlaces a Facebook, Instagram, Twitter, etc.

### 🏷️ `product` (El Producto)
- `product.name`: Título del producto.
- `product.description`: Contenido HTML de la descripción.
- `product.price | money`: Precio actual formateado.
- `product.compare_at_price | money`: Precio original (tachar).
- `product.images`: Lista de objetos de imagen.
- `product.has_stock`: Booleano de disponibilidad.
- `product.variants`: Lista de variantes (color, talle).
- `product.url`: URL de la página de detalles.

### 🛒 `cart` (El Carrito)
- `cart.items`: Lista de productos agregados.
- `cart.total | money`: Suma total de los productos.
- `cart.items_count`: Cantidad total de artículos.

### 👤 `customer` & `order`
- `customer.name`, `customer.email`: Datos del usuario logueado.
- `order.number`, `order.status`: Datos tras una compra.

---

## 🛠️ Filtros y Funciones de Tiendanube

### 🖼️ Manejo de Imágenes
- `product_image_url(size)`: Genera la URL de la imagen del producto. 
  - *Tamaños:* `tiny`, `small`, `medium`, `large`, `huge`, `original`.
- `| resize(width, height)`: Redimensiona imágenes generales.

### 🔗 Assets y Recursos
- `| static_url`: Genera la URL para archivos en la carpeta `/static`.
- `css_tag`: Función para generar el tag `<link rel="stylesheet">`.
- `js_tag`: Función para generar el tag `<script src="...">`.

### 💰 Formatos y Traducción
- `| money`: Aplica el formato de moneda de la tienda.
- `| translate` (o `| t`): Traduce un texto basado en `config/translations.txt`.
- `| default('valor')`: Proporciona un fallback si la variable está vacía.

---

## 🏗️ Métodos de Inclusión Modular

| Método | Uso Recomendado |
| :--- | :--- |
| `{% snipplet "file.tpl" %}` | Inclusión rápida de la carpeta `/snipplets`. No requiere ruta completa. |
| `{% include "path/to/file.tpl" with {var: val} %}` | Inclusión estándar pasando variables específicas. Requiere ruta desde la raíz. |
| `{% embed "file.tpl" %}` | Permite sobreescribir bloques (`{% block %}`) dentro del archivo incluido. |

---

## 💡 Mejores Prácticas de Twig
- **Defensa:** Usar `{% if var is defined %}` e `{% if list is not empty %}` antes de renderizar.
- **Rendimiento:** Utilizar `{% cache %}` en bloques de código pesados que no cambian frecuentemente.
- **Seguridad:** Usar `| escape` o `| e` para sanitizar entradas de usuario si es necesario, aunque Tiendanube escapa la mayoría automáticamente.
