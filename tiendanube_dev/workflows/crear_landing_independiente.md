---
description: Creación de landing page independiente con su propio template en Tiendanube
---

## 🚀 Landing Page Independiente

Instrucciones para crear una página con diseño único y URL propia:

1. **Definir URL en `config/settings.txt`**

   ```txt
   subtitle = Landing {Nombre}
       attribute = {nombre}_landing_url
       type = text
       description = URL de la página (ej: corporativo)
   ```

2. **Detección de Página (`templates/page.tpl`)**
   Configurar el switch para cargar el componente nuevo:

   ```twig
   {% set es_landing_{nombre} = page.handle == settings.{nombre}_landing_url %}

   {% if es_landing_{nombre} %}
       {% include "snipplets/page-{nombre}.tpl" %}
   {% else %}
       {# Contenido normal #}
       {{ page.content }}
   {% endif %}
   ```

3. **Componente de Página (`snipplets/page-{nombre}.tpl`)**
   Crear el archivo con el diseño específico.
   **IMPORTANTE:** Si usas carruseles Swiper, activa la inicialización forzada al final del archivo:

   ```twig
   <script>
   document.addEventListener('DOMContentLoaded', function() {
       if (typeof createSwiper !== 'undefined') {
           createSwiper('.js-swiper-{nombre}', { slidesPerView: 1 });
       }
   });
   </script>
   ```

4. **Vincular en `config/defaults.txt`**
   Asignar el valor por defecto: `{nombre}_landing_url = {handle}`.
