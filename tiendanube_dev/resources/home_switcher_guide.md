# 🔄 Guía: Home Section Switcher (El Cerebro de Scatola)

En la tienda Scatola, el orden de las secciones en el Home no es estático; el administrador puede reordenarlas desde el panel. Aquí te explicamos cómo funciona y cómo agregar una nueva.

## 1. El Bucle en `templates/home.tpl`

El archivo `home.tpl` suele recorrer un rango de posiciones (ej. 1 a 18):

```twig
{% for i in 1..18 %}
    {% set section_select = attribute(settings, 'home_order_position_' ~ i) %}
    {% include 'snipplets/home/home-section-switch.tpl' %}
{% endfor %}
```

## 2. El Orquestador: `home-section-switch.tpl`

Este archivo recibe `section_select` y decide qué snipplet incluir:

```twig
{% if section_select == 'slider' %}
    {% include 'snipplets/home/home-slider.tpl' %}
{% elseif section_select == 'mi_nueva_seccion' %}
    {% include 'snipplets/home/mi-nueva-seccion.tpl' %}
{% endif %}
```

## 3. Configuración en `defaults.txt`

Debes definir el orden por defecto para que la tienda no se vea vacía inicialmente:

```text
home_order_position_1 = slider
home_order_position_2 = products
home_order_position_3 = mi_nueva_seccion
...
```

## 4. Configuración en `settings.txt`

Para que el usuario pueda elegir tu sección, debes agregarla a los dropdowns de `home_order_position` (esto suele estar en una sección de "Orden de secciones"):

```text
home_order_position_1
    type = select
    values
        empty = Ocultar
        slider = Carrusel de imágenes
        products = Productos destacados
        mi_nueva_seccion = Mi Nueva Sección Increíble
```

---

## 💡 Pro-Tip: Modo Preview

Siempre usa `params.preview` para mostrar contenido de ejemplo cuando el usuario está en el personalizador pero aún no ha cargado datos:

```twig
{% if has_data or params.preview %}
    {# Renderizar sección #}
{% endif %}
```
