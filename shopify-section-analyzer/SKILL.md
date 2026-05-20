---
name: shopify-section-analyzer
description: Analiza imágenes de diseño para generar prompts estructurados para maquetar secciones, bloques o snippets en Shopify. Úsala SIEMPRE que el usuario suba una imagen de un diseño o mockup que quiera convertir en código Shopify Liquid. También actívala cuando el usuario diga frases como "Realiza esta seccion en base a esta imagen","quiero maquetar esta sección", "pasa esta imagen a Shopify", "maqueta este diseño", "crea esta sección en Liquid", "convierte este diseño a Shopify", o cuando comparta cualquier imagen de referencia visual con intención de desarrollar en Shopify. TAMBIÉN actívala en modo corrección cuando el usuario suba DOS imágenes indicando cuál es el diseño esperado y cuál es como quedó la sección actualmente — frases como "La seccion no quedo como viene en la imagen","no quedó como quería", "esto no se parece al diseño", "corrígeme esta sección", "la sección no coincide con el diseño", "tengo el diseño y cómo quedó" son señales claras de este modo. No esperes a que el usuario pida explícitamente un "prompt estructurado" — si hay imagen + intención Shopify, activa esta skill.
---

# Shopify Section Analyzer

Skill para analizar imágenes de diseño y generar prompts estructurados que guíen el desarrollo de secciones, bloques o snippets en Shopify Liquid.

---

## Detección de modo — Lo primero que debes hacer

Antes de cualquier análisis, identifica en cuál de estos dos modos estás operando:

### MODO A — Maquetación desde cero

**Señales:** El programador sube UNA imagen (el diseño objetivo) y quiere convertirla en una sección Shopify nueva.
→ Sigue el **Flujo de Maquetación** más abajo.

### MODO B — Corrección de sección existente

**Señales:** El programador sube DOS imágenes y especifica cuál es el diseño esperado y cuál es como quedó la sección actualmente. Frases típicas: "no quedó como quería", "corrígeme esto", "no se parece al diseño", "tengo el diseño y cómo quedó".
→ Sigue el **Flujo de Corrección** más abajo.

**Si el programador sube dos imágenes sin aclarar cuál es cuál, pregunta antes de continuar:**

> "¿Puedes indicarme cuál imagen es el diseño esperado y cuál es cómo quedó la sección actualmente?"

---

## Flujo de Maquetación (MODO A)

Sigue estos pasos en orden. No te saltes ninguno.

### PASO 1 — Análisis visual de la imagen

Cuando recibas una imagen, analízala profundamente como desarrollador Shopify senior. Extrae y documenta:

**Estructura y layout**

- Tipo de componente (sección completa, bloque dentro de sección, snippet reutilizable, header, footer, popup)
- Layout detectado: hero, grid, columns (cuántas), slider/carousel, accordion, tabs, sticky, split (imagen + texto), card grid, banner
- Jerarquía visual: qué elemento es protagonista, qué es secundario, qué es apoyo
- Alineación general (centrado, izquierda, asimétrico)

**Elementos presentes**
Lista todos los elementos que veas:

- Textos: headlines, subtítulos, párrafos, etiquetas, badges, precios
- Medios: imágenes de fondo, imágenes de producto, íconos, videos
- Interactivos: botones (cuántos, qué tipo), links, formularios, inputs, selects
- Decorativos: separadores, fondos de color, overlays, gradientes, formas

**Comportamiento visible o inferible**

- ¿Hay indicadores de slider (dots, flechas)?
- ¿Hay estados hover visibles o implícitos?
- ¿Hay secciones que parecen colapsables?
- ¿Hay animaciones sugeridas?

**Responsive**

- ¿Se ve cómo se comportaría en móvil?
- ¿Hay cambios de layout evidentes entre desktop y móvil?

---

### PASO 2 — Clasificar el componente Shopify

Después del análisis visual, determina qué tipo de archivo Shopify corresponde:

| Tipo                        | Cuándo usarlo                                            |
| --------------------------- | -------------------------------------------------------- |
| `sections/nombre.liquid`    | Componente completo agregable desde el editor de temas   |
| `blocks/` dentro de section | Elementos repetibles configurables dentro de una sección |
| `snippets/nombre.liquid`    | Componente reutilizable sin schema propio                |
| `layout/`                   | Si afecta estructura global (header, footer)             |

Explica al programador por qué elegiste esa clasificación.

---

### PASO 3 — Preguntas críticas (máximo 4)

Solo pregunta lo que la imagen NO puede revelar. Elige únicamente las preguntas que sean bloqueantes para el desarrollo. Ejemplos de preguntas válidas:

- ¿Los textos (headline, descripción) son editables desde el editor de temas o están fijos?
- ¿Las imágenes vienen de productos de Shopify, de metafields, o son imágenes estáticas del tema?
- ¿El slider (si hay) avanza automáticamente o solo con interacción del usuario?
- ¿Esta sección debe aparecer en todas las páginas o solo en específicas?
- ¿Los colores de fondo/botones deben usar variables del tema (`--color-button`) o son valores fijos del diseño?
- ¿Hay lógica de Liquid condicional que debamos manejar (mostrar solo si hay producto, si hay descuento, etc.)?

