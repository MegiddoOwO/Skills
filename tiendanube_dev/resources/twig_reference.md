# Referencia Técnica: Twig en Tiendanube

Twig es el motor de plantillas utilizado por Tiendanube. Esta guía detalla los objetos globales, filtros de sistema y métodos de inclusión para el desarrollo de temas profesionales.

## 📦 Objetos Globales y Propiedades

### 🏪 `store` (La Tienda)
- `store.name`: Nombre comercial.
- `store.url`: URL base de la tienda.
- `store.logo`, `store.favicon`: URLs de los archivos de marca.
- `store.email`, `store.phone`, `store.address`.
- `store.social_networks`: Objeto con `facebook`, `instagram`, `twitter`, `pinterest`, `blog`.
- `store.customer_accounts_enabled`: Booleano para lógica de login.

### 🌐 Variables Globales de Contexto
- `current_url`: URL completa de la página actual.
- `page_title`: Título para el tag `<title>`.
- `page_description`: Contenido para meta descripción.
- `template`: Nombre del template actual (e.g., `home`, `product`, `cart`, `search`).
- `current_language.name`, `current_language.lang`: Datos del idioma activo.

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
- `cart.items`: Lista de productos agregados (`Cart_item`).
- `cart.total`, `cart.subtotal`: Montos acumulados.
- `cart.items_count`: Cantidad total de artículos.
- `cart.promos`: Lista de promociones aplicadas (e.g., "3x2").
- `cart.shipping_cost`: Costo de envío calculado.

### 👤 `customer` & `order`
- `customer.name`, `customer.email`, `customer.order_count`.
- `order.number`, `order.status`, `order.payment_status`, `order.shipping_status`.

### 🗺️ Navegación y Estructura
- `navigation`: Array de links para menús (con `name`, `url`, `subitems`, `current`).
- `breadcrumbs`: Lista de niveles para la ruta de navegación (con `name`, `url`, `last`).

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
