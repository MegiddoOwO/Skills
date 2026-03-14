# Configuración del Schema (Input Types)

El schema (`{% schema %}`) define cómo se presentan las opciones de personalización al comerciante.

## Atributos Estándar
| Atributo | Descripción | Requerido |
| :--- | :--- | :--- |
| `type` | Tipo de input (ej. `text`, `image_picker`) | Sí |
| `id` | ID para acceder al valor en Liquid | Sí |
| `label` | Etiqueta visible en el editor (Español recomendado) | Sí |
| `default` | Valor por defecto | No |
| `info` | Texto de ayuda adicional | No |

## Basic Input Settings
- **`checkbox`**: Retorna `boolean`.
- **`number`**: Retorna `number` o `nil`.
- **`radio`**: Selección de una opción entre varias.
- **`range`**: Slider numérico con `min`, `max`, `step` y `unit`.
- **`select`**: Menú desplegable o control segmentado.
- **`text`**: Campo de texto de una línea.
- **`textarea`**: Campo de texto multilínea.

## Specialized Input Settings
- **`image_picker`**: Selector de imágenes de la biblioteca. Retorna objeto `image`.
- **`color`**: Selector de color. Retorna objeto `color`.
- **`color_background`**: Campo para gradientes o fondos CSS.
- **`url`**: Selector de enlaces (páginas, productos, externos).
- **`richtext`**: Editor de texto enriquecido (HTML).
- **`inline_richtext`**: Richtext simplificado (sin etiquetas de bloque).
- **`product` / `collection`**: Selectores de recursos específicos.
- **`product_list` / `collection_list`**: Permite seleccionar múltiples elementos.

## Ejemplo de Schema Robusto (Merchant First)
```json
{
  "name": "Sección de Ejemplo",
  "settings": [
    {
      "type": "header",
      "content": "Diseño y Colores"
    },
    {
      "type": "color",
      "id": "background_color",
      "label": "Color de fondo",
      "default": "#ffffff"
    },
    {
      "type": "range",
      "id": "padding_top",
      "min": 0,
      "max": 100,
      "step": 4,
      "unit": "px",
      "label": "Espaciado superior",
      "default": 36
    }
  ]
}
```
