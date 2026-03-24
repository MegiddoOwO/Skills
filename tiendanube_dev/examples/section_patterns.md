# Ejemplos y Patrones de Diseño: Secciones

Patrones recomendados para la generación de secciones modulares y eficientes en Tiendanube.

## 💎 Patrones de Componentes

### 1. Inclusión de Sniperlets
- **Simple:** `{% snipplet "snipplets/banner.tpl" %}`.
- **Dinámico (Slots):** `{% embed "snipplets/card.tpl" %}` para inyectar bloques HTML dentro de un componente base.

### 2. Secciones de Banner/Hero (LCP)
- Utilizar `<img>` con `srcset` para responsividad.
- `loading="eager"` para la primera imagen visible (Prioridad de Carga).

### 3. Carruseles (Swiper.js)
- El marcado HTML debe estar en un snipplet limpio.
- La ejecución de JS debe encapsularse en `{% verbatim %}` si se incluye dentro del snipplet para evitar colisiones con el compilador Twig.

### 4. Grillas Dinámicas
- **Límite:** Utilizar el filtro `| take(n)` para asegurar que el diseño no se sature.
- **Validación:** Siempre usar `is not empty` para colecciones antes de renderizar el contenedor.

### 5. Skeleton Loaders (AJAX)
- Para secciones como "Búsqueda Rápida" o "Carrito Lateral", incluir un estado de "Shimmer" en el snipplet que se muestre mientras los datos se cargan vía AJAX.

---

## 🛠️ Snippets de Referencia

### Loop de Productos con Validación
```twig
{% if settings.show_featured_products %}
    {% set featured_products = sections.featured.products | take(4) %}
    {% if featured_products is not empty %}
        <div class="product-grid row">
            {% for product in featured_products %}
                {% include 'snipplets/product-item.tpl' with {'product': product} %}
            {% endfor %}
        </div>
    {% endif %}
{% endif %}
```

### 6. Selección Dinámica de Secciones
Pattern para permitir que el mercader elija qué widget mostrar desde un `select` en el admin:

```twig
{# settings.home_featured_section contiene el ID definido en sections.txt #}
{% set selected_section = sections[settings.home_featured_section] %}

{% if selected_section.products is not empty %}
    <h2 class="title">{{ selected_section.name }}</h2>
    <div class="grid">
        {% for product in selected_section.products | take(4) %}
            {% snipplet "product_grid.tpl" %}
        {% endfor %}
    </div>
{% endif %}
```

### 7. Optimización de Listas con `slice`
Ideal para layouts que requieren saltar el primer elemento (ej: una grilla con un "Main Feature"):

```twig
{% set extra_products = sections.home.products | slice(1, 3) %}
{% for product in extra_products %}
    {# Renderiza productos del 2 al 4 #}
{% endfor %}
```

### 8. Lógica de Badge de Oferta (Complex Twig)
```twig
{% if product.compare_at_price > product.price %}
    {% set percentage = ((product.compare_at_price - product.price) / product.compare_at_price * 100) | round %}
    <span class="badge badge-sale">-{{ percentage }}%</span>
{% endif %}
```
