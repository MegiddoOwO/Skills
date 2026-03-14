# Desarrollador de Secciones y Bloques (Shopify Liquid)

## Objetivo
Crear secciones y bloques de Shopify Liquid que sean técnicamente perfectos, sigan la documentación oficial y ofrezcan una experiencia de usuario (UX) excepcional para el comerciante a través del Customizer.

## Instrucciones de Flujo Crítico

### 1. Validación de API (MCP)
- **Acción Obligatoria**: Invoca el servidor MCP `shopify-dev-mcp` usando la herramienta `learn_shopify_api` antes de generar cualquier código.
- **Meta**: Verificar compatibilidad de objetos Liquid y APIs con la versión actual de Shopify.

### 2. Lógica de Desarrollo de Bloques
- **Regla Estricta**: NO desarrolles bloques a menos que el usuario lo solicite explícitamente.
- Si no se mencionan bloques, la sección debe ser funcional por sí sola o basada en configuraciones globales.

### 3. Filosofía de "Merchant First" (Configurabilidad)
- Cada sección DEBE tener un schema de configuraciones robusto.
- **Obligatorio incluir**:
    - Selectores de color.
    - Ajustes de espaciado (padding/margin).
    - Alineación de texto.
    - Selectores de imagen (`image_picker`).
    - Opciones de visibilidad.
- **Idioma**: Todo el schema (`label`, `info`, `content`) DEBE estar en **español**.

### 4. Auditoría de Accesibilidad y Responsividad (Integración)
- **Acción Obligatoria**: Una vez finalizada y validada la creación de la sección, se DEBE invocar a la skill `auditor-ui-responsiva-ux`.
- **Meta**: Evaluar la implementación de unidades relativas, tipografía fluida y estándares de accesibilidad WCAG 2.2 para garantizar una UX excepcional en todos los dispositivos.

## Estándares Técnicos

### Rendimiento
- Uso eficiente de filtros de imagen (`image_url`, `srcset`).
- Implementar carga perezosa (`loading="lazy"`) para imágenes.
- Evitar ciclos `for` innecesarios para optimizar el TTFB.

### Estructura
- Separación clara entre:
    - HTML/Liquid.
    - `{% style %}`: CSS encapsulado usando el ID de la sección.
    - `{% schema %}`: Configuración JSON en español.

## Restricciones
- NO usar librerías externas (jQuery, Bootstrap) a menos que se solicite. Preferir Vanilla JS y CSS puro.
- Referencia siempre los archivos en `.agent/skills/shopify-dev/reference/` para asegurar la precisión técnica.

## Referencias Disponibles
- [Arquitectura](file:///home/megiddo/Documentos/shopify/dabalash/.agent/skills/shopify-dev/reference/structure.md)
- [Settings del Schema](file:///home/megiddo/Documentos/shopify/dabalash/.agent/skills/shopify-dev/reference/schema-settings.md)
- [Mejores Prácticas](file:///home/megiddo/Documentos/shopify/dabalash/.agent/skills/shopify-dev/reference/best-practices.md)

## Ejemplos
- [Sección Básica](file:///home/megiddo/Documentos/shopify/dabalash/.agent/skills/shopify-dev/examples/basic-section.liquid)
- [Sección Avanzada](file:///home/megiddo/Documentos/shopify/dabalash/.agent/skills/shopify-dev/examples/advanced-section.liquid)
