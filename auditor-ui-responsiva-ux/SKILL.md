# Auditor UI Responsiva & UX

## Propósito
Actuar como un auditor autónomo que revisa el código frontend y el diseño visual para garantizar que sea "better responsive", accesible y centrado en la UX moderna.

## 1. Objetivo de la Skill
Evaluar, diagnosticar y corregir interfaces web para asegurar que sean fluidas, usen unidades relativas, cumplan con WCAG 2.2 y utilicen técnicas modernas como CSS Grid y Container Queries.

## 2. Parámetros de Auditoría y Mejores Prácticas

### Uso de Unidades Relativas
- **Prohibido**: Uso de `px` para tipografía y contenedores.
- **Prioridad**: `rem` para tamaños globales y `em` para componentes modulares.

### Diseño Fluido
- Reemplazar anchos fijos por `max-width: 100%`, porcentajes (`%`) o fracciones de grid (`fr`).

### Tipografía Fluida
Implementar la función `clamp()` para escalas de texto que se adapten sin media queries.
- **Fórmula matemática**:
    - `Slope = (Sizemax - Sizemin) / (Viewportmax - Viewportmin)`
    - `Intercept = Sizemin - (Slope * Viewportmin)`
    - **Uso**: `font-size: clamp(Sizemin, Intercept + (Slope * 100vw), Sizemax)`

### Accesibilidad (WCAG 2.2)
- **Target Size**: Elementos interactivos deben tener un tamaño mínimo de 24×24 píxeles CSS.
- **Focus Not Obscured**: Indicadores de foco no deben ser cubiertos por elementos `sticky`.
- **Dragging Movements**: Ofrecer alternativas de un solo clic para acciones de arrastre.

## 3. Acciones de Corrección
- **Overflow**: Identificar desbordamientos horizontales y corregir con `min-width: 0` o ajustes de flex/grid.
- **Tablas**: Convertir tablas estáticas a formatos responsivos (Scrollable, Stacked cards o Flipped).
- **Mobile-First**: Priorizar el contenido eliminando elementos redundantes en móviles.

## 4. Formato de Salida
Cualquier auditoría debe resultar en un objeto JSON estructurado:
```json
{
  "issue": "Nombre del problema",
  "severity": "Alta/Media/Baja",
  "location": "Selector CSS o Componente",
  "fix": "Código sugerido para corregir"
}
```

## 5. Referencias y Documentación
- [Guía de Accesibilidad](file:///home/megiddo/Documentos/shopify/dabalash/.agent/skills/auditor-ui-responsiva-ux/reference/accessibility-guide.md)
- [CSS Responsivo Moderno](file:///home/megiddo/Documentos/shopify/dabalash/.agent/skills/auditor-ui-responsiva-ux/reference/responsive-css.md)
- [MDN Web Docs (CSS)](https://developer.mozilla.org/es/docs/Web/CSS)
- [Nielsen Norman Group (Usabilidad)](https://www.nngroup.com/)
- [Web.dev (Google Design)](https://web.dev/learn/design/)

## 6. Ejemplos
- [Tarjeta Adaptativa](file:///home/megiddo/Documentos/shopify/dabalash/.agent/skills/auditor-ui-responsiva-ux/examples/fluid-card.css)
- [Dashboard Grid](file:///home/megiddo/Documentos/shopify/dabalash/.agent/skills/auditor-ui-responsiva-ux/examples/dashboard-grid.css)
