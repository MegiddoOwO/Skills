# Arquitectura de Secciones y Bloques de Shopify

## Secciones
Las secciones son archivos Liquid que permiten crear módulos de contenido reutilizables que pueden ser personalizados por los comerciantes.

### Características Clave
- **Reutilización**: Se pueden usar en múltiples plantillas JSON.
- **Configurabilidad**: Utilizan la etiqueta `{% schema %}` para exponer ajustes en el editor de temas.
- **Límites**: Se pueden renderizar hasta 25 secciones en una plantilla JSON.
- **Bloques**: Soporte para hasta 50 bloques por sección.

### Renderizado
- **Dinámico**: Recomendado. Referenciado en plantillas JSON o grupos de secciones.
- **Estático**: Usando `{% section 'nombre-archivo' %}`. No permite reordenamiento por el comerciante.

## Bloques
Los bloques permiten a los comerciantes agregar, eliminar y reordenar contenido dentro de una sección.

### Tipos de Bloques
- **Bloques de Tema**: Definidos en el schema de la sección.
- **Bloques de Aplicación**: Permiten a los desarrolladores de apps insertar contenido sin editar el código del tema.

### Atributos del Bloque
- `type`: Identificador único (free-form string).
- `name`: Título visible en el editor.
- `limit`: Cantidad máxima de bloques de este tipo.
- `settings`: Ajustes específicos del bloque.

### Renderizado de Bloques
```liquid
{% for block in section.blocks %}
  {% case block.type %}
    {% when 'slide' %}
      <div class="slide" {{ block.shopify_attributes }}>
        {{ block.settings.image | image_url: width: 2048 | image_tag }}
      </div>
  {% endcase %}
{% endfor %}
```
> [!IMPORTANT]
> Siempre usa `{{ block.shopify_attributes }}` en el contenedor raíz del bloque para que el editor de temas pueda identificarlo.
