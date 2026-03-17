---
description: Flujo para crear un formulario de contacto funcional y sincronizado con el admin
---

## 📧 Creación de Formulario de Contacto

### 🚨 PASO 0: Protocolo de Diagnóstico (OBLIGATORIO)

Antes de proceder, el agente debe aplicar la **Biblia de Scatola** (`.agent/skills/tiendanube_master/SKILL.md`) y realizar las 5 preguntas del Protocolo de Diagnóstico al usuario. **No se debe generar código hasta que los 5 puntos estén validados.**

**IMPORTANTE:** Para que los mensajes aparezcan en el panel de Tiendanube, los IDs deben ser exactos.

1. **Snippet del Formulario (`snipplets/home/home-{nombre}.tpl`)**

   ```twig
   {% embed "snipplets/forms/form.tpl" with{
       form_id: 'contact-form',        // ⚠️ CRÍTICO: No cambiar
       form_action: '/winnie-pooh',    // ⚠️ CRÍTICO: No cambiar
       data_store: 'contact-form'      // ⚠️ CRÍTICO: No cambiar
   } %}
       {% block form_body %}
           {# Honeypot anti-spam #}
           <div class="winnie-pooh hidden">
               <input type="text" name="winnie-pooh">
           </div>

           <input type="hidden" name="type" value="contact" />

           {# Campos (usar snipplets/forms/form-input.tpl) #}
           {% include 'snipplets/forms/form-input.tpl' with {input_name: 'name', input_label_text: 'Nombre' | translate} %}
           {% include 'snipplets/forms/form-input.tpl' with {input_name: 'email', type_email: true, input_label_text: 'Email' | translate} %}
           {% include 'snipplets/forms/form-input.tpl' with {input_name: 'message', text_area: true, input_label_text: 'Mensaje' | translate} %}
       {% endblock %}
   {% endembed %}
   ```

2. **Seguridad y Validación:** Asegurar que el campo `winnie-pooh` esté presente para evitar spam.
