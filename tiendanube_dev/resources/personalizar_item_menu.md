---
description: Personalización de un elemento específico del menú de navegación
---

## 🎨 Ítem de Menú Personalizado

Pasos para aplicar estilos únicos a un botón específico del menú:

1. **Añadir Clase de Identificación (`snipplets/navigation/navigation-nav-list.tpl`)**

   ```twig
   {# Dentro del bucle de navegación #}
   {% set nombre_limpio = item.name | upper %}
   <li class="nav-item {% if nombre_limpio == '{TEXTO_DEL_BOTON}' %}nav-item-destacado{% endif %}">
       <a class="nav-link">
           {{ item.name }}
       </a>
   </li>
   ```

2. **Estilos Específicos (`static/css/custom.css`)**
   Aplicar el diseño usando el selector de alta prioridad:

   ```css
   .nav-desktop-list .nav-item-destacado .nav-link {
     color: var(--accent-color) !important;
     font-family: "Patrick Hand", cursive !important;
     font-size: 1.1rem !important;
   }

   /* Selector para menú móvil */
   .modal-nav-hamburger .nav-item-destacado .nav-link {
     color: var(--accent-color) !important;
   }
   ```

3. **Fuentes:** Si usas fuentes especiales como Patrick Hand, asegúrate de que el archivo `.woff2` esté en `static/fonts/` y cargado mediante `@font-face` en los estilos globales.


---

# Guía: Personalizar un Elemento Específico del Menú de Navegación

Esta guía explica cómo personalizar el estilo (color, fuente, tamaño, negrita) de un elemento específico del menú de navegación sin afectar los demás elementos.

## 📋 Caso de Uso

Personalizar el elemento "EMPRENDE" en el menú principal con:
- Color rosa personalizado
- Fuente handwritten (Patrick Hand)
- Tamaño más grande (1.65em)
- Negrita (font-weight: 700)

## 🔧 Pasos para Implementar

### 1. Modificar el Template de Navegación

**Archivo:** `snipplets/navigation/navigation-nav-list.tpl`

Agregar lógica para detectar el elemento específico y asignar clases CSS personalizadas:

```twig
{% for item in navigation %}
    {# Detectar el elemento específico (ejemplo: EMPRENDE) #}
    {% set is_emprende = item.name | upper == 'EMPRENDE' or item.name | upper == 'EMPRENDA' or 'EMPRENDE' in (item.name | upper) %}
    
    {% if item.subitems %}
        <li class="... nav-item {% if is_emprende %}nav-item-emprende{% endif %}" data-component="menu.item">
            <a class="... nav-list-link ... {% if is_emprende %}nav-link-emprende{% endif %}" href="...">
                {{ item.name }}
            </a>
            {# ... resto del código ... #}
        </li>
    {% else %}
        {% set is_emprende = item.name | upper == 'EMPRENDE' or item.name | upper == 'EMPRENDA' or 'EMPRENDE' in (item.name | upper) %}
        <li class="... nav-item {% if is_emprende %}nav-item-emprende{% endif %}" data-component="menu.item">
            <a class="nav-list-link ... {% if is_emprende %}nav-link-emprende{% endif %}" href="...">
                {{ item.name }}
            </a>
        </li>
    {% endif %}
{% endfor %}
```

**Nota:** Reemplazar `EMPRENDE` y `emprende` con el nombre del elemento que deseas personalizar.

### 2. Agregar Google Fonts (si es necesario)

**Archivo:** `layouts/layout.tpl`

Si necesitas una fuente personalizada de Google Fonts, agregar en la sección `<head>`:

```twig
{# Google Fonts - Nombre de la fuente #}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nombre+Fuente&display=swap" rel="stylesheet">
```

**Ejemplo con Patrick Hand:**
```twig
<link href="https://fonts.googleapis.com/css2?family=Patrick+Hand&display=swap" rel="stylesheet">
```

### 3. Agregar Estilos CSS

#### Opción A: Archivo CSS Personalizado

**Archivo:** `static/css/custom.css`

