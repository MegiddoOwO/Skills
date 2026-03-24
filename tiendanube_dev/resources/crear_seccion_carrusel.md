---
description: Creación de carrusel dinámico (Swiper) en Tiendanube
---

## 🎡 Carrusel Dinámico (Sistema Swiper)

### 🚨 PASO 0: Protocolo de Diagnóstico (OBLIGATORIO)

Antes de proceder, el agente debe aplicar la **Biblia de Scatola** (`.agent/skills/tiendanube_master/SKILL.md`) y realizar las 5 preguntas del Protocolo de Diagnóstico al usuario. **No se debe generar código hasta que los 5 puntos estén validados.**

1. **Configurar Administrador (`config/settings.txt`)**

   ```txt
   collapse
       name = {nombre}_config
       description = Carrusel {Nombre}

       gallery
           name = {nombre}_galeria
           description = Imágenes del carrusel
           gallery_link = true
           gallery_more_info = true
   ```

2. **Crear Estructura (`snipplets/home/home-{nombre}.tpl`)**

   ```twig
   <section class="section-{nombre} mb-4" data-store="home-{nombre}">
       <div class="js-swiper-{nombre} swiper-container">
           <div class="swiper-wrapper">
               {% for item in settings.{nombre}_galeria %}
                   <div class="swiper-slide">
                       <img src="{{ item.image | static_url | settings_image_url('large') }}" class="lazyload w-100">
                       {% if item.title %}<h3 class="h4 text-center mt-2">{{ item.title | translate }}</h3>{% endif %}
                   </div>
               {% endfor %}
           </div>
           <div class="js-swiper-next-{nombre} swiper-button-next"></div>
           <div class="js-swiper-prev-{nombre} swiper-button-prev"></div>
       </div>
   </section>
   ```

3. **Inyectar JavaScript**
   Añadir al final del archivo si es una página interna o en el archivo de scripts globales para el home:
   ```javascript
   createSwiper(".js-swiper-{nombre}", {
     slidesPerView: 1,
     navigation: {
       nextEl: ".js-swiper-next-{nombre}",
       prevEl: ".js-swiper-prev-{nombre}",
     },
     breakpoints: {
       768: { slidesPerView: 4 },
     },
   });
   ```
