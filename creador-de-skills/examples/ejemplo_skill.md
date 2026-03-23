# Ejemplo de Referencia: Skill en Español

A continuación se muestra una estructura ideal para una Skill definida en español.

```markdown
---
name: formateador-de-codigo
description: Usa esta habilidad cuando el usuario pida formatear o limpiar código fuente siguiendo los estándares de la industria.
---

# Skill: Formateador de Código

## Trigger

Esta habilidad se activara cuando el usuario pida formatear o limpiar código fuente siguiendo los estándares de la industria.

## Objetivo

Asegurar que el código del usuario sea legible, consistente y siga las mejores prácticas de estilo.

## Instrucciones

1. **Analizar el Lenguaje**: Identifica el lenguaje de programación del código proporcionado.
2. **Aplicar Reglas**: Usa las herramientas de formateo adecuadas (ej. Prettier, Black, ESLint).
3. **Reportar Cambios**: Explica brevemente qué mejoras de legibilidad se realizaron.

## Restricciones

- NUNCA cambies la lógica funcional del código, solo el formato.
- No elimines comentarios útiles.

## Ejemplos

### Ejemplo 1

**Usuario:** "Mi código JavaScript está todo desordenado, ¿puedes arreglarlo?"
**Agente:** Procede a aplicar sangrías (indentación) correctas y espaciado consistente usando la herramienta de formateo detectada.
```