```css
/*============================================================================
  Estilo específico para [NOMBRE_ELEMENTO] en el menú principal
==============================================================================*/

/* Estilo para el enlace en el menú de navegación DESKTOP - Alta especificidad */
.head-main .nav-desktop-list .nav-item-[nombre] .nav-link-[nombre],
.head-main .nav-desktop-list .nav-link-[nombre],
.nav-desktop-list .nav-item-[nombre] .nav-link-[nombre],
.nav-desktop-list .nav-link-[nombre] {
  color: #ff6b9d !important;                    /* Color personalizado */
  font-weight: 700 !important;                  /* Negrita (400=normal, 700=bold) */
  font-size: 1.65em !important;                 /* Tamaño (1em=normal, 1.65em=65% más grande) */
  font-family: 'Patrick Hand', cursive !important; /* Fuente personalizada */
  font-style: normal !important;
  text-decoration: none !important;
}

/* Hover state para DESKTOP - Alta especificidad */
.head-main .nav-desktop-list .nav-item-[nombre] .nav-link-[nombre]:hover,
.head-main .nav-desktop-list .nav-link-[nombre]:hover,
.nav-desktop-list .nav-item-[nombre] .nav-link-[nombre]:hover,
.nav-desktop-list .nav-link-[nombre]:hover {
  color: #ff4d8a !important;                    /* Color hover (más oscuro) */
  text-decoration: none !important;
}

/*============================================================================
  Estilo específico para [NOMBRE_ELEMENTO] en el menú móvil (Hamburger)
==============================================================================*/

/* Estilo para el enlace en el menú móvil - Alta especificidad */
.modal-nav-hamburger .nav-item-[nombre] .nav-link-[nombre],
.modal-nav-hamburger .nav-link-[nombre],
.nav-list-panel .nav-item-[nombre] .nav-link-[nombre],
.nav-list-panel .nav-link-[nombre],
.nav-body .nav-item-[nombre] .nav-link-[nombre],
.nav-body .nav-link-[nombre] {
  color: #ff6b9d !important;                    /* Color personalizado */
  font-weight: 700 !important;                  /* Negrita */
  font-size: 1.65em !important;                 /* Tamaño */
  font-family: 'Patrick Hand', cursive !important; /* Fuente personalizada */
  font-style: normal !important;
  text-decoration: none !important;
}

/* Hover state para MÓVIL - Alta especificidad */
.modal-nav-hamburger .nav-item-[nombre] .nav-link-[nombre]:hover,
.modal-nav-hamburger .nav-link-[nombre]:hover,
.nav-list-panel .nav-item-[nombre] .nav-link-[nombre]:hover,
.nav-list-panel .nav-link-[nombre]:hover,
.nav-body .nav-item-[nombre] .nav-link-[nombre]:hover,
.nav-body .nav-link-[nombre]:hover {
  color: #ff4d8a !important;                    /* Color hover */
  text-decoration: none !important;
}
```

#### Opción B: CSS Inline en Layout (Recomendado para asegurar carga)

**Archivo:** `layouts/layout.tpl`

Agregar en la sección `<head>`, después de los otros estilos:

```twig
{# Estilo específico para [NOMBRE_ELEMENTO] en el menú - Inline para asegurar carga #}
<style>
    /* Estilo para el enlace en el menú de navegación DESKTOP - Alta especificidad */
    .head-main .nav-desktop-list .nav-item-[nombre] .nav-link-[nombre],
    .head-main .nav-desktop-list .nav-link-[nombre],
    .nav-desktop-list .nav-item-[nombre] .nav-link-[nombre],
    .nav-desktop-list .nav-link-[nombre] {
        color: #ff6b9d !important;
        font-weight: 700 !important;
        font-size: 1.65em !important;
        font-family: 'Patrick Hand', cursive !important;
        font-style: normal !important;
        text-decoration: none !important;
    }

    /* Hover state para DESKTOP - Alta especificidad */
    .head-main .nav-desktop-list .nav-item-[nombre] .nav-link-[nombre]:hover,
    .head-main .nav-desktop-list .nav-link-[nombre]:hover,
    .nav-desktop-list .nav-item-[nombre] .nav-link-[nombre]:hover,
    .nav-desktop-list .nav-link-[nombre]:hover {
        color: #ff4d8a !important;
        text-decoration: none !important;
    }

    /* Estilo para el enlace en el menú móvil (Hamburger) - Alta especificidad */
    .modal-nav-hamburger .nav-item-[nombre] .nav-link-[nombre],
    .modal-nav-hamburger .nav-link-[nombre],
    .nav-list-panel .nav-item-[nombre] .nav-link-[nombre],
    .nav-list-panel .nav-link-[nombre],
    .nav-body .nav-item-[nombre] .nav-link-[nombre],
    .nav-body .nav-link-[nombre] {
        color: #ff6b9d !important;
        font-weight: 700 !important;
        font-size: 1.65em !important;
        font-family: 'Patrick Hand', cursive !important;
        font-style: normal !important;
        text-decoration: none !important;
    }

    /* Hover state para MÓVIL - Alta especificidad */
    .modal-nav-hamburger .nav-item-[nombre] .nav-link-[nombre]:hover,
    .modal-nav-hamburger .nav-link-[nombre]:hover,
    .nav-list-panel .nav-item-[nombre] .nav-link-[nombre]:hover,
    .nav-list-panel .nav-link-[nombre]:hover,
    .nav-body .nav-item-[nombre] .nav-link-[nombre]:hover,
    .nav-body .nav-link-[nombre]:hover {
        color: #ff4d8a !important;
        text-decoration: none !important;
    }
</style>
```

