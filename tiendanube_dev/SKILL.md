---
name: Tiendanube Dev
description: Arquitecto experto para el desarrollo de temas y secciones en Tiendanube (Twig, settings.txt, Nimbus integration).
---

# 🚀 Skill: Tiendanube Dev (Arquitecto de Experiencias)

Esta skill me convierte en el motor experto de desarrollo para el ecosistema de Tiendanube. Combina el conocimiento del **Theme Base** con las mejores prácticas de **Nimbus Design System** y la flexibilidad de la plataforma.

## 🎯 Protocolos de Desarrollo

### 1. Diagnóstico del Componente

Antes de escribir una sola línea de código, valida estos puntos críticos:

- **Slug Único:** Prefijo para variables, clases y archivos (Ej: `tdv-hero-banner`).
- **Tipo de Sección:** ¿Estática, dinámica (loop) o carrusel (Swiper.js)?
- **Integración con el Admin:** ¿Qué campos serán editables en `settings.txt`?
- **SEO & Responsividad:** ¿Usa etiquetas `h1`-`h6` correctamente? ¿Cómo cambia en móviles (767px)?

### 2. Estructura de Snipplets (.tpl)

Cada sección debe seguir este patrón organizacional:

1.  **Lógica Twig (Data Fetching):** Captura de variables desde `settings` con filtros `| default`.
2.  **Marcado HTML:** Semántica correcta con atributos `data-store`.
3.  **Estilos (CSS):** Uso de variables globales (`--main-foreground`, `--accent-color`).
4.  **Scripts (JS):** Inicialización de sliders o lógica interactiva.

### 2. Entregables Obligatorios (ULTRAMEGA IMPORTANTE)

Para cada nueva sección, es obligatorio generar y/o actualizar:

1.  **Archivo `.tpl`:** El código fuente de la sección en `snipplets/home/`.
2.  **Configuración `settings.txt`:** Definición de campos y tipos para el admin.
3.  **Valores `defaults.txt`:** Datos iniciales para que la sección no se vea vacía.
4.  **Integración `home-section-switch.tpl`:** El bloque `elseif` para que la sección sea elegible y movible en el Home.

---

## 🏗️ Arquitectura de Código En tienda Scatola

### 🎨 Sistema de Diseño (Nimbus & Tokens)

Utilizar siempre los tokens de diseño de Tiendanube para consistencia:

- **Colores:** `--main-foreground`, `--main-background`, `--accent-color`, `--secondary-background`.
- **Tipografía:** `--heading-font`, `--body-font`, `--h1` a `--h6`.
- **Contenedores:** `.container`, `.row`, `.col-12`.
- **Nimbus:** Implementar principios de cohesión visual del sistema de diseño oficial.

### ⚙️ Configuración (settings.txt)

- **Imágenes:** Todo campo `type = image` requiere `original = nombre_campo.jpg`.
- **Grupos:** Organizar secciones por títulos claros en el admin.
- **Indentación:** Obligatorio 4 espacios en sub-propiedades para evitar errores de parseo.

---

## 🛠️ Ejemplos y Referencias

### 📝 Guías y Arquitectura (Referencia Local)

Consulta los recursos especializados para dominar el codigo implementado en la tienda Scatola:

- **Switcher de Inicio:** [home_switcher_guide.md](tiendanube_dev/resources/home_switcher_guide.md)
- **Settings Pro:** [advanced_settings.md](tiendanube_dev/resources/advanced_settings.md)
- **Referencia Twig:** [twig_reference.md](tiendanube_dev/resources/twig_reference.md)
- **Performance & SEO:** [performance_best_practices.md](tiendanube_dev/resources/performance_best_practices.md)
- **Sección Simple:** [crear_seccion_simple.md](tiendanube_dev/workflows/crear_seccion_simple.md)
- **Carrusel (Swiper):** [crear_seccion_carrusel.md](tiendanube_dev/workflows/crear_seccion_carrusel.md)
- **Landing Independiente:** [crear_landing_independiente.md](tiendanube_dev/workflows/crear_landing_independiente.md)
- **Formularios Pro:** [crear_formulario.md](tiendanube_dev/workflows/crear_formulario.md)

### 🔗 Documentación Crítica (Enlaces Externos)

- [Acerca del Theme Base](https://docs.tiendanube.com/help/acerca-del-theme-base)
- [Nuestro Código (Twig, Snipplets, Objetos)](https://docs.tiendanube.com/help/nuestro-codigo)
- [Manual de Funcionalidades & Tutoriales](https://docs.tiendanube.com/help/funcionalidades)
- [DevHub: API Publica y Nimbus](https://dev.nuvemshop.com.br/es/docs/developer-tools/overview)
- [Guía de Personalización de Diseño](https://ayuda.tiendanube.com/es_AR/diseno/guia-personalizar-el-diseno-de-tu-tiendanube)

---

## ⚠️ Checklist Anti-Error 500

- [ ] ¿Están balanceados los `{% if %}` y `{% for %}`?
- [ ] ¿Usaste `~` para concatenación de strings?
- [ ] ¿Están los campos de `settings` definidos en `defaults.txt`?
- [ ] ¿Verificaste `is not empty` antes de acceder a sub-propiedades?
- [ ] ¿Encapsulaste el JS complejo en `{% verbatim %}` si es necesario?
