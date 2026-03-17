# 🛠️ Ejemplo: Sección de Banner Personalizado

Este ejemplo muestra cómo crear una sección de banner con título, descripción, imagen de fondo y botón de acción (CTA).

## 📄 HTML + Twig (`snipplets/home/custom-banner.tpl`)

```twig
{# 1. Captura de variables desde settings #}
{% set banner_image = settings.custom_banner_image | static_url %}
{% set banner_title = settings.custom_banner_title | default('Bienvenido a nuestra tienda') %}
{% set banner_text = settings.custom_banner_text %}
{% set banner_button_text = settings.custom_banner_button_text %}
{% set banner_button_link = settings.custom_banner_button_link %}

{# 2. Estructura HTML #}
<section id="custom-banner" class="section-custom-banner" style="background-image: url('{{ banner_image }}');">
    <div class="container">
        <div class="row">
            <div class="col-md-6 content-wrapper">
                <h2 class="banner-title">{{ banner_title }}</h2>
                {% if banner_text %}
                    <p class="banner-description">{{ banner_text }}</p>
                {% endif %}
                {% if banner_button_text and banner_button_link %}
                    <a href="{{ banner_button_link }}" class="btn btn-primary">{{ banner_button_text }}</a>
                {% endif %}
            </div>
        </div>
    </div>
</section>

{# 3. Estilos encapsulados #}
<style>
.section-custom-banner {
    padding: 80px 0;
    background-size: cover;
    background-position: center;
    color: var(--main-foreground);
    min-height: 400px;
    display: flex;
    align-items: center;
}
.banner-title {
    font-family: var(--heading-font);
    font-size: 2.5rem;
    margin-bottom: 20px;
}
.banner-description {
    font-size: 1.1rem;
    margin-bottom: 30px;
}
</style>
```

---

## ⚙️ Configuración (`config/settings.txt`)

Añade esto a tu archivo `settings.txt` bajo la sección correspondiente:

```text
custom_banner
    title = Banner Personalizado
    description = Configuración del banner principal.
    fields
        custom_banner_image
            type = image
            title = Imagen de fondo
            original = custom_banner_image.jpg
        custom_banner_title
            type = text
            title = Título del banner
        custom_banner_text
            type = textarea
            title = Texto descriptivo
        custom_banner_button_text
            type = text
            title = Texto del botón
        custom_banner_button_link
            type = text
            title = Enlace del botón
```

---

## 📝 Valores por defecto (`config/defaults.txt`)

```text
custom_banner_title = Colección de Verano 2024
custom_banner_text = Descubre las últimas tendencias en moda.
custom_banner_button_text = Ver Más
custom_banner_button_link = /productos
```
