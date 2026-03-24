---
name: Tiendanube Dev
description: Arquitecto experto para el desarrollo de temas y secciones en Tiendanube (Twig, settings.txt, Nimbus integration).
---

# 🚀 Skill: Tiendanube Dev (Arquitecto de Experiencias)

Motor experto de desarrollo para el ecosistema de Tiendanube. Combina el conocimiento del **Theme Base**, las mejores prácticas de **Nimbus Design System**, y la flexibilidad de **Twig** como motor de plantillas.

## Trigger

Esta skill se activa cuando el usuario necesita desarrollar o modificar una sección del tema de Tiendanube.

## 🎯 Protocolo de Desarrollo

### 1. Diagnóstico del Componente

Antes de escribir código, valida estos puntos:

- **Slug Único:** Prefijo para variables, clases y archivos (Ej: `tdv-hero-banner`).
- **Tipo de Sección:** ¿Estática, dinámica (loop) o carrusel (Swiper.js)?
- **Integración con el Admin:** ¿Qué campos serán editables en `settings.txt`?
- **SEO & Responsividad:** ¿Usa etiquetas `h1`-`h6` correctamente? ¿Cómo cambia en móviles (767px)?

### 2. Anatomía de un Snipplet (.tpl)

Cada sección debe seguir este patrón interno:

1. **Lógica Twig (Data Fetching):** Captura de variables desde `settings` con filtros `| default`.
2. **Marcado HTML:** Semántica correcta con atributos `data-store`.
3. **Estilos (CSS):** Uso de variables globales (`--main-foreground`, `--accent-color`).
4. **Scripts (JS):** Inicialización de sliders o lógica interactiva (encapsular en `{% verbatim %}` si es necesario).

### 3. Entregables Obligatorios (⚠️ ULTRAMEGA IMPORTANTE)

Para **cada nueva sección**, es obligatorio generar y/o actualizar:

| #   | Entregable                    | Descripción                                                            |
| --- | ----------------------------- | ---------------------------------------------------------------------- |
| 1   | **Archivo `.tpl`**            | Código fuente en `snipplets/home/`.                                    |
| 2   | **`settings.txt`**            | Definición de campos y tipos para el admin.                            |
| 3   | **`defaults.txt`**            | Datos iniciales para que la sección no se vea vacía.                   |
| 4   | **`home-section-switch.tpl`** | Bloque `elseif` para que la sección sea elegible y movible en el Home. |

---

## 🏗️ Arquitectura del Theme Base

### 📂 Estructura de Carpetas

| Carpeta      | Propósito                  | Archivos Clave                                                 |
| :----------- | :------------------------- | :------------------------------------------------------------- |
| `/layouts`   | Template principal.        | `layout.tpl` (`{% head_content %}`, `{% template_content %}`). |
| `/templates` | Páginas específicas.       | `home.tpl`, `product.tpl`, `category.tpl`, `cart.tpl`.         |
| `/snipplets` | Componentes reutilizables. | `product_grid.tpl`, `labels.tpl`, `shipping_options.tpl`.      |
| `/static`    | Assets (CSS/JS/Imágenes).  | `checkout.scss.tpl`, `style-colors.scss.tpl`.                  |
| `/config`    | Configuración del Admin.   | `settings.txt`, `translations.txt`, `sections.txt`.            |

### ⚙️ Configuración (`settings.txt`)

- **Tipos:** `checkbox`, `color`, `dropdown`, `image`, `font`, `gallery`.
- **Imágenes:** Todo `type = image` requiere `original = nombre.jpg`.
- **Indentación:** Obligatorio 4 espacios en sub-propiedades.
- **Secciones (`sections.txt`):** Para widgets dinámicos de productos en el Home.
- **Traducciones (`translations.txt`):** Filtro `{{ 'Texto' | translate }}`. La clave debe coincidir con la entrada en español.

