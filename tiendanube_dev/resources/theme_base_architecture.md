# Referencia Técnica: Arquitectura Theme Base

Esta guía detalla la infraestructura y reglas del **Theme Base** de Tiendanube para el desarrollo de temas y secciones.

## 📂 Estructura de Carpetas

Es fundamental respetar la organización de archivos para que la plataforma procese correctamente el tema:

| Carpeta | Propósito | Archivos Clave |
| :--- | :--- | :--- |
| `/layouts` | Estructura general (Template Engine). | `layout.tpl` (Contiene `{% head_content %}` y `{% template_content %}`). |
| `/templates` | Lógica de páginas específicas. | `home.tpl`, `product.tpl`, `category.tpl`, `cart.tpl`. |
| `/snipplets` | Componentes reutilizables. | `product_grid.tpl`, `labels.tpl`, `shipping_options.tpl` (AJAX). |
| `/static` | Assets (CSS/JS/Imágenes). | `checkout.scss.tpl` (Debe estar aquí para ser detectado). |
| `/config` | Configuración del Admin. | `settings.txt`, `translations.txt`, `sections.txt`. |

---

## ⚙️ Configuración Avanzada (`/config`)

### 📝 mappings en `settings.txt`
Define la interfaz del administrador. Tipos comunes:
- `checkbox`, `color`, `dropdown`, `image`, `font`.
- `gallery`: Para sliders dinámicos configurables.
- **Regla Crítica:** Imágenes requieren `original = nombre.jpg` para ser procesadas.

### 🧩 Herencia y Widgets (`sections.txt`)
Utilizado para declarar widgets de productos en el Home (Destacados, Ofertas). Permite que el mercader elija qué categorías mostrar dinámicamente.

### 🌐 Internacionalización (`translations.txt`)
- **Filtro Twig:** `{{ 'Texto en Español' | translate }}`.
- **Regla:** La clave debe existir en `translations.txt` bajo la entrada en español para ser traducida a otros idiomas en el frontend.

---

## 🎨 Sistema de Diseño y Performance

- **Framework:** Basado en Bootstrap 4 (`.container`, `.row`, `.col-*`).
- **CSS Crítico:** Incluir estilos vitales en `<style>` mediante `{% include "static/css/style-critical.tpl" %}` dentro del `<head>` para evitar Render-Blocking.
- **Carga Asíncrona:** Usar el patrón `load-css-async.tpl` para recursos no críticos.
- **Preview en Vivo:** Definir variables en `style-colors.scss.tpl` para que el sistema de Tiendanube detecte cambios en tiempo real desde el admin.
