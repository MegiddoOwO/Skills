

---

# 🏗️ Guía Técnica: Carrusel de Productos Multi-Origen Filtrado por Tag

Esta guía detalla el proceso técnico, paso a paso, para implementar un **Carrusel de Productos** que consolida (fusiona) múltiples bandejas de productos nativas de Tiendanube y las filtra dinámicamente mediante una etiqueta (Tag) ingresada directamente desde el administrador, sin necesidad de recurrir a complejas re-inicializaciones mediante JavaScript.

La ventaja principal de este enfoque es la optimización del rendimiento, ya que el filtrado ocurre **del lado del servidor (Twig)** y no del lado del cliente.

---

## 🏛 Arquitectura y Reglas del Sistema

### Limitación del Motor de Tiendanube

A nivel global (fuera de las páginas de categoría), Tiendanube **no permite** llamar a la totalidad del catálogo por temas de rendimiento. Solo expone tres bandejas globales ("colecciones maestras") que el administrador alimenta manualmente:

1. `sections.primary.products` (Productos Destacados)
2. `sections.new.products` (Nuevos Productos / Novedades)
3. `sections.sale.products` (Productos en Oferta)

**Regla de Oro:** Para que un producto pueda ser capturado por este carrusel, debe cumplir dos condiciones obligatorias:

1. Tener la etiqueta (Tag) exacta configurada en el personalizador.
2. Pertenecer a al menos UNA de las tres bandejas mencionadas anteriormente.

---

## 🛠 Proceso de Implementación (Paso a Paso)

### PASO 1: Campos de Base de Datos (`config/settings.txt`)

Debemos habilitar el punto de entrada para que el administrador decida qué etiqueta filtrará.

**Acción:** En tu archivo `settings.txt`, dar de alta en una sección modular el bloque del Carrusel, obligando el uso de un campo `text` (nunca `input`).

```txt
	collapse
		name = mi_namespace_carrusel_collapse
		title = Carrusel Filtrado
		backto = mi_namespace_order_position
	checkbox
		name = mi_namespace_carrusel_show
		description = Mostrar carrusel
	i18n_input
		name = mi_namespace_carrusel_title
		description = Título de la sección
	text
		name = mi_namespace_carrusel_tag
		description = Tag de los productos a mostrar (ej: quince_anos)
```

No olvides inicializar los defaults en `config/defaults.txt`.

---

### PASO 2: La Lógica de Fusión y Filtrado (El Componente HTML/Twig)

El "corazón" de este componente requiere crear un arreglo vacío y utilizar el filtro `merge` nativo de Twig. Luego, se itera y se detectan coincidencias en la matriz `product.tags`.

**Acción:** Crear tu archivo `.tpl` en la carpeta `snipplets/` que corresponda e inyectar esta lógica:

