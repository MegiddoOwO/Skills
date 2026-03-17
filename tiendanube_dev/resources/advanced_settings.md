# ⚙️ Componentes Avanzados de `settings.txt`

Tiendanube ofrece componentes potentes para el administrador que van más allá de simples textos.

## 🖼️ El Componente `gallery`
Permite al usuario subir múltiples imágenes con links y textos de forma dinámica.

```text
mi_galeria
    type = gallery
    gallery_image = Cargar Foto
    gallery_link = Enlace (Opcional)
    gallery_width = 800
    gallery_height = 800
    gallery_more_info = true (Habilita campos de título y descripción por slide)
```

**Uso en Twig:**
```twig
{% for item in settings.mi_galeria %}
    <img src="{{ item.image | static_url }}">
    <a href="{{ item.link }}">{{ item.title }}</a>
{% endfor %}
```

---

## 🌎 El Componente `i18n_input`
Genera automáticamente campos para todos los idiomas activos en la tienda (ES, PT, EN).

```text
mi_titulo_traducible
    type = i18n_input
    description = Título de la sección
```

**Uso en Twig (automático):**
```twig
<h2>{{ settings.mi_titulo_traducible | translate }}</h2>
```

---

## 📂 El Componente `collapse` y `form_group`
Sirven para organizar visualmente el panel de administración.

```text
mi_grupo_ajustes
    collapse
        title = Ajustes Visuales
    checkbox
        name = mostrar_borde
        description = Mostrar borde en fotos
    color
        name = color_borde
        description = Color del borde
```

---

## 🔢 Rangos y Pasos (`range_number`)
Ideal para tamaños de fuente o anchos de contenedor.

```text
font_size
    type = range_number
    min = 12
    max = 24
    step = 2
```