### 🎨 Sistema de Diseño (Nimbus & Bootstrap 4)

- **Colores:** `--main-foreground`, `--main-background`, `--accent-color`, `--secondary-background`.
- **Tipografía:** `--heading-font`, `--body-font`, `--h1` a `--h6`.
- **Grid:** Bootstrap 4 (`.container`, `.row`, `.col-*`).
- **CSS Crítico:** `{% include "static/css/style-critical.tpl" %}` en el `<head>`.
- **Carga Asíncrona:** Patrón `load-css-async.tpl` para recursos no críticos.

### 🧩 Inclusión Modular de Componentes

| Método                                          | Cuándo Usarlo                                         |
| :---------------------------------------------- | :---------------------------------------------------- |
| `{% snipplet "file.tpl" %}`                     | Inclusión rápida desde `/snipplets`.                  |
| `{% include "path/file.tpl" with {var: val} %}` | Pasar variables específicas al componente.            |
| `{% embed "file.tpl" %}`                        | Sobreescribir bloques (`{% block %}`) del componente. |

---

## 📚 Base de Conocimiento

### 🔬 Referencias Técnicas (`resources/`)

| Recurso                                                                  | Descripción                                                       |
| :----------------------------------------------------------------------- | :---------------------------------------------------------------- |
| [twig_reference.md](resources/twig_reference.md)                         | Objetos globales, filtros, funciones y mejores prácticas de Twig. |
| [theme_base_architecture.md](resources/theme_base_architecture.md)       | Carpetas, configuración avanzada y performance.                   |
| [advanced_settings.md](resources/advanced_settings.md)                   | Guía avanzada de `settings.txt`.                                  |
| [home_switcher_guide.md](resources/home_switcher_guide.md)               | Switcher de secciones del Home.                                   |
| [performance_best_practices.md](resources/performance_best_practices.md) | Performance y SEO.                                                |
| [personalizar_item_menu.md](resources/personalizar_item_menu.md)         | Personalización de menús.                                         |

### 💎 Ejemplos y Patrones (`examples/`)

| Recurso                                                       | Descripción                                                    |
| :------------------------------------------------------------ | :------------------------------------------------------------- |
| [section_patterns.md](examples/section_patterns.md)           | Patrones de diseño para secciones (Banners, AJAX, Navegación). |
| [custom_banner_section.md](examples/custom_banner_section.md) | Ejemplo completo de sección de banner personalizado.           |

### 🔧 Workflows (Paso a Paso)

| Workflow                                                                   | Descripción                            |
| :------------------------------------------------------------------------- | :------------------------------------- |
| [crear_seccion_simple.md](resources/crear_seccion_simple.md)               | Crear una sección estática desde cero. |
| [crear_seccion_carrusel.md](resources/crear_seccion_carrusel.md)           | Crear un carrusel con Swiper.js.       |
| [crear_landing_independiente.md](resources/crear_landing_independiente.md) | Crear una landing page independiente.  |
| [crear_formulario.md](resources/crear_formulario.md)                       | Crear formularios avanzados.           |

### 🔗 Documentación Externa

- [DevHub: API Publica y Nimbus](https://dev.nuvemshop.com.br/es/docs/developer-tools/overview)

---

## ⚠️ Checklist Anti-Error 500

Antes de entregar cualquier código, verificar:

- [ ] ¿Están balanceados los `{% if %}` y `{% for %}`?
- [ ] ¿Usaste `~` para concatenación de strings?
- [ ] ¿Están los campos de `settings` definidos en `defaults.txt`?
- [ ] ¿Verificaste `is not empty` antes de acceder a sub-propiedades?
- [ ] ¿Encapsulaste el JS complejo en `{% verbatim %}` si es necesario?
- [ ] ¿El `home-section-switch.tpl` incluye el nuevo bloque `elseif`?
- [ ] ¿Las imágenes en `settings.txt` tienen `original = nombre.jpg`?
