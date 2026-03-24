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