### 4. Cargar el Archivo CSS Personalizado (si usas Opción A)

**Archivo:** `layouts/layout.tpl`

Agregar después de los otros estilos CSS:

```twig
{# Custom CSS file #}
{{ 'css/custom.css' | static_url | static_inline }}
```

## 🎨 Personalización de Propiedades

### Color
```css
color: #ff6b9d !important;  /* Color hexadecimal */
color: rgb(255, 107, 157) !important;  /* RGB */
color: rgba(255, 107, 157, 1) !important;  /* RGBA con transparencia */
```

### Tamaño de Fuente
```css
font-size: 1em !important;      /* Tamaño normal */
font-size: 1.15em !important;  /* 15% más grande */
font-size: 1.3em !important;   /* 30% más grande */
font-size: 1.65em !important;  /* 65% más grande */
font-size: 18px !important;    /* Tamaño fijo en píxeles */
```

### Peso de Fuente (Negrita)
```css
font-weight: 400 !important;  /* Normal */
font-weight: 500 !important;  /* Medium */
font-weight: 600 !important;  /* Semi-bold */
font-weight: 700 !important;  /* Bold (negrita) */
font-weight: 800 !important;  /* Extra-bold */
font-weight: 900 !important;  /* Black */
```

### Fuente Personalizada
```css
/* Fuente del sistema */
font-family: 'Arial', sans-serif !important;

/* Google Fonts */
font-family: 'Patrick Hand', cursive !important;
font-family: 'Roboto', sans-serif !important;
font-family: 'Open Sans', sans-serif !important;

/* Múltiples fuentes (fallback) */
font-family: 'Patrick Hand', 'Comic Sans MS', cursive, sans-serif !important;
```

### Otros Estilos
```css
font-style: italic !important;     /* Cursiva */
text-decoration: underline !important;  /* Subrayado */
text-transform: uppercase !important;    /* Mayúsculas */
letter-spacing: 2px !important;   /* Espaciado entre letras */
```

## 📝 Ejemplo Completo: Personalizar "CONTACTO"

### 1. Template (`navigation-nav-list.tpl`)
```twig
{% set is_contacto = item.name | upper == 'CONTACTO' or 'CONTACTO' in (item.name | upper) %}
<li class="... nav-item {% if is_contacto %}nav-item-contacto{% endif %}">
    <a class="nav-list-link ... {% if is_contacto %}nav-link-contacto{% endif %}" href="...">
        {{ item.name }}
    </a>
</li>
```

### 2. CSS (`custom.css` o inline)
```css
.nav-desktop-list .nav-link-contacto {
  color: #007bff !important;           /* Azul */
  font-weight: 600 !important;        /* Semi-bold */
  font-size: 1.2em !important;         /* 20% más grande */
  font-family: 'Roboto', sans-serif !important;
}
```

## ⚠️ Notas Importantes

1. **Especificidad CSS**: Los selectores con mayor especificidad (más clases anidadas) tienen prioridad. Por eso usamos `.head-main .nav-desktop-list .nav-link-[nombre]` en lugar de solo `.nav-link-[nombre]`.

2. **!important**: Se usa `!important` para sobrescribir estilos del tema base que tienen alta especificidad.

3. **Desktop y Móvil**: Asegúrate de agregar estilos tanto para desktop (`.nav-desktop-list`) como para móvil (`.modal-nav-hamburger`, `.nav-list-panel`).

4. **Detección del Elemento**: La lógica de detección en el template debe ser flexible para capturar variaciones del nombre (mayúsculas, minúsculas, acentos, etc.).

5. **Caché del Navegador**: Después de hacer cambios, recarga la página con `Ctrl+F5` (Windows) o `Cmd+Shift+R` (Mac) para limpiar la caché.

## 🔍 Verificación

Para verificar que los estilos se aplicaron correctamente:

1. **Inspeccionar Elemento**: Abre las herramientas de desarrollador (F12) y busca el elemento en el HTML.
2. **Verificar Clases**: Confirma que las clases `nav-item-[nombre]` y `nav-link-[nombre]` están presentes.
3. **Verificar Estilos**: En la pestaña "Computed" o "Estilos", verifica que tus estilos CSS se están aplicando.
4. **Probar Desktop y Móvil**: Verifica que los estilos funcionan tanto en desktop como en móvil.

## 📚 Referencias

- **Google Fonts**: https://fonts.google.com/
- **Colores Hexadecimales**: https://htmlcolorcodes.com/
- **Especificidad CSS**: https://developer.mozilla.org/es/docs/Web/CSS/Specificity

