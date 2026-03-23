import os
import sys

def create_skill(skill_name):
    base_path = f".agent/skills/{skill_name}"
    
    # Create directories
    directories = [
        base_path,
        f"{base_path}/scripts",
        f"{base_path}/examples",
        f"{base_path}/references"
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Directorio creado: {directory}")
        else:
            print(f"El directorio ya existe: {directory}")

    # Create basic SKILL.md template in Spanish
    skill_md_content = f"""---
name: {skill_name}
description: Describe aquí para qué sirve esta habilidad de forma detallada para que el agente sepa cuándo activarla.
---
# Skill: {skill_name}

## Objetivo
Define claramente qué logra esta habilidad.

## Instrucciones
1. Paso uno...
2. Paso dos...

## Restricciones
- No hacer esto...
- Siempre hacer aquello...

## Ejemplos
### Ejemplo 1
**Usuario:** Consulta de ejemplo
**Agente:** Acción de ejemplo
"""
    
    skill_md_path = f"{base_path}/SKILL.md"
    if not os.path.exists(skill_md_path):
        with open(skill_md_path, "w", encoding="utf-8") as f:
            f.write(skill_md_content)
        print(f"Archivo creado: {skill_md_path}")
    else:
        print(f"El archivo ya existe: {skill_md_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python crear_skill.py <nombre-de-la-skill>")
        sys.exit(1)
    
    create_skill(sys.argv[1])
