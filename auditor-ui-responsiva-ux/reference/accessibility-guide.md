# Guía de Accesibilidad (WCAG 2.2) para Auditoría UI

Esta guía detalla los criterios específicos que deben revisarse durante una auditoría de accesibilidad.

## 1. Target Size (Tamaño del Objetivo)
Los elementos interactivos deben facilitar su activación, especialmente en dispositivos táctiles.
- **Criterio**: El tamaño mínimo de cualquier elemento interactivo debe ser de **24×24 píxeles CSS**.
- **Excepción**: Si hay un espaciado equivalente alrededor del elemento que sume el área mínima.

## 2. Focus Not Obscured (Foco no Obscurecido)
Asegura que el usuario siempre sepa qué elemento tiene el foco del teclado.
- **Problema común**: Elementos `sticky` (cabeceras, banners) que cubren el elemento enfocado al hacer scroll.
- **Solución**: Usar `scroll-margin-top` o `scroll-padding-top` para asegurar un margen visual cuando se navega con el teclado.

## 3. Dragging Movements (Movimientos de Arrastre)
No todos los usuarios pueden realizar acciones de arrastre con precisión.
- **Requisito**: Cualquier funcionalidad que requiera arrastrar (ej. reordenar una lista, slider) debe tener una alternativa de **un solo clic** (ej. botones de "subir"/"bajar" o clics en puntos específicos).

## 4. Contrastes y Tipografía
- **Contraste**: Mínimo 4.5:1 para texto normal y 3:1 para texto grande.
- **Escalabilidad**: El texto debe poder aumentarse hasta un 200% sin pérdida de funcionalidad o contenido.
- **Unidades**: NUNCA usar `px` para `font-size`. Usar `rem`.