---

**Última actualización:** 2024
**Versión:** 1.0



---

# 🎯 Guía: Centrar Menú de Navegación en Desktop

## 📋 Descripción

Esta guía documenta cómo se implementó el centrado del menú de navegación en desktop y cómo aplicar este mismo cambio en futuras páginas o temas.

---

## 🔍 Implementación Actual

### Ubicación del Código

El centrado del menú se implementa en el archivo:
- **Archivo**: `snipplets/header/header.tpl`
- **Línea**: 188

### Código Implementado

```188:190:snipplets/header/header.tpl
<div class="container {{ show_block_desktop_hide_mobile_class }} {% if settings.logo_position_desktop == 'center' %}text-center{% endif %}">
    {% snipplet "navigation/navigation.tpl" %}
</div>
```

### Explicación

El centrado se logra mediante:

1. **Condición**: Se verifica si `settings.logo_position_desktop == 'center'`
2. **Clase aplicada**: Cuando la condición es verdadera, se aplica la clase `text-center`
3. **Resultado**: La clase `text-center` (de Bootstrap/estilos del tema) centra el contenido del contenedor, lo que a su vez centra el menú de navegación

### Estructura del Menú

El menú de navegación se renderiza dentro de un contenedor que:
- Solo se muestra en desktop (`show_block_desktop_hide_mobile_class`)
- Está dentro de un `container` para mantener el ancho máximo
- Se centra cuando el logo está configurado en posición `center` en desktop

---

## 🚀 Cómo Aplicar en Futuras Páginas

### Opción 1: Usar la Misma Lógica (Recomendado)

Si necesitas centrar el menú en otra página que use el mismo header, simplemente asegúrate de que:

1. **Configuración en Tiendanube**: 
   - Ve a **Diseño > Configuración del tema**
   - Configura `logo_position_desktop` en `center`

2. **El código ya está implementado**: 
   - El archivo `snipplets/header/header.tpl` ya contiene la lógica
   - Se aplicará automáticamente cuando la configuración esté en `center`

### Opción 2: Aplicar Manualmente en un Template Específico

Si necesitas centrar el menú solo en una página específica sin cambiar la configuración global:

1. **Localiza el template** donde quieres aplicar el cambio (ej: `templates/page.tpl`, `templates/category.tpl`, etc.)

2. **Busca la sección del header** o donde se incluye la navegación

3. **Aplica la clase `text-center`** al contenedor del menú:

```twig
<div class="container d-none d-md-block text-center">
    {% snipplet "navigation/navigation.tpl" %}
</div>
```

### Opción 3: Crear un Snippet Reutilizable

Si necesitas reutilizar esta funcionalidad en múltiples lugares:

1. **Crea un nuevo snippet** (opcional): `snipplets/navigation/navigation-centered.tpl`

```twig
{% set header_left_with_big_search = settings.logo_position_desktop == 'left' and settings.search_big_desktop %}
<div class="nav-desktop {% if header_left_with_big_search %}nav-desktop-left{% endif %}">
    <ul class="js-nav-desktop-list nav-desktop-list text-center" data-store="navigation" data-component="menu">
        <span class="js-nav-desktop-list-arrow js-nav-desktop-list-arrow-left nav-desktop-list-arrow nav-desktop-list-arrow-left disable" style="display: none">
            <svg class="icon-inline icon-lg icon-flip-horizontal"><use xlink:href="#chevron"/></svg>
        </span>
        {% include 'snipplets/navigation/navigation-nav-list.tpl' with {'megamenu' : true } %}
        <span class="js-nav-desktop-list-arrow js-nav-desktop-list-arrow-right nav-desktop-list-arrow nav-desktop-list-arrow-right" style="display: none">
            <svg class="icon-inline icon-lg"><use xlink:href="#chevron"/></svg>
        </span>
    </ul>
</div>
```

2. **Úsalo en el template** donde lo necesites:

```twig
<div class="container d-none d-md-block">
    {% snipplet "navigation/navigation-centered.tpl" %}
</div>
```

---

## 🎨 Estilos CSS Relacionados

### Clase `text-center`

La clase `text-center` está definida en los estilos del tema y aplica:

```css
.text-center {
    text-align: center !important;
}
```

### Estilos del Menú Desktop

Los estilos principales del menú desktop están en:
- **Archivo**: `static/css/style-critical.scss`
- **Líneas**: 1416-1520

```1416:1428:static/css/style-critical.scss
.nav-desktop {
  position: relative;
  width: 100%;
  height: 100%;
}

.nav-desktop-list {
  height: 100%;
  margin: 0;
  padding: 20px 0;
  list-style: none;
  white-space: nowrap!important;
}
```

