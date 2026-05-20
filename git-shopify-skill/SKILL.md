---
name: git-shopify-commits
description: >
  Skill personalizada para gestionar commits de Git en proyectos Shopify. Úsala siempre que el
  usuario mencione: hacer un commit, Realizar commits de los cambios realizados, git commit, subir cambios, guardar cambios en git, crear un
  branch, nombrar una rama, push, staging, o cuando pregunte cómo describir lo que modificó en
  su proyecto Shopify. También activa esta skill si el usuario comparte una lista de archivos
  modificados (.liquid, .js, .css, .json) y quiere saber cómo commitearlos. Genera mensajes de
  commit claros en español, valida el branch actual, sugiere el tipo correcto (feat/fix/chore/
  style/refactor/docs) según el contexto Shopify, y ayuda con el naming de feature branches.
---

# Git Commits — Proyectos Shopify

Skill personalizada para generar, validar y estructurar commits de Git en proyectos de desarrollo
Shopify (temas, apps, customizaciones). Todo en **español**, con formato propio del usuario.

---

## Formato de Commit

```
tipo(archivo_o_accion): Descripción clara y concisa en español
```

**Ejemplos reales:**

```
feat(product-card.liquid): Agregar botón de lista de deseos en tarjeta de producto
fix(cart-drawer.js): Corregir cálculo de descuentos en carrito deslizable
chore(settings_schema.json): Actualizar opciones de color del tema
style(header.liquid): Ajustar espaciado y tipografía en navegación principal
refactor(collection.liquid): Simplificar lógica de filtros de colección
docs(README.md): Documentar proceso de instalación del tema
```

### Reglas del formato

- El `tipo` siempre en **minúsculas**
- El `archivo_o_accion` entre paréntesis: puede ser el nombre del archivo modificado o una
  acción descriptiva (ej: `cart-logic`, `product-schema`, `theme-config`)
- La descripción **comienza con mayúscula**, en **español**, **modo imperativo**
  (ej: "Agregar", "Corregir", "Actualizar" — no "Agregado" ni "Se agregó")
- Máximo ~72 caracteres en la primera línea
- Sin punto final

---

## Tipos de Commit y cuándo usarlos

| Tipo       | Cuándo usarlo en Shopify                                                     |
| ---------- | ---------------------------------------------------------------------------- |
| `feat`     | Nueva funcionalidad visible: sección nueva, componente, integración de app   |
| `fix`      | Corrección de bug: algo que estaba roto o no funcionaba como esperado        |
| `chore`    | Tareas de mantenimiento: configuraciones, dependencias, metafields, esquemas |
| `style`    | Cambios visuales puros: CSS, tipografía, colores, espaciado (sin lógica)     |
| `refactor` | Mejora de código sin cambiar funcionalidad: limpiar, reorganizar, optimizar  |
| `docs`     | Documentación: README, comentarios en código, guías internas                 |

### Mapeo por tipo de archivo Shopify

| Archivo modificado                | Tipo sugerido por defecto |
| --------------------------------- | ------------------------- |
| `*.liquid` (nueva sección/bloque) | `feat`                    |
| `*.liquid` (corrección de lógica) | `fix`                     |
| `*.liquid` (solo maquetación)     | `style`                   |
| `*.js` (nueva funcionalidad)      | `feat`                    |
| `*.js` (corrección)               | `fix`                     |
| `*.css / *.scss`                  | `style`                   |
| `settings_schema.json`            | `chore`                   |
| `*.json` (metafields/config)      | `chore`                   |
| `locales/*.json`                  | `chore`                   |
| `README.md` / documentación       | `docs`                    |

---

## Flujo de Trabajo Completo

### Paso 1 — Validar el branch antes de commitear

**Siempre verificar** en qué branch está el usuario antes de proceder.

**Reglas de branches:**

- ✅ `main` — Solo recibe merges desde feature branches. **NUNCA commitear directamente** a main
  (salvo hotfixes urgentes, ver abajo)
