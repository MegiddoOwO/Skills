---
name: creador-de-skills
description: Usa esta habilidad cuando el usuario quiera crear una nueva "Skill" (habilidad) en el workspace, especialmente si desea que las instrucciones y la estructura estén en español.
---
# Creador de Skills (Habilidades)

Esta habilidad automatiza la creación de nuevas capacidades para el agente dentro del entorno de Antigravity, asegurando que sigan las mejores prácticas y estén localizadas al español.

## Objetivo
Asistir en el diseño, estructuración y creación física de nuevas Skills en el workspace.

## Instrucciones
1. **Identificar la Intención**: Pregunta al usuario el nombre de la nueva Skill y su propósito principal si no lo ha proporcionado.
2. **Diseñar el Metadato**: Genera un nombre (minúsculas y guiones) y una descripción detallada en español que sirva como "frase de activación".
3. **Ejecutar el Scaffolder**: Una vez confirmado el nombre, ejecuta el script de creación:
   `python .agent/skills/creador-de-skills/scripts/crear_skill.py <nombre-de-la-skill>`
4. **Redactar el Cuerpo**: Completa el archivo `SKILL.md` recién creado siguiendo el patrón: Objetivo, Instrucciones, Restricciones y Ejemplos, todo en español.
5. **Referencia**: Consulta `examples/ejemplo_skill.md` para ver un modelo de alta calidad.

## Restricciones
- Todas las Skills generadas deben ubicarse en `.agent/skills/`.
- Las descripciones deben ser ricas en palabras clave para facilitar la detección por el LLM.
- El idioma principal de las instrucciones generadas debe ser el español.

## Ejemplos
### Ejemplo 1
**Usuario:** "Crea una skill para manejar inventarios de Shopify"
**Agente:** 
1. Propone el nombre `gestor-inventario-shopify`.
2. Ejecuta `python .agent/skills/creador-de-skills/scripts/crear_skill.py gestor-inventario-shopify`.
3. Procede a redactar las instrucciones detalladas en el nuevo `SKILL.md`.