---

## ✅ Checklist para Aplicar el Cambio

- [ ] Identificar la página/template donde se necesita centrar el menú
- [ ] Verificar si la configuración global (`logo_position_desktop == 'center'`) es suficiente
- [ ] Si no, aplicar la clase `text-center` manualmente en el contenedor del menú
- [ ] Verificar que el menú se centra correctamente en desktop (pantallas > 768px)
- [ ] Verificar que no afecta el diseño en mobile
- [ ] Probar en diferentes tamaños de pantalla

---

## 🔧 Variables y Configuraciones

### Variable de Configuración

- **Variable**: `settings.logo_position_desktop`
- **Valores posibles**: `'left'` | `'center'`
- **Ubicación**: Configuración del tema en Tiendanube

### Clases CSS Utilizadas

- `text-center`: Centra el texto/contenido
- `show_block_desktop_hide_mobile_class`: Muestra solo en desktop (`d-none d-md-block`)
- `container`: Limita el ancho máximo y centra el contenedor

---

## 🐛 Problemas Comunes y Soluciones

### Problema 1: El menú no se centra

**Solución**: 
- Verifica que la clase `text-center` esté aplicada al contenedor correcto
- Asegúrate de que el contenedor tenga `display: block` o `display: flex` con `justify-content: center`

### Problema 2: El menú se centra pero los items están alineados a la izquierda

**Solución**: 
- Verifica que `nav-desktop-list` tenga `text-align: center` o que los items estén dentro de un contenedor centrado
- Puede ser necesario agregar estilos adicionales:

```css
.nav-desktop-list.text-center {
  text-align: center;
}
```

### Problema 3: El centrado afecta el diseño en mobile

**Solución**: 
- Usa clases responsive: `text-center` solo en desktop con `text-md-center`
- O usa la clase condicional `show_block_desktop_hide_mobile_class` para que solo se aplique en desktop

---

## 📝 Notas Adicionales

- El centrado funciona mejor cuando el logo está en posición `center` en desktop
- Si el logo está en `left`, el menú normalmente se muestra al lado del logo, no debajo
- La clase `text-center` es una utilidad de Bootstrap que se puede sobrescribir con estilos personalizados si es necesario

---

## 🔗 Archivos Relacionados

- `snipplets/header/header.tpl` - Header principal donde se aplica el centrado
- `snipplets/navigation/navigation.tpl` - Componente del menú de navegación
- `snipplets/navigation/navigation-nav-list.tpl` - Lista de items del menú
- `static/css/style-critical.scss` - Estilos del menú desktop

---

**Última actualización**: 2024
**Versión del tema**: Scatola



---

# Documentación: Aplicación de Color y Cambio de Fuente en el Menú Principal de EMPRENDE

Este documento describe cómo se implementó la personalización del elemento "EMPRENDE" en el menú principal de navegación, aplicando un color rosa personalizado y la fuente "Patrick Hand" (handwritten).

---

## 📋 Objetivo