```twig
{% if settings.mi_namespace_carrusel_show %}

    {# 1. Fusión de las bandejas maestras #}
    {% set all_products = [] %}

    {% if sections.primary.products %}
        {% set all_products = all_products | merge(sections.primary.products) %}
    {% endif %}
    {% if sections.new.products %}
        {% set all_products = all_products | merge(sections.new.products) %}
    {% endif %}
    {% if sections.sale.products %}
        {% set all_products = all_products | merge(sections.sale.products) %}
    {% endif %}

    {# 2. Obtención de la etiqueta y limpieza de espacios vacíos #}
    {% set filter_tag = settings.mi_namespace_carrusel_tag | default('') | trim %}
    {% set products_found = 0 %}

    <section class="section-my-carousel py-5 position-relative" data-store="my-custom-carousel">
        <div class="container position-relative">

            {% if settings.mi_namespace_carrusel_title %}
                <h2 class="h3 mt-3 mb-4 text-center">{{ settings.mi_namespace_carrusel_title | translate }}</h2>
            {% endif %}

            <div class="js-swiper-my-namespace-carousel swiper-container">
                <div class="swiper-wrapper">

                    {# 3. Intersección: Revisar cada producto. #}
                    {% for product in all_products %}
                        {# Si el campo está vacío, o el tag coincide, lo inyectamos #}
                        {% if not filter_tag or filter_tag in product.tags %}
                            {% set products_found = products_found + 1 %}
                            {# Inyectar la tarjeta normal o el item en formato slide #}
                            {% include 'snipplets/grid/item.tpl' with {'slide_item': true} %}
                        {% endif %}
                    {% endfor %}

                </div>
            </div>

            {# 4. Manejo de Errores (Empty State) #}
            {% if products_found == 0 %}
                <div class="text-center w-100 mt-4 mb-4" style="background: #f8f9fa; padding: 30px;">
                    <p class="mb-0">No encontramos productos con el Tag: <strong>{{ filter_tag | default('Vacío') }}</strong></p>
                    <small>Asegúrate de que haya productos en Destacados, Ofertas o Novedades con esa etiqueta.</small>
                </div>
            {% endif %}

            {# Flechas de Navegación (Opcionales) #}
            {% if products_found > 0 %}
                <div class="js-swiper-my-namespace-carousel-prev swiper-button-prev d-none d-md-flex"></div>
                <div class="js-swiper-my-namespace-carousel-next swiper-button-next d-none d-md-flex"></div>
            {% endif %}

        </div>
    </section>

    {# 5. Inicialización Responsiva (Swiper) #}
    {% if products_found > 0 %}
        <style>
            /* CSS Para mantener las flechas en medio y ocultas en móvil por Usabilidad Táctil */
            .section-my-carousel .swiper-button-prev,
            .section-my-carousel .swiper-button-next {
                position: absolute; top: 50%; transform: translateY(-50%); z-index: 10;
            }
        </style>
        <script>
            document.addEventListener('DOMContentLoaded', function() {
                var initCarousel = setInterval(function() {
                    if (typeof window.Swiper !== 'undefined') {
                        clearInterval(initCarousel);
                        new window.Swiper('.js-swiper-my-namespace-carousel', {
                            /* Configuraciones fraccionadas para inducir el scroll ("Affordance") */
                            slidesPerView: 1.2,
                            spaceBetween: 15,
                            navigation: {
                                nextEl: '.js-swiper-my-namespace-carousel-next',
                                prevEl: '.js-swiper-my-namespace-carousel-prev',
                            },
                            breakpoints: {
                                768: {
                                    slidesPerView: 3.5,
                                    spaceBetween: 20,
                                }
                            }
                        });
                    }
                }, 500);
            });
        </script>
    {% endif %}

{% endif %}
```

---

## 🎯 Resumen Teórico

Esta arquitectura resuelve 3 grandes retos:

1. **Evita la lentitud:** Transforma las limitaciones de Tiendanube en ventajas, uniendo inteligentemente (`| merge`) sólo las bandejas optimizadas, en lugar de intentar llamar a todo el catálogo mediante peticiones externas o APIs.
2. **Autenticidad Visual:** Permite inyectar fraccionamiento en Swiper.js (`1.2` en celulares) para indicar psicológicamente al comprador que existe más contenido lateral.
3. **Control Absoluto:** Le cede el control al administrador para reutilizar el mismo componente con múltiples tags distintos (`jeans`, `verano`, `liquidación`, etc.) a lo largo y ancho de las Landings del proyecto.


---

# 📦 Guía de Migración: Carrusel de Secciones Personalizado

## 🎯 Descripción General

Esta sección permite crear un carrusel completamente personalizable usando Embla Carousel, con imágenes, títulos, enlaces y múltiples opciones de configuración responsivas.

---

## 📋 Checklist de Archivos a Modificar/Crear

### ✅ Archivos que debes modificar:
- [ ] `config/settings.txt`
- [ ] `config/defaults.txt`
- [ ] `layouts/layout.tpl`
- [ ] `snipplets/home/home-section-switch.tpl`

### ✅ Archivos que debes crear:
- [ ] `snipplets/home/home-carrusel-secciones.tpl`
- [ ] `snipplets/defaults/home/carrusel_secciones_help.tpl` (opcional)

---

## 🔧 PASO 1: Configuración en `config/settings.txt`

### Ubicación:
Agrega esta configuración dentro de la sección de **Home** (busca donde están otras secciones como `slider`, `featured_products`, etc.)

### Código a agregar:

