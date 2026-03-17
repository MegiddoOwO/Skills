---
description: Flujo para crear una nueva sección estática en el Home de Tiendanube
---

## 🛠️ Creación de Sección Estática (Patrón Scatola)

### 🚨 PASO 0: Protocolo de Diagnóstico (OBLIGATORIO)

Antes de proceder, el agente debe aplicar la **Biblia de Scatola** (`.agent/skills/tiendanube_master/SKILL.md`) y realizar las 5 preguntas del Protocolo de Diagnóstico al usuario. **No se debe generar código hasta que los 5 puntos estén validados.**

1. **Configurar `settings.txt`**

   ```txt
   subtitle = {Nombre}
       attribute = {nombre}_show
       type = checkbox
       default = true

       attribute = {nombre}_title
       type = i18n_input
       description = Título
   ```

2. **Añadir a `defaults.txt`** (Nombre y valores base).

3. **Inyectar en `snipplets/home/home-section-switch.tpl`**

   ```twig
   {% elseif section_select == '{nombre}' %}
       {% include 'snipplets/home/home-{nombre}.tpl' %}
   ```

4. **Crear `snipplets/home/home-{nombre}.tpl` con el siguiente código base:**
   ```twig
   {% if settings.{nombre}_show %}
   <section class="section-{nombre} mb-5" data-store="home-{nombre}">
       <div class="container">
           <h2 class="h2 text-center">{{ settings.{nombre}_title | translate }}</h2>
           {# Contenido aquí #}
       </div>
   </section>
   <style>
   .section-{nombre} {
       background: var(--main-background);
       color: var(--main-foreground);
   }
   </style>
   {% endif %}
   ```