Personalizar visualmente el elemento "EMPRENDE" en el menú de navegación para destacarlo del resto de elementos del menú, aplicando:
- **Color**: Rosa personalizado (#ff6b9d)
- **Fuente**: Patrick Hand (handwritten/cursiva)
- **Tamaño**: 1.65em (65% más grande que el tamaño normal)
- **Peso**: 700 (negrita)
- **Hover**: Color más oscuro (#ff4d8a)

---

## 🔧 Archivos Modificados

La implementación requirió modificar **3 archivos principales**:

1. **`snipplets/navigation/navigation-nav-list.tpl`** - Detección y asignación de clases CSS
2. **`layouts/layout.tpl`** - Carga de Google Fonts y estilos inline
3. **`static/css/custom.css`** - Estilos CSS para desktop y móvil

---

## 📝 Implementación Detallada

### Paso 1: Detección del Elemento en el Template de Navegación

**Archivo:** `snipplets/navigation/navigation-nav-list.tpl`

Se agregó lógica para detectar cuando un elemento del menú es "EMPRENDE" y asignarle clases CSS específicas.

#### Código Implementado:

```6:6:snipplets/navigation/navigation-nav-list.tpl
{% set is_emprende = item.name | upper == 'EMPRENDE' or item.name | upper == 'EMPRENDA' or 'EMPRENDE' in (item.name | upper) %}
```

Esta línea detecta el elemento "EMPRENDE" considerando variaciones como:
- "EMPRENDE" (mayúsculas)
- "Emprende" (capitalizado)
- "EMPRENDA" (variante en portugués)
- Cualquier texto que contenga "EMPRENDE"

#### Aplicación de Clases CSS:

**Para elementos con subitems:**
```8:12:snipplets/navigation/navigation-nav-list.tpl
<li class="{% if megamenu %}js-desktop-nav-item js-item-subitems-desktop nav-item-desktop {% if not subitem %}js-nav-main-item nav-dropdown nav-main-item {% endif %}{% endif %} nav-item item-with-subitems {% if is_emprende %}nav-item-emprende{% endif %}" data-component="menu.item">
			{% if megamenu %}
			<div class="nav-item-container">
			{% endif %}
				<a class="{% if hamburger %}js-toggle-menu-panel align-items-center{% endif %} nav-list-link position-relative {{ item.current ? 'selected' : '' }} {% if is_emprende %}nav-link-emprende{% endif %}" href="{% if megamenu and item.url %}{{ item.url }}{% else %}#{% endif %}">{{ item.name }}
```

**Para elementos sin subitems:**
```72:74:snipplets/navigation/navigation-nav-list.tpl
{% set is_emprende = item.name | upper == 'EMPRENDE' or item.name | upper == 'EMPRENDA' or 'EMPRENDE' in (item.name | upper) %}
		<li class="js-desktop-nav-item {% if megamenu %}{% if not subitem %}js-nav-main-item nav-main-item{% endif %} nav-item-desktop{% endif %} nav-item {% if is_emprende %}nav-item-emprende{% endif %}" data-component="menu.item">
			<a class="nav-list-link {{ item.current ? 'selected' : '' }} {% if is_emprende %}nav-link-emprende{% endif %}" href="{% if item.url %}{{ item.url | setting_url }}{% else %}#{% endif %}">{{ item.name }}</a>
```

**Clases CSS asignadas:**
- `nav-item-emprende` → Se agrega al `<li>` (contenedor)
- `nav-link-emprende` → Se agrega al `<a>` (enlace)

---

### Paso 2: Carga de Google Fonts (Patrick Hand)

**Archivo:** `layouts/layout.tpl`

Se agregaron los enlaces de Google Fonts en la sección `<head>` para cargar la fuente "Patrick Hand".

#### Código Implementado:

```15:18:layouts/layout.tpl
{# Google Fonts - Patrick Hand para EMPRENDE #}
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Patrick+Hand&display=swap" rel="stylesheet">
```

**Explicación:**
- `preconnect` → Establece conexión temprana con Google Fonts para mejorar rendimiento
- `display=swap` → Permite mostrar texto con fuente del sistema mientras carga Patrick Hand

---

### Paso 3: Estilos CSS Inline en Layout

**Archivo:** `layouts/layout.tpl`

Se agregaron estilos CSS inline después de la carga del archivo `custom.css` para asegurar que los estilos se apliquen correctamente.

#### Código Implementado:

```76:125:layouts/layout.tpl
{# Estilo específico para EMPRENDE en el menú - Inline para asegurar carga #}
        <style>
            /* Estilo para el enlace EMPRENDE en el menú de navegación - Alta especificidad */
            .head-main .nav-desktop-list .nav-item-emprende .nav-link-emprende,
            .head-main .nav-desktop-list .nav-link-emprende,
            .nav-desktop-list .nav-item-emprende .nav-link-emprende,
            .nav-desktop-list .nav-link-emprende {
                color: #ff6b9d !important;
                font-weight: 700 !important;
                font-size: 1.65em !important;
                font-family: 'Patrick Hand', cursive !important;
                font-style: normal !important;
                text-decoration: none !important;
            }

            /* Hover state para EMPRENDE - Alta especificidad */
            .head-main .nav-desktop-list .nav-item-emprende .nav-link-emprende:hover,
            .head-main .nav-desktop-list .nav-link-emprende:hover,
            .nav-desktop-list .nav-item-emprende .nav-link-emprende:hover,
            .nav-desktop-list .nav-link-emprende:hover {
                color: #ff4d8a !important;
                text-decoration: none !important;
            }

            /* Estilo para el enlace EMPRENDE en el menú móvil (Hamburger) - Alta especificidad */
            .modal-nav-hamburger .nav-item-emprende .nav-link-emprende,
            .modal-nav-hamburger .nav-link-emprende,
            .nav-list-panel .nav-item-emprende .nav-link-emprende,
            .nav-list-panel .nav-link-emprende,
            .nav-body .nav-item-emprende .nav-link-emprende,
            .nav-body .nav-link-emprende {
                color: #ff6b9d !important;
                font-weight: 700 !important;
                font-size: 1.65em !important;
                font-family: 'Patrick Hand', cursive !important;
                font-style: normal !important;
                text-decoration: none !important;
            }

            /* Hover state para EMPRENDE en móvil - Alta especificidad */
            .modal-nav-hamburger .nav-item-emprende .nav-link-emprende:hover,
            .modal-nav-hamburger .nav-link-emprende:hover,
            .nav-list-panel .nav-item-emprende .nav-link-emprende:hover,
            .nav-list-panel .nav-link-emprende:hover,
            .nav-body .nav-item-emprende .nav-link-emprende:hover,
            .nav-body .nav-link-emprende:hover {
                color: #ff4d8a !important;
                text-decoration: none !important;
            }
        </style>
```

**Características de los estilos:**

1. **Alta especificidad**: Múltiples selectores anidados para asegurar que los estilos se apliquen sobre los estilos del tema base
2. **Desktop y móvil**: Estilos separados para ambos contextos
3. **Estados hover**: Color más oscuro al pasar el mouse (#ff4d8a)
4. **!important**: Necesario para sobrescribir estilos del tema con alta especificidad

---

### Paso 4: Estilos CSS en Archivo Personalizado

**Archivo:** `static/css/custom.css`

Se agregaron los mismos estilos en el archivo CSS personalizado como respaldo y para mantener consistencia.

#### Código Implementado:

```278:332:static/css/custom.css
/*============================================================================
  Estilo específico para EMPRENDE en el menú principal
==============================================================================*/

/* Estilo para el enlace EMPRENDE en el menú de navegación - Alta especificidad */
.head-main .nav-desktop-list .nav-item-emprende .nav-link-emprende,
.head-main .nav-desktop-list .nav-link-emprende,
.nav-desktop-list .nav-item-emprende .nav-link-emprende,
.nav-desktop-list .nav-link-emprende {
  color: #ff6b9d !important;
  font-weight: 700 !important;
  font-size: 1.65em !important;
  font-family: 'Patrick Hand', cursive !important;
  font-style: normal !important;
  text-decoration: none !important;
}

/* Hover state para EMPRENDE - Alta especificidad */
.head-main .nav-desktop-list .nav-item-emprende .nav-link-emprende:hover,
.head-main .nav-desktop-list .nav-link-emprende:hover,
.nav-desktop-list .nav-item-emprende .nav-link-emprende:hover,
.nav-desktop-list .nav-link-emprende:hover {
  color: #ff4d8a !important;
  text-decoration: none !important;
}

/*============================================================================
  Estilo específico para EMPRENDE en el menú móvil (Hamburger)
==============================================================================*/

/* Estilo para el enlace EMPRENDE en el menú móvil - Alta especificidad */
.modal-nav-hamburger .nav-item-emprende .nav-link-emprende,
.modal-nav-hamburger .nav-link-emprende,
.nav-list-panel .nav-item-emprende .nav-link-emprende,
.nav-list-panel .nav-link-emprende,
.nav-body .nav-item-emprende .nav-link-emprende,
.nav-body .nav-link-emprende {
  color: #ff6b9d !important;
  font-weight: 700 !important;
  font-size: 1.65em !important;
  font-family: 'Patrick Hand', cursive !important;
  font-style: normal !important;
  text-decoration: none !important;
}

/* Hover state para EMPRENDE en móvil - Alta especificidad */
.modal-nav-hamburger .nav-item-emprende .nav-link-emprende:hover,
.modal-nav-hamburger .nav-link-emprende:hover,
.nav-list-panel .nav-item-emprende .nav-link-emprende:hover,
.nav-list-panel .nav-link-emprende:hover,
.nav-body .nav-item-emprende .nav-link-emprende:hover,
.nav-body .nav-link-emprende:hover {
  color: #ff4d8a !important;
  text-decoration: none !important;
}

/* Asegurar que el estilo se aplique solo a EMPRENDE y no afecte otros elementos */
```

**Carga del archivo CSS:**

El archivo `custom.css` se carga en `layouts/layout.tpl`:

```73:74:layouts/layout.tpl
{# Custom CSS file #}
        {{ 'css/custom.css' | static_url | static_inline }}
```

---

## 🎨 Propiedades CSS Aplicadas

### Color
- **Normal**: `#ff6b9d` (rosa vibrante)
- **Hover**: `#ff4d8a` (rosa más oscuro)

### Fuente
- **Familia**: `'Patrick Hand', cursive`
- **Peso**: `700` (negrita)
- **Tamaño**: `1.65em` (65% más grande que el tamaño base)
- **Estilo**: `normal` (no cursiva, aunque la fuente es handwritten)

### Otros Estilos
- **Decoración de texto**: `none` (sin subrayado)
- **Especificidad**: Alta (múltiples clases anidadas)
- **Importancia**: `!important` (para sobrescribir estilos del tema)

---

## 🔍 Selectores CSS Utilizados

### Desktop
- `.head-main .nav-desktop-list .nav-item-emprende .nav-link-emprende`
- `.head-main .nav-desktop-list .nav-link-emprende`
- `.nav-desktop-list .nav-item-emprende .nav-link-emprende`
- `.nav-desktop-list .nav-link-emprende`

### Móvil (Hamburger Menu)
- `.modal-nav-hamburger .nav-item-emprende .nav-link-emprende`
- `.modal-nav-hamburger .nav-link-emprende`
- `.nav-list-panel .nav-item-emprende .nav-link-emprende`
- `.nav-list-panel .nav-link-emprende`
- `.nav-body .nav-item-emprende .nav-link-emprende`
- `.nav-body .nav-link-emprende`

**Razón de múltiples selectores:**
- Asegurar que los estilos se apliquen en diferentes contextos del DOM
- Sobrescribir estilos del tema con mayor especificidad
- Cubrir diferentes estructuras HTML según el estado del menú

---

## ⚙️ Consideraciones Técnicas

### 1. Especificidad CSS
Los selectores con mayor especificidad tienen prioridad. Por eso se usan múltiples clases anidadas en lugar de un selector simple como `.nav-link-emprende`.

### 2. Uso de !important
Se utiliza `!important` porque los estilos del tema base de Tiendanube tienen alta especificidad y necesitan ser sobrescritos.

### 3. Estilos Duplicados
Los estilos están tanto en `layout.tpl` (inline) como en `custom.css` para:
- **Inline**: Asegurar carga inmediata y evitar problemas de caché
- **CSS externo**: Mantener código organizado y reutilizable

### 4. Compatibilidad Desktop y Móvil
Se implementaron estilos separados para desktop y móvil porque:
- Estructura HTML diferente
- Clases CSS diferentes según el contexto
- Menú hamburguesa tiene su propio sistema de clases

### 5. Detección Flexible
La lógica de detección en el template es flexible para capturar:
- Variaciones de mayúsculas/minúsculas
- Variantes en diferentes idiomas (EMPRENDE/EMPRENDA)
- Texto que contenga "EMPRENDE"

---

## ✅ Verificación

Para verificar que los estilos se aplicaron correctamente:

1. **Inspeccionar Elemento**: Abrir herramientas de desarrollador (F12) y buscar el elemento "EMPRENDE" en el HTML
2. **Verificar Clases**: Confirmar que las clases `nav-item-emprende` y `nav-link-emprende` están presentes
3. **Verificar Estilos**: En la pestaña "Computed" o "Estilos", verificar que los estilos CSS se están aplicando:
   - Color: `#ff6b9d`
   - Font-family: `'Patrick Hand', cursive`
   - Font-size: `1.65em`
   - Font-weight: `700`
4. **Probar Desktop y Móvil**: Verificar que los estilos funcionan en ambos contextos
5. **Probar Hover**: Verificar que el color cambia a `#ff4d8a` al pasar el mouse

---

## 📊 Resumen de Cambios

| Archivo | Líneas Modificadas | Tipo de Cambio |
|---------|-------------------|----------------|
| `snipplets/navigation/navigation-nav-list.tpl` | 6, 8, 12, 72, 74 | Lógica de detección y clases CSS |
| `layouts/layout.tpl` | 15-18, 76-125 | Google Fonts y estilos inline |
| `static/css/custom.css` | 278-332 | Estilos CSS externos |

---

## 🔄 Flujo de Implementación

```
1. Usuario carga la página
   ↓
2. layout.tpl carga Google Fonts (Patrick Hand)
   ↓
3. navigation-nav-list.tpl detecta elemento "EMPRENDE"
   ↓
4. Se asignan clases: nav-item-emprende y nav-link-emprende
   ↓
5. custom.css aplica estilos (o estilos inline en layout.tpl)
   ↓
6. Elemento "EMPRENDE" se muestra con color rosa y fuente Patrick Hand
```

---

## 📚 Referencias

- **Google Fonts - Patrick Hand**: https://fonts.google.com/specimen/Patrick+Hand
- **Especificidad CSS**: https://developer.mozilla.org/es/docs/Web/CSS/Specificity
- **Guía de Personalización**: Ver `GUIA_PERSONALIZAR_ELEMENTO_MENU.md`

---

## 🎯 Resultado Final

El elemento "EMPRENDE" en el menú principal ahora se muestra con:
- ✅ Color rosa personalizado (#ff6b9d)
- ✅ Fuente handwritten (Patrick Hand)
- ✅ Tamaño 65% más grande (1.65em)
- ✅ Negrita (font-weight: 700)
- ✅ Efecto hover con color más oscuro (#ff4d8a)
- ✅ Funciona en desktop y móvil

---

**Última actualización:** 2024  
**Versión:** 1.0  
**Autor:** Documentación técnica del proyecto