```txt
collapse
	name = carrusel_secciones_cfg
	description = Carrusel de secciones personalizado
	backto = home_order_position
	
	checkbox
		name = carrusel_secciones_show
		description = Mostrar carrusel de secciones
	
	i18n_input
		name = carrusel_secciones_title
		description = Título de la sección
	
	dropdown
		name = carrusel_secciones_title_size_mobile
		description = Tamaño del título en móvil
		values
			small = Pequeño
			medium = Mediano
			large = Grande
	
	dropdown
		name = carrusel_secciones_title_size_desktop
		description = Tamaño del título en desktop
		values
			small = Pequeño
			medium = Mediano
			large = Grande
			xlarge = Extra grande
	
	dropdown
		name = carrusel_secciones_image_title_size_mobile
		description = Tamaño del título de las imágenes en móvil
		values
			small = Pequeño
			medium = Mediano
			large = Grande
	
	dropdown
		name = carrusel_secciones_image_title_size_desktop
		description = Tamaño del título de las imágenes en desktop
		values
			small = Pequeño
			medium = Mediano
			large = Grande
			xlarge = Extra grande
	
	dropdown
		name = carrusel_secciones_autoplay
		description = Reproducción automática
		values
			none = Sin reproducción automática
			3000 = 3 segundos
			4000 = 4 segundos
			5000 = 5 segundos
	
	checkbox
		name = carrusel_secciones_loop
		description = Carrusel infinito
	
	checkbox
		name = carrusel_secciones_dots
		description = Mostrar indicadores (dots)
	
	checkbox
		name = carrusel_secciones_arrows
		description = Mostrar flechas de navegación
	
	dropdown
		name = carrusel_secciones_aspect_ratio
		description = Relación de aspecto de las imágenes
		values
			auto = Automático
			square = Cuadrado (1:1)
			portrait = Vertical (3:4)
			landscape = Horizontal (4:3)
			wide = Panorámico (16:9)
	
	dropdown
		name = carrusel_secciones_object_fit
		description = Ajuste de imagen
		values
			contain = Contener (sin recortar)
			cover = Cubrir (con recorte)
			fill = Rellenar (puede distorsionar)
	
	range_number
		name = carrusel_secciones_border_radius
		description = Radio de borde (px)
		min = 0
		max = 20
	
	dropdown
		name = carrusel_secciones_align
		description = Alineación del carrusel
		values
			start = Inicio
			center = Centro
	
	dropdown
		name = carrusel_secciones_mobile_items
		description = Elementos visibles en móvil
		values
			1 = 1
			1.5 = 1.5
			2 = 2
			2.5 = 2.5
			3 = 3
			3.5 = 3.5
	
	dropdown
		name = carrusel_secciones_desktop_items
		description = Elementos visibles en desktop
		values
			2 = 2
			2.5 = 2.5
			3 = 3
			3.5 = 3.5
			4 = 4
			4.5 = 4.5
			5 = 5
			5.5 = 5.5
			6 = 6
	
	dropdown
		name = carrusel_secciones_mobile_container
		description = Ancho del carrusel en móvil
		values
			full = Sin márgenes (hasta el borde)
			full_left = Margen izquierdo, sin margen derecho
			minimal = Márgenes mínimos
			normal = Container normal
			wide = Container amplio
	
	dropdown
		name = carrusel_secciones_desktop_container
		description = Ancho del carrusel en desktop
		values
			full = Sin márgenes (ancho completo)
			full_left = Margen izquierdo, sin margen derecho
			normal = Container normal
			wide = Container amplio
	
	dropdown
		name = carrusel_secciones_mobile_spacing
		description = Espaciado entre elementos en móvil (px)
		values
			0 = Sin espacio
			5 = 5px
			10 = 10px
			15 = 15px
			20 = 20px
	
	dropdown
		name = carrusel_secciones_desktop_spacing
		description = Espaciado entre elementos en desktop (px)
		values
			0 = Sin espacio
			5 = 5px
			10 = 10px
			15 = 15px
			20 = 20px
	
	color
		name = carrusel_secciones_background
		description = Color de fondo de la sección
	
	gallery
		name = carrusel_secciones_items
		description = Imágenes del carrusel
		gallery_link = true
		gallery_width = 800
		gallery_height = 800
		gallery_more_info = true
```

### Agregar la sección al selector de orden:

Busca el dropdown `home_order_position` y agrega esta línea dentro de `values`:

```txt
carrusel_secciones = Carrusel de secciones personalizado
```

---

## 🎨 PASO 2: Valores por defecto en `config/defaults.txt`

### Código a agregar:

