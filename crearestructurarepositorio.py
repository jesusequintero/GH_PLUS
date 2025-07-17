import os

estructura = [
    "lib/core",
    "lib/features/auth",
    "lib/features/repos",
    "lib/features/codespace",
    "lib/features/shared",
    "lib/services",
    "docs",
    "docs/03-sprint-backlogs",
    "docs/04-ceremonias",
    "docs/05-registro-desarrollo",
    "docs/06-architecture"
]

archivos_base = {
    ".gitignore": "build/\n.dart_tool/\n.idea/\n*.iml\n",
    "pubspec.yaml": "name: gh_plus\ndescription: Flutter app to manage GitHub Codespaces from mobile.\nversion: 0.1.0\n",
    "README.md": "# GH_PLUS\n\nApp Flutter para gestionar Codespaces desde un dispositivo móvil.\n",
    "docs/01-readme.md": "# Documentación del proyecto GH_PLUS\n\nEstructura y documentación Scrum completa.",
    "docs/02-product-backlog.md": "# Product Backlog\n\n| ID | Historia de Usuario | Prioridad | Estado |\n|----|----------------------|-----------|--------|\n",
    "docs/03-sprint-backlogs/sprint-1-backlog.md": "# Sprint 1 Backlog\n\nHistorias seleccionadas y tareas del Sprint 1.",
    "docs/04-ceremonias/sprint-1-planning.md": "# Sprint 1 Planning\n\nObjetivo, historias y tareas desglosadas.",
    "docs/04-ceremonias/sprint-1-review.md": "# Sprint 1 Review\n\nResumen de lo entregado y feedback del PO.",
    "docs/04-ceremonias/sprint-1-retrospective.md": "# Sprint 1 Retrospective\n\nAnálisis de lo que salió bien y áreas de mejora.",
    "docs/05-registro-desarrollo/sprint-1.md": "# Registro de Desarrollo – Sprint 1\n\nBitácora del sprint con historias entregadas.",
    "docs/06-architecture/project-structure.md": "# Estructura del Proyecto Flutter\n\nÁrbol de carpetas y distribución lógica.",
    "docs/06-architecture/tech-stack.md": "# Stack Tecnológico\n\nFlutter, GitHub API, WebView, OAuth2, clipboard."
}

# Crear carpetas
for carpeta in estructura:
    os.makedirs(carpeta, exist_ok=True)
    print(f"✔️ Carpeta creada: {carpeta}")

# Crear archivos base
for ruta, contenido in archivos_base.items():
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(contenido)
        print(f"📄 Archivo creado: {ruta}")

print("\n✅ Repositorio GH_PLUS generado con éxito.")