- ✅ `feature/nombre-descriptivo` — Branch de trabajo normal
- ⚠️ Si el usuario está en `main` y quiere commitear trabajo nuevo → **alertar** y sugerir crear
  un feature branch primero

**Si detectas que está en `main`**, mostrar este aviso:

```
⚠️  Estás en el branch `main`.
    Se recomienda no commitear trabajo nuevo directamente aquí.
    ¿Quieres que te ayude a crear un feature branch primero?
```

### Paso 2 — Naming de Feature Branches

Formato: `feature/descripcion-corta-en-kebab-case`

**Reglas:**

- Todo en **minúsculas**
- Palabras separadas por guiones `-`
- Descriptivo pero corto (3-5 palabras máximo)
- Sin caracteres especiales ni acentos

**Ejemplos:**

```
feature/cart-drawer-redesign
feature/product-recommendations
feature/mega-menu-mobile
feature/checkout-custom-fields
feature/filtros-coleccion
```

**Comando sugerido:**

```bash
git checkout -b feature/nombre-de-tu-feature
```

### Paso 3 — Sincronizar y revisar archivos

**OBLIGATORIO:** Antes de cualquier commit o revisión, realizar un pull inicial para evitar conflictos.

```bash
git pull origin <nombre-del-branch>
```

Luego, pedir al usuario que comparta `git status` o lista de archivos modificados...

Pedir al usuario que comparta `git status` o lista de archivos modificados si no los ha
mencionado. Esto permite sugerir el tipo correcto y el scope del commit.

### Paso 4 — Generar el mensaje de commit

Con base en los archivos y el contexto, generar **1 mensaje principal** y opcionalmente
**2 alternativas** si hay ambigüedad.

**Formato de presentación al usuario:**

```
✅ Commit sugerido:
   feat(product-card.liquid): Agregar sección de reviews en página de producto

📋 Alternativas:
   feat(reviews-section): Integrar bloque de reseñas en template de producto
   feat(product.liquid): Implementar visualización de valoraciones de clientes

📌 Comando listo para copiar:
   git add . && git commit -m "feat(product-card.liquid): Agregar sección de reviews en página de producto"
```

### Paso 5 — Commits con múltiples archivos

Si los archivos modificados tocan **áreas distintas**, recomendar dividir en commits separados:

```
💡 Tienes cambios en áreas diferentes. Considera hacer commits separados:

   1. git add product-card.liquid && git commit -m "feat(product-card.liquid): ..."
   2. git add cart.js && git commit -m "fix(cart.js): ..."
```

---

## Casos Especiales

### Hotfix en main

Si hay un bug crítico que requiere fix directo en main:

```
fix(archivo): Corregir [problema crítico] — hotfix
```

Y recordar hacer el merge/cherry-pick a los feature branches activos.

### WIP (Work in Progress)

Para commits de respaldo/avance sin terminar:

```
chore(wip): Avance en implementación de [feature] — pendiente revisión
```

### Primer commit de un proyecto/tema

```
chore(init): Configuración inicial del tema Shopify
```

---

## Checklist Pre-Commit

Antes de generar el commit, verificar mentalmente:

- [ ] ¿El usuario está en un feature branch (no en main)?
- [ ] ¿Se realizó el pull inicial para evitar conflictos?
- [ ] ¿Se sabe qué archivos se modificaron?
- [ ] ¿El tipo de commit refleja correctamente la naturaleza del cambio?
- [ ] ¿La descripción está en español, modo imperativo, clara y concisa?
- [ ] ¿El scope (archivo_o_accion) identifica bien el área modificada?
- [ ] ¿Hay cambios en múltiples áreas que convenga separar?

---

## Referencia Rápida

Para contexto adicional sobre estructura de archivos Shopify y ejemplos extendidos,
ver: `references/shopify-files-guide.md`