```txt
carrusel_secciones_show = 1
carrusel_secciones_title_es = Regalos Para Todas Las Ocasiones
carrusel_secciones_title_en = Gifts For All Occasions
carrusel_secciones_title_pt = Presentes Para Todas As Ocasiões
carrusel_secciones_title_size_desktop = large
carrusel_secciones_title_size_mobile = medium
carrusel_secciones_image_title_size_desktop = medium
carrusel_secciones_image_title_size_mobile = small
carrusel_secciones_autoplay = 4000
carrusel_secciones_loop = 1
carrusel_secciones_dots = 1
carrusel_secciones_arrows = 1
carrusel_secciones_aspect_ratio = square
carrusel_secciones_object_fit = cover
carrusel_secciones_border_radius = 8
carrusel_secciones_align = start
carrusel_secciones_mobile_items = 2.5
carrusel_secciones_desktop_items = 4.5
carrusel_secciones_mobile_container = full
carrusel_secciones_desktop_container = normal
carrusel_secciones_mobile_spacing = 5
carrusel_secciones_desktop_spacing = 10
carrusel_secciones_background = rgba(0, 0, 0, 0)
```

**Nota:** Ajusta los títulos (`_es`, `_en`, `_pt`) según los idiomas que maneje tu tienda.

---

## 📚 PASO 3: Cargar librería en `layouts/layout.tpl`

### Ubicación:
Dentro del `<head>`, preferiblemente cerca de donde se cargan otros scripts.

### Código a agregar:

```twig
{# Embla Carousel para home #}
{% if template == 'home' %}
    {{ 'https://unpkg.com/embla-carousel/embla-carousel.umd.js' | script_tag(true) }}
    {{ 'https://unpkg.com/embla-carousel-autoplay/embla-carousel-autoplay.umd.js' | script_tag(true) }}
{% endif %}
```

**⚠️ Importante:** La condición `{% if template == 'home' %}` asegura que solo se cargue en la página de inicio, optimizando el rendimiento.

---

## 🔀 PASO 4: Integrar en `snipplets/home/home-section-switch.tpl`

### Ubicación:
Dentro del switch/case donde se manejan las secciones del home.

### Código a agregar:

```twig
{% elseif section_select == 'carrusel_secciones' %}
    {#  **** Carrusel de secciones personalizado ****  #}
    {% set has_carrusel_secciones_items = settings.carrusel_secciones_items and settings.carrusel_secciones_items is not empty %}
    {% if show_help or (show_component_help and not has_carrusel_secciones_items) %}
        {% snipplet 'defaults/home/carrusel_secciones_help.tpl' %}
    {% else %}
        {% include 'snipplets/home/home-carrusel-secciones.tpl' %}
    {% endif %}
```

**Nota:** El `carrusel_secciones_help.tpl` es opcional. Si no lo creas, elimina esa parte del código.

---

## 🎨 PASO 5: Crear el snippet principal

### Archivo: `snipplets/home/home-carrusel-secciones.tpl`

**Ver el archivo completo en el repositorio.** Aquí te dejo la estructura principal:

```twig
{#/*============================================================================
  #Carrusel de secciones personalizado
==============================================================================*/#}

{% set has_carrusel_items = settings.carrusel_secciones_items and settings.carrusel_secciones_items is not empty %}
{% set carrusel_title = settings.carrusel_secciones_title %}
{# ... más variables ... #}

{% if has_carrusel_items %}
<section class="section-carrusel-secciones position-relative mb-5" data-store="home-carrusel-secciones">
    <div class="carrusel-container-wrapper">
        {% if carrusel_title %}
            <h2 class="h3 mt-3 mb-4 text-center carrusel-title-spacing">{{ carrusel_title | translate }}</h2>
        {% endif %}
        
        <div class="embla-carrusel-secciones-wrapper-outer">
            <div class="embla-carrusel-secciones-wrapper">
                <div class="embla-carrusel-secciones" id="embla-carrusel-secciones">
                    <div class="embla-carrusel-secciones__container">
                        {% for slide in settings.carrusel_secciones_items %}
                            {# ... slides ... #}
                        {% endfor %}
                    </div>
                </div>
                
                {# Flechas de navegación #}
                {% if show_arrows %}
                    {# ... arrows ... #}
                {% endif %}
            </div>
            
            {# Dots #}
            {% if show_dots %}
                {# ... dots ... #}
            {% endif %}
        </div>
    </div>
</section>

{# CSS #}
<style>
    {# ... estilos ... #}
</style>

{# JavaScript #}
<script>
    {# ... inicialización ... #}
</script>
{% endif %}
```

**📄 Copia el archivo completo desde:** `snipplets/home/home-carrusel-secciones.tpl`

---

## ✅ PASO 6: Verificación

### 1. Sube los archivos a tu tema:
```bash
# Si usas SFTP, sube:
- config/settings.txt
- config/defaults.txt
- layouts/layout.tpl
- snipplets/home/home-section-switch.tpl
- snipplets/home/home-carrusel-secciones.tpl
```