**Nunca hagas más de 4 preguntas.** Si puedes inferirlo razonablemente, hazlo y documéntalo como supuesto.

---

### PASO 4 — Generar el prompt estructurado

Con el análisis visual + las respuestas del programador, genera el prompt final. Usa esta estructura obligatoria:

```
## PROMPT SHOPIFY — [Nombre descriptivo de la sección]

### Tipo de componente
[section / snippet / block — con nombre de archivo sugerido]

### Descripción general
[Qué hace esta sección y cuál es su propósito en la tienda]

### Layout y estructura HTML
[Descripción de la estructura de contenedores, filas, columnas]
Ejemplo de estructura sugerida:
<section>
  <div class="container">
    <!-- elementos detectados en orden de jerarquía -->
  </div>
</section>

### Elementos y contenido
[Lista detallada de cada elemento, su tipo y de dónde viene el contenido]
- Headline → setting tipo text en schema
- Imagen de fondo → setting tipo image_picker en schema
- Botón CTA → settings: label (text) + url (url) en schema
- [etc.]

### Schema settings sugeridos
[Lista de settings que debe tener el {% schema %}]
- type: "text" | name: "Título" | id: "title"
- type: "image_picker" | name: "Imagen de fondo" | id: "bg_image"
- type: "color" | name: "Color de fondo" | id: "bg_color"
- [etc.]

### Comportamiento e interactividad
[Descripción de toda la lógica JS necesaria]
- [Nombre del comportamiento]: [Cómo debe funcionar]

### Responsive
[Cómo debe adaptarse en mobile vs desktop]

### Supuestos documentados
[Lista de decisiones que tomaste sin preguntar y por qué]
- Supuse que X porque en la imagen se ve Y
- Supuse que los colores usan variables del tema porque es buena práctica

### Variables Liquid probables
[Lista de variables o lógica Liquid que se va a necesitar]
- {{ section.settings.title }}
- {% if section.settings.bg_image != blank %}
- {% for block in section.blocks %}
```

---

### PASO 5 — Confirmación y ajuste

Después de entregar el prompt, pregunta:

> "¿Hay algo en este prompt que no corresponde con tu visión del diseño o que quieras ajustar antes de pasarlo a desarrollo?"

Si el programador ajusta algo, actualiza el prompt completo y entrega la versión final limpia.

---

## Flujo de Corrección (MODO B)

Cuando el programador pasa dos imágenes para corregir una sección existente, sigue este flujo especializado.

---

### PASO C1 — Análisis comparativo visual

Examina ambas imágenes en paralelo como desarrollador Shopify senior. Construye una tabla de diferencias organizada por categoría:

**Layout y estructura**

- ¿Cambió el número de columnas o filas?
- ¿Cambió el orden de los elementos?
- ¿Hay elementos que aparecen en el diseño pero no en la implementación (o viceversa)?
- ¿Cambió el espaciado general (padding, margin, gaps)?

**Tipografía**

- ¿Difieren los tamaños de fuente?
- ¿Hay diferencias en peso (bold/regular), familia tipográfica o alineación del texto?
- ¿Hay diferencias en interlineado o letter-spacing?

**Colores y estilos visuales**

- ¿Colores de fondo, bordes, botones o textos son diferentes?
- ¿Falta o sobra algún overlay, gradiente o sombra?
- ¿Bordes redondeados (border-radius) distintos?

**Imágenes y medios**

- ¿La imagen tiene proporciones, recorte o posición diferente (object-position)?
- ¿Falta o sobra alguna imagen o ícono?

**Elementos faltantes o sobrantes**

- ¿Qué elementos están en el diseño pero no aparecen en la implementación?
- ¿Qué elementos aparecen en la implementación pero no deberían estar según el diseño?

**Responsive (si aplica)**

- ¿Las diferencias son solo en mobile o también en desktop?

---

### PASO C2 — Priorización de correcciones

Clasifica cada diferencia detectada en tres niveles:

| Prioridad         | Criterio                                 | Ejemplos                                                             |
| ----------------- | ---------------------------------------- | -------------------------------------------------------------------- |
| 🔴 **Crítica**    | Rompe el diseño o la funcionalidad       | Elemento faltante, layout completamente distinto, imagen rota        |
| 🟡 **Importante** | Afecta visualmente de forma notable      | Colores incorrectos, tipografía equivocada, espaciados muy distintos |
| 🟢 **Menor**      | Detalle fino que puede ajustarse después | Letter-spacing levemente distinto, sombra más suave                  |

---

### PASO C3 — Preguntas críticas de corrección (máximo 3)

Solo pregunta lo que no puedas inferir de las imágenes y que sea bloqueante para generar las correcciones. Ejemplos válidos:

- ¿Las diferencias de color son porque se usaron valores hardcodeados en lugar de variables del tema?
- ¿El elemento faltante [X] existe en el código pero está oculto con CSS, o nunca fue implementado?
- ¿Las diferencias en mobile son intencionales o también deben corregirse?

---

### PASO C4 — Generar el prompt de correcciones

Con el análisis comparativo y las respuestas del programador, genera el prompt de correcciones. Usa esta estructura:

```
## PROMPT DE CORRECCIÓN — [Nombre de la sección]

### Contexto
Sección existente que no coincide con el diseño esperado.
Archivo probable: sections/[nombre].liquid

### Resumen de diferencias detectadas
[Descripción breve de cuántas y qué tipo de diferencias hay]

### Correcciones críticas 🔴
[Lista de correcciones que deben aplicarse primero]

1. [Elemento/propiedad] — ESPERADO: [descripción] | ACTUAL: [descripción]
   → Corrección: [qué cambiar exactamente y dónde]

2. [Elemento/propiedad] — ESPERADO: [descripción] | ACTUAL: [descripción]
   → Corrección: [qué cambiar exactamente y dónde]

### Correcciones importantes 🟡
[Lista de correcciones visuales notables]

1. [Elemento/propiedad] — ESPERADO: [descripción] | ACTUAL: [descripción]
   → Corrección: [qué cambiar exactamente y dónde]

### Correcciones menores 🟢
[Ajustes finos opcionales]

1. [Elemento/propiedad] — ESPERADO: [descripción] | ACTUAL: [descripción]
   → Corrección: [qué cambiar exactamente y dónde]

### Áreas sin diferencias detectadas
[Qué partes de la sección ya están correctas y no deben tocarse]

### Supuestos documentados
[Decisiones asumidas sin preguntar y por qué]
- Supuse que X porque en la imagen se observa Y

### Orden de aplicación recomendado
1. Primero corregir las críticas: [lista]
2. Luego las importantes: [lista]
3. Finalmente los detalles menores: [lista]
```

---

### PASO C5 — Confirmación

Después de entregar el prompt de correcciones, pregunta:

> "¿Hay alguna diferencia que no detecté o alguna corrección que no deba aplicarse?"

Si el programador agrega o descarta correcciones, actualiza el prompt y entrega la versión final limpia.

---

## Reglas generales

- **Piensa siempre como desarrollador Shopify**, no como diseñador gráfico
- **Documenta todos los supuestos** — es mejor asumir y documentar que dejar ambigüedad
- **Usa nomenclatura Shopify real**: `section.settings`, `block.settings`, `{% schema %}`, `{% stylesheet %}`, `{% javascript %}`
- **Sugiere buenas prácticas** cuando las veas necesarias (ej: lazy loading en imágenes, uso de `image_url` filter)
- **No generes código Liquid todavía** — el objetivo de la skill es el prompt estructurado, no el código final
- Si la imagen es de baja calidad o ambigua, dilo explícitamente y describe qué partes no puedes inferir con certeza

---

## Ejemplo de output esperado

Imagen recibida: hero section con imagen de fondo, headline centrado, subtítulo, botón CTA y overlay oscuro.

```
## PROMPT SHOPIFY — Hero Section con Overlay

### Tipo de componente
sections/hero-banner.liquid

### Descripción general
Sección hero de pantalla completa con imagen de fondo, overlay oscuro semitransparente,
headline principal, subtítulo y botón de llamada a la acción centrado verticalmente.

### Layout y estructura HTML
Contenedor full-width con position relative. Imagen de fondo como background-image
o tag <img> con object-fit cover. Overlay como div absoluto con opacity.
Contenido centrado con flexbox (column, center center).

### Elementos y contenido
- Imagen de fondo → image_picker en schema
- Overlay → color + opacity configurable en schema
- Headline (H1) → text en schema
- Subtítulo → textarea en schema
- Botón CTA → text (label) + url en schema

### Schema settings sugeridos
- type: "image_picker" | id: "bg_image" | label: "Imagen de fondo"
- type: "range" | id: "overlay_opacity" | min: 0 | max: 100 | step: 5 | label: "Opacidad del overlay"
- type: "color" | id: "overlay_color" | label: "Color del overlay" | default: "#000000"
- type: "text" | id: "heading" | label: "Título principal"
- type: "textarea" | id: "subheading" | label: "Subtítulo"
- type: "text" | id: "btn_label" | label: "Texto del botón"
- type: "url" | id: "btn_url" | label: "URL del botón"

### Comportamiento e interactividad
- Ninguno detectado. Sección estática.

### Responsive
- Desktop: altura mínima 600px, contenido centrado
- Mobile: altura mínima 400px, padding horizontal reducido, fuente del headline más pequeña

### Supuestos documentados
- Supuse overlay negro porque es el color visible en la imagen
- Supuse que heading y subheading son editables porque es un hero principal
- Supuse que el botón tiene un solo CTA (solo hay uno visible)

### Variables Liquid probables
- {{ section.settings.heading }}
- {{ section.settings.bg_image | image_url: width: 1920 }}
- {% if section.settings.btn_label != blank %}
```
