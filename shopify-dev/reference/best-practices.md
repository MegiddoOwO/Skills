# Mejores Prácticas de Rendimiento y Desarrollo

## Rendimiento (Performance)
- **Imágenes**:
    - Usa siempre el filtro `image_url` con tamaños específicos.
    - Implementa `srcset` para adaptabilidad.
    - Usa `loading="lazy"` para imágenes debajo de la mitad superior de la página (below the fold).
- **TTFB**:
    - Evita ciclos `for` anidados excesivos.
    - No realices peticiones de red o cálculos complejos dentro del renderizado Liquid.

## Estructura y Estilos
- **Encapsulación de CSS**:
    - Usa la etiqueta `{% style %}` para estilos específicos de la instancia.
    - Prefiere variables CSS (`--variable`) pasadas desde el schema.
- **JavaScript**:
    - Usa la etiqueta `{% javascript %}` para lógica global o componentes web.
    - Evita librerías externas pesadas (jQuery); prefiere Vanilla JS.
    - Utiliza `data-*` attributes para pasar configuraciones del schema al JS.

## Merchant Experience (UX)
- **Labels en Español**: Todos los labels, info y content del schema deben estar en español.
- **Documentación Inline**: Usa la etiqueta `{% doc %}` para explicar el propósito de snippets complejos.
- **Visual Preview**: Asegúrate de que los cambios en el Customizer se reflejen instantáneamente mediante eventos de JavaScript si es necesario.

## Etiquetas Críticas
- `{% schema %}`: Definición de la configuración.
- `{% stylesheet %}`: CSS concatenado por Shopify.
- `{% javascript %}`: JS concatenado y cargado con `defer`.