### 2. En el panel de Tiendanube:
1. Ve a **Diseño > Personalizar diseño**
2. Busca la sección **"Página de inicio"**
3. En **"Orden de las secciones"** deberías ver: **"Carrusel de secciones personalizado"**
4. Haz clic en la sección para configurarla
5. Agrega imágenes desde el **campo "Imágenes del carrusel"**

### 3. Configuración recomendada inicial:
- **Elementos visibles móvil:** 2.5 o 3
- **Elementos visibles desktop:** 4.5
- **Aspecto de imagen:** Square (1:1)
- **Ajuste de imagen:** Cover
- **Autoplay:** 4 segundos
- **Loop infinito:** Activado
- **Dots:** Activado
- **Flechas:** Activado

---

## 🐛 Problemas Comunes y Soluciones

### ❌ Problema 1: Las imágenes no se muestran
**Causa:** Sintaxis incorrecta en Twig para acceder a las imágenes del gallery.

**Solución:** Asegúrate de usar:
```twig
data-src="{{ slide.image | static_url | settings_image_url('large') }}"
```

**NO uses:**
```twig
{{ item | static_url('large') }}  ❌
```

---

### ❌ Problema 2: El loop infinito no funciona correctamente
**Causa:** Conflictos con `align: 'start'` y `containScroll: 'trimSnaps'`.

**Solución:** En el JavaScript, usa esta configuración:
```javascript
const options = {
    loop: true,  // o false según configuración
    align: 'start',
    slidesToScroll: 1,
    skipSnaps: false,
    dragFree: false
};
```

Y en el CSS, elimina transiciones manuales:
```css
.embla-carrusel-secciones__container {
    display: flex;
    backface-visibility: hidden;
    touch-action: pan-y;
    /* NO agregues: transition: transform 0.3s ease; */
}
```

---

### ❌ Problema 3: Las flechas se cortan
**Causa:** Las flechas están dentro de un contenedor con `overflow: hidden`.

**Solución:** Estructura correcta de divs:
```html
<div class="embla-carrusel-secciones-wrapper">  <!-- overflow: visible -->
    <div class="embla-carrusel-secciones">  <!-- overflow: hidden -->
        <!-- slides -->
    </div>
    <!-- arrows FUERA del div con overflow hidden -->
    <button class="embla-carrusel-secciones__prev">...</button>
    <button class="embla-carrusel-secciones__next">...</button>
</div>
```

---

### ❌ Problema 4: Los títulos de las imágenes no aparecen
**Causa:** Usando `gallery_caption` en lugar del campo `title` por defecto.

**Solución:**
- En `settings.txt`, usa `gallery_more_info = true` (NO uses `gallery_caption`)
- En el template, accede con `{{ slide.title }}`

---

### ❌ Problema 5: Configuración móvil no se aplica
**Causa:** CSS no estructurado con "Mobile First".

**Solución:** Define estilos móviles primero, luego sobrescribe con media queries:
```css
/* Móvil (por defecto) */
.carrusel-container-wrapper {
    padding: 0 0.75rem;
}

/* Desktop (sobrescribe) */
@media (min-width: 768px) {
    .carrusel-container-wrapper {
        max-width: 1140px;
        margin: 0 auto;
    }
}
```

---

### ❌ Problema 6: El autoplay no funciona
**Causa:** Plugin no cargado o configuración incorrecta.

**Solución:**
1. Verifica que ambas librerías se carguen en `layout.tpl`
2. Inicializa el plugin correctamente:

```javascript
const plugins = [];

if (autoplayDelay) {
    plugins.push(
        EmblaCarouselAutoplay({ 
            delay: autoplayDelay,
            stopOnInteraction: false,
            stopOnMouseEnter: true
        })
    );
}

const emblaApi = EmblaCarousel(emblaNode, options, plugins);
```

---

## 🎯 Consejos Pro

### 1. **Lazy Loading de Imágenes**
El carrusel usa `lazyload` de Tiendanube:
```html
<img 
    src="{{ 'images/empty-placeholder.png' | static_url }}" 
    data-src="{{ slide.image | static_url | settings_image_url('large') }}" 
    class="lazyload"
>
```

### 2. **Tamaños de Imagen Recomendados**
```txt
gallery_width = 800
gallery_height = 800
```
Esto optimiza la carga sin perder calidad.

