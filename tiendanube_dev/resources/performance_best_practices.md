# ⚡ Mejores Prácticas de Rendimiento (Web Vitals)

Para que una tienda Scatola sea rápida y tenga buen puntaje en Google PageSpeed, sigue estas reglas de oro.

## 1. Lazy Loading de Imágenes

Nunca cargues todas las imágenes de golpe. Usa la clase `lazyload` y el atributo `data-src`.

```twig
<img
    src="{{ 'images/empty-placeholder.png' | static_url }}"
    data-src="{{ slide.image | static_url | settings_image_url('large') }}"
    class="lazyload"
    alt="{{ slide.title }}"
>
```

_Nota: El `src` inicial debe ser un placeholder ligero o un SVG transparente._

---

## 2. Filtro `settings_image_url`

No cargues la imagen original si solo vas a mostrar un thumbnail. Usa tamaños específicos:

- `tiny` (50px)
- `thumb` (100px)
- `small` (240px)
- `medium` (480px)
- `large` (1024px)
- `huge` (2048px)
- `original`

---

## 3. Scripts no bloqueantes

En la tienda Scatola, es preferible usar `DOMContentLoaded.addEventOrExecute` para asegurar que el DOM esté listo sin bloquear el renderizado inicial.

```twig
<script>
    DOMContentLoaded.addEventOrExecute(() => {
        // Tu lógica aquí (ej: Swiper)
    });
</script>
```

---

## 4. Evitar el Reflow (Layout Shift)

Siempre define una relación de aspecto (`aspect-ratio`) o dimensiones fijas en CSS para los contenedores de imágenes, evitando que el contenido "salte" cuando la imagen carga.

```css
.mi-contenedor-imagen {
  aspect-ratio: 16 / 9;
  background-color: #f0f0f0;
}
```
