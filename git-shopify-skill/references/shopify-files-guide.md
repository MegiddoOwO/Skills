# Guía de Archivos Shopify — Referencia para Commits

## Estructura típica de un tema Shopify

```
theme/
├── assets/          → JS, CSS, imágenes, fuentes
├── config/          → settings_schema.json, settings_data.json
├── layout/          → theme.liquid, password.liquid
├── locales/         → es.json, en.json (traducciones)
├── sections/        → secciones reutilizables (.liquid)
├── snippets/        → fragmentos reutilizables (.liquid)
├── templates/       → plantillas de página (.liquid o .json)
└── README.md
```

---

## Ejemplos de commits por área

### Layout
```
style(theme.liquid): Agregar fuente personalizada en head del tema
feat(theme.liquid): Integrar script de chat en vivo en layout principal
fix(password.liquid): Corregir redirección en página de contraseña
```

### Sections
```
feat(hero-banner.liquid): Crear sección de banner con video de fondo
style(announcement-bar.liquid): Ajustar altura y animación de barra de anuncios
fix(featured-collection.liquid): Corregir número de columnas en móvil
refactor(header.liquid): Reorganizar lógica del menú de navegación
```

### Snippets
```
feat(product-card.liquid): Agregar etiqueta de descuento en tarjeta de producto
fix(cart-item.liquid): Corregir visualización de variantes sin imagen
style(breadcrumb.liquid): Actualizar separador y color de migas de pan
```

### Templates
```
feat(product.json): Agregar sección de productos relacionados al template
chore(collection.json): Actualizar orden de secciones en página de colección
feat(page.about.liquid): Crear template personalizado para página "Acerca de"
```

### Assets — JavaScript
```
feat(cart-drawer.js): Implementar apertura automática del carrito al agregar producto
fix(product-form.js): Corregir selección de variante al cambiar color
refactor(filters.js): Optimizar lógica de filtros AJAX en colección
```

### Assets — CSS/SCSS
```
style(base.css): Actualizar variables de colores del tema
style(product-page.css): Mejorar diseño responsivo de galería de imágenes
style(cart.css): Rediseñar drawer del carrito para móvil
```

### Config
```
chore(settings_schema.json): Agregar opción de color para sección hero
chore(settings_data.json): Actualizar configuración de tipografía del tema
```

### Locales
```
chore(es.json): Agregar traducciones para nuevos textos del carrito
chore(en.json): Corregir texto del botón de checkout
```

---

## Situaciones comunes en Shopify y qué tipo usar

| Situación                                      | Tipo        |
|------------------------------------------------|-------------|
| Nueva sección desde cero                       | `feat`      |
| Agregar opción a settings_schema               | `chore`     |
| Corregir bug en carrito                        | `fix`       |
| Cambiar colores / fuentes / espaciado          | `style`     |
| Integrar app de terceros (reviews, chat, etc.) | `feat`      |
| Traducir textos en locales                     | `chore`     |
| Mejorar rendimiento (lazy load, etc.)          | `refactor`  |
| Limpiar código sin cambiar funcionalidad       | `refactor`  |
| Actualizar README o documentación interna      | `docs`      |
| Cambiar metafields o configuraciones           | `chore`     |