### 3. **Variables CSS del Tema**
Usa las variables del tema para mantener consistencia:
- `var(--main-background)`
- `var(--main-foreground)`
- `var(--accent-color)`
- `var(--font-base)`, `var(--font-large)`, etc.

### 4. **Internacionalización**
Usa `| translate` para todos los textos:
```twig
{{ carrusel_title | translate }}
{{ slide.title | translate }}
```

### 5. **Responsive Breakpoint**
El breakpoint estándar en Tiendanube es `768px`:
```css
@media (min-width: 768px) { /* Desktop */ }
@media (max-width: 767px) { /* Mobile */ }
```

---

## 📊 Estructura de Datos del Gallery

Cuando usas `gallery` con `gallery_more_info = true`, cada item tiene:

```javascript
{
    image: "...",      // URL de la imagen
    title: "...",      // Título (campo por defecto)
    link: "...",       // URL del enlace
    description: "...", // Descripción (no usado en este carrusel)
    button: "...",     // Texto del botón (no usado)
    color: "..."       // Color (no usado)
}
```

**Acceso en Twig:**
```twig
{% for slide in settings.carrusel_secciones_items %}
    {{ slide.image }}
    {{ slide.title }}
    {{ slide.link }}
{% endfor %}
```

---

## 🔄 Personalización Adicional

### Cambiar el nombre de la sección:
Simplemente renombra todas las instancias de `carrusel_secciones` por tu nombre preferido (ej: `custom_carousel`).

### Agregar más opciones:
1. Define el nuevo setting en `settings.txt`
2. Agrega el valor por defecto en `defaults.txt`
3. Crea la variable en el template
4. Aplica en CSS/JavaScript

### Usar en otras páginas:
Cambia la condición en `layout.tpl`:
```twig
{% if template == 'home' or template == 'page' %}
```

---

## 📞 Soporte

Si encuentras problemas:
1. Verifica que todos los archivos estén subidos correctamente
2. Revisa la consola del navegador (F12) para errores de JavaScript
3. Comprueba que las librerías de Embla se carguen correctamente
4. Asegúrate de que las imágenes estén agregadas en el panel de administración

---

**🎉 ¡Listo! Tu carrusel personalizado debería estar funcionando perfectamente.**



---

# Guía Técnica: Creación de Carrusel de Productos con Filtros por Tags (Tiendanube / Codefy)

Este documento detalla exhaustivamente el funcionamiento y la implementación de la sección "Carrusel de Productos con Filtros". Su objetivo es servir como manual técnico para replicar este comportamiento interactivo (filtrado por tags en tiempo real mediante pestañas y deslizamiento táctil horizontal) en cualquier nueva sección o componente a futuro.

## Arquitectura y Archivos Involucrados

Para que la sección sea modular, editable desde el panel de administración y funcional en el frontend, intervienen los siguientes componentes:

1. **[snipplets/home/home-carrusel-productos-filtros.tpl](file:///Users/macpro/Documents/GitHub/scatola/snipplets/home/home-carrusel-productos-filtros.tpl) (o el nombre del nuevo componente)**: El núcleo HTML, Twig, CSS local y la lógica JavaScript de filtrado e integración con Embla.
2. **[snipplets/home/home-section-switch.tpl](file:///Users/macpro/Documents/GitHub/scatola/snipplets/home/home-section-switch.tpl)**: El enrutador que inyecta el componente en el Layout del Home.
3. **[config/settings.txt](file:///Users/macpro/Documents/GitHub/scatola/config/settings.txt) y [config/defaults.txt](file:///Users/macpro/Documents/GitHub/scatola/config/defaults.txt)**: Definen las variables editables por el comerciante (hasta 6 filtros, etiquetas, configuraciones de diseño, etc.).
4. **Librería de Terceros (Embla Carousel)**: Requerimiento obligatorio global que debe estar cargado en el `<head>` o al final del `<body>` del documento principal (`layout.tpl`) para manejar la función de deslizamiento físico (Swipe/Drag).

---

## 1. Lógica Backend (Twig) y Renderizado DOM

El proceso de recolección y filtrado inicial se maneja del lado del servidor usando el motor de plantillas Twig.

### A. Definición de Filtros en Base a Configuraciones
El administrador puede dar de alta hasta 6 pestañas. En el componente [.tpl](file:///Users/macpro/Documents/GitHub/scatola/snipplets/home/home-popup.tpl) se debe inicializar un arreglo `filters`. 
Por cada filtro configurado en [settings.txt](file:///Users/macpro/Documents/GitHub/scatola/config/settings.txt) (Nombre y Tag), se inyecta un objeto que servirá para construir el menú de pestañas.

```twig
{# Ejemplo del push al arreglo de filtros si el Tag está configurado #}
{% set filters = [] %}
{% if settings.mi_carrusel_filter_1_name and settings.mi_carrusel_filter_1_tag %}
    {% set filters = filters|merge([{
        'name': settings.mi_carrusel_filter_1_name,
        'tag': settings.mi_carrusel_filter_1_tag,
        'badge': settings.mi_carrusel_filter_1_badge | default(''),
        'id': 'filter-1'
    }]) %}
{% endif %}
```

### B. Consolidación del Listado Global de Productos
Dado que se busca mostrar productos de diferentes colecciones (Destacados, Nuevos, Ofertas), se debe generar un "Master Array" de productos usando la función `merge`.

```twig
{% set all_products = [] %}
{% if sections.primary.products %} {% set all_products = all_products | merge(sections.primary.products) %} {% endif %}
{% if sections.new.products %} {% set all_products = all_products | merge(sections.new.products) %} {% endif %}
{% if sections.sale.products %} {% set all_products = all_products | merge(sections.sale.products) %} {% endif %}
```

### C. Pre-filtrado Servidor (Seguridad Funcional)
Para evitar enviar miles de nodos HTML innecesarios al navegador (ahorro de latencia), cruzamos `all_products` contra los `tags` definidos en el arreglo `filters`. Si un producto tiene coincidencia, entra en `all_tagged_products`. 

### D. Renderizado HTML Crítico (`data-tags`)
Cada producto (`slide` dentro de la grilla de `Embla`) **DEBE** contener un atributo `data-tags` que imprima los tags en formato de texto separado por comas. El JavaScript utilizará esto como su "Base de Datos en Tiempo Real" en el navegador para saber qué tarjetas mostrar u ocultar.

```twig
<div class="embla-carrusel-productos__slide" data-tags="{{ product.tags | join(',') }}">
  {# Card de producto... #}
</div>
```

---

## 2. Construcción del Menú de Filtros (Tabs)

Se generan dinámicamente según el array bidimensional `filters` inicializado arriba. El primer elemento recibe la clase `--active`. 
Cada botón lleva como data-atributo el `tag` que le corresponde. 

```twig
<div class="filtros-container">
    {% for filter in filters %}
        <button class="filtro-btn {% if loop.first %}filtro-btn--active{% endif %}" data-tag="{{ filter.tag }}">
            {{ filter.name }}
        </button>
    {% endfor %}
</div>
```

---

## 3. Lógica Frontend (JavaScript y Embla Carousel)

Esta es la sección más delicada. El componente no realiza peticiones asíncronas (AJAX) al hacer click en las pestañas. Utiliza **Virtual DOM manual**.

Dado que `Embla Carousel` lee los elementos hijos de un contenedor (`.embla__container`) para calcular el ancho total de las pistas y los puntos de snap, si ocultamos elementos por CSS (`display: none`), Embla se "romperá" y dejará hoyos en blanco. La solución es **extraer y reinsertar nodos HTML puros**, y luego "destruir e inicializar" la librería Embla en milisegundos.

### A. Variables de Estado Global del Componente
```javascript
document.addEventListener('DOMContentLoaded', function() {
    const filterButtons = document.querySelectorAll('.filtro-btn');
    const slidesContainer = document.querySelector('.embla__container');
    
    // 1. Guardar todos los slides originales renderizados por Twig en memoria temporal
    let productSlides = Array.from(document.querySelectorAll('.embla__slide'));
    const originalSlidesData = productSlides.map(slide => ({
        tags: slide.getAttribute('data-tags') || '', // Para la validación del filtro
        html: slide.outerHTML                        // El "String" literal del nodo HTML
    }));

    let emblaApi = null;
    let currentFilter = '{{ filters[0].tag }}'; // Empezar con la primera tab de Twig
```

### B. Función de Filtrado Virtual
Cuando el usuario hace clic en una pestaña (`tag`):

1. Se vacía el contenedor del carrusel por completo.
2. Se itera el listado que guardamos en memoria `originalSlidesData`.
3. Si la propiedad `tags` del objeto cruza con el `tag` consultado, se vuelve a inyectar ese `html` crudo en el contenedor usando `insertAdjacentHTML`.

```javascript
    function filterProducts(tag) {
        if (!slidesContainer) return;

        slidesContainer.innerHTML = ''; // Vaciar el carrusel físico

        originalSlidesData.forEach(data => {
            // Verificar si el tag clickeado está dentro del listado de tags del HTML
            if (data.tags.includes(tag)) {
                slidesContainer.insertAdjacentHTML('beforeend', data.html);
                const newSlide = slidesContainer.lastElementChild;
                
                // Asegurar que sean visibles
                newSlide.classList.remove('hidden'); 
                newSlide.style.display = '';
            }
        });

        // NOTA: Agregar validación en caso de que un Tag no arroje resultados, 
        // puedes inyectar todo nuevamente (originalSlidesData) o mostrar un mensaje "Sin productos".

        // -------------------------
        // Manejo de Interfaz Activa
        // -------------------------
        document.querySelectorAll('.filtro-btn').forEach(btn => {
            btn.classList.toggle('filtro-btn--active', btn.getAttribute('data-tag') === tag);
        });

        // ---------------------------------
        // El Paso Crítico: Reborn de Embla
        // ---------------------------------
        if (emblaApi) {
            emblaApi.destroy(); // Matar los eventos táctiles viejos, dado que destruímos nodos hijos
            emblaApi = null;
        }

        // Deferir la reinicialización para asegurar que el navegador haya repintado el DOM
        setTimeout(() => initializeEmblaCarousel(0), 0); 
    }
```

### C. Función Inicializadora de Embla Carousel

Debemos verificar que la librería Embla exista (ya que a veces se carga diferida al final del body). Luego, configuramos el carrusel y lo almacenamos en `emblaApi`.

```javascript
    function initializeEmblaCarousel(startIndex = 0) {
        // Retry loop en caso de carga lenta del CDN de Embla
        if (typeof EmblaCarousel === 'undefined') {
            setTimeout(() => initializeEmblaCarousel(startIndex), 100);
            return;
        }

        const emblaNode = document.querySelector('.embla-carrusel-productos');
        if (!emblaNode) return;

        const options = { loop: false, align: 'start', startIndex };
        const plugins = [];
        // (Opcional) Autoplay Plugin de Embla si corresponde
        
        // Arrancar Motor
        emblaApi = EmblaCarousel(emblaNode, options, plugins);
        
        // Vincular flechas de navegación personalizadas a la API
        const prevBtn = document.querySelector('.embla__prev');
        if (prevBtn && !prevBtn.dataset.bound) {
            prevBtn.addEventListener('click', () => emblaApi && emblaApi.scrollPrev());
            prevBtn.dataset.bound = 'true';
        }
        // Repetir validación para botón 'next', etc.
    }
```

### D. Disparo Original y Event Listeners
Para finalizar y poner en marcha el componente cuando la página carga:

```javascript
    // Asignar los clics a las pestañas y derivarlas a filterProducts
    filterButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            filterProducts(this.getAttribute('data-tag'));
        });
    });

    // Iniciar con el filtro de la pestaña principal
    filterProducts(currentFilter);
});
```

---

## 4. Requisitos de Estilos (CSS)
Aunque el comportamiento recae en JS, `Embla` funciona mediante las mecánicas nativas de Flexbox en CSS.

Es de carácter **Obligatorio** que las siguientes reglas CSS se mantengan para que los cálculos matemáticos internos de la librería Embla Carousel no choquen al reinicializarse:

```css
.embla {
  overflow: hidden; /* Muy estricto, es el marco de la fotografía */
}
.embla__container {
  display: flex; /* Obligatorio */
  will-change: transform; /* Optimización del navegador */
}
.embla__slide {
  flex: 0 0 [porcentaje-de-ancho]; /* ej: calc(100% / 4) para desktop */
  min-width: 0; /* Evitar estiramiento de flexbox que corrompe el cálculo */
}
```

## Resumen del Flujo
1. **Twig/Servidor** junta todos los productos, revisa tags y ensambla un carrusel HTML gigante e invisible.
2. **Javascript** en su línea inicial *"Copia y Pega"* todo ese HTML gigante en una variable de memoria (`originalSlidesData`).
3. **Pestaña es presionada**, JS vacía la pantalla, filtra su memoria cruzando Tags contra el String del ID y clona solo lo que la pestaña requiere al DOM.
4. **Javascript** le avisa a `EmblaCarousel` que las tarjetas mutaron. Destruye la instancia actual y crea una nueva con las tarjetas exactas, lo que habilita que se pueda desplazar `swipe/tactil` correctamente las tarjetas con animaciones suaves.
