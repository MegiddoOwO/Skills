# CSS Responsivo Moderno: Técnicas y Unidades

Guía técnica para la implementación de interfaces fluidas y adaptativas.

## 1. Unidades Relativas vs Fijas
- **REM**: Relativo al tamaño de fuente del elemento raíz (`html`). Ideal para tipografía y espaciado consistente.
- **EM**: Relativo al tamaño de fuente del elemento padre. Útil para componentes que deben escalar proporcionalmente a su texto (ej. iconos dentro de botones).
- **CH**: Relativo al ancho del carácter '0'. Excelente para limitar el ancho de párrafos de texto (ideal: 45-75ch).

## 2. Flexbox vs CSS Grid
- **Flexbox**: Control en una dimensión (filas O columnas). Ideal para alineación de menús, botones y componentes pequeños.
- **CSS Grid**: Control en dos dimensiones. Ideal para layouts de página completos y dashboards complejos.
    - Uso de `minmax()` y `auto-fit`/`auto-fill` para rejillas que no requieren media queries.

## 3. Tipografía Fluida con `clamp()`
La función `clamp(min, preferred, max)` permite que el valor se mueva entre un mínimo y un máximo basado en un valor preferido (usualmente usando `vw`).

**Fórmula de Slope e Intercept**:
```css
font-size: clamp(1rem, 0.8rem + 1vw, 1.5rem);
```

## 4. Container Queries
Permiten estilizar un elemento basado en el tamaño de su contenedor, no del viewport total.
```css
.container { container-type: inline-size; }
@container (min-width: 400px) {
  .card { display: flex; }
}
```

## 5. Prevención de Overflow
- Usar `min-width: 0` en elementos flex/grid para permitir que se reduzcan por debajo de su contenido intrínseco.
- Usar `overflow-wrap: break-word` para textos largos que podrían romper el layout.
