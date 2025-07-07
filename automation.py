import os

estructura = [
    "codespaces-mobile-plus/lib/core",
    "codespaces-mobile-plus/lib/features/auth",
    "codespaces-mobile-plus/lib/features/repos",
    "codespaces-mobile-plus/lib/features/codespace",
    "codespaces-mobile-plus/lib/features/shared",
    "codespaces-mobile-plus/lib/services",
    "codespaces-mobile-plus/docs",
    "codespaces-mobile-plus/docs/03-sprint-backlogs",
    "codespaces-mobile-plus/docs/04-ceremonias",
    "codespaces-mobile-plus/docs/05-registro-desarrollo",
    "codespaces-mobile-plus/docs/06-architecture"
]

archivos_base = {
    "codespaces-mobile-plus/.gitignore": "build/\n.dart_tool/\n.idea/\n*.iml\n",
    "codespaces-mobile-plus/pubspec.yaml": "name: codespaces_mobile_plus\ndescription: Flutter app to manage GitHub Codespaces from mobile.\nversion: 0.1.0\n",
    "codespaces-mobile-plus/README.md": "# Codespaces Mobile+\n\nApp Flutter para gestionar Codespaces desde un dispositivo móvil.\n",
    "codespaces-mobile-plus/docs/01-readme.md": "# Documentación del proyecto Codespaces Mobile+\n\nEstructura y documentación Scrum completa.",
    "codespaces-mobile-plus/docs/02-product-backlog.md": "# Product Backlog\n\n| ID | Historia de Usuario | Prioridad | Estado |\n|----|----------------------|-----------|--------|\n",
    "codespaces-mobile-plus/docs/03-sprint-backlogs/sprint-1-backlog.md": "# Sprint 1 Backlog\n\nHistorias seleccionadas y tareas del Sprint 1.",
    "codespaces-mobile-plus/docs/04-ceremonias/sprint-1-planning.md": "# Sprint 1 Planning\n\nObjetivo, historias y tareas desglosadas.",
    "codespaces-mobile-plus/docs/04-ceremonias/sprint-1-review.md": "# Sprint 1 Review\n\nResumen de lo entregado y feedback del PO.",
    "codespaces-mobile-plus/docs/04-ceremonias/sprint-1-retrospective.md": "# Sprint 1 Retrospective\n\nAnálisis de lo que salió bien y áreas de mejora.",
    "codespaces-mobile-plus/docs/05-registro-desarrollo/sprint-1.md": "# Registro de Desarrollo – Sprint 1\n\nBitácora del sprint con historias entregadas.",
    "codespaces-mobile-plus/docs/06-architecture/project-structure.md": "# Estructura del Proyecto Flutter\n\nÁrbol de carpetas y distribución lógica.",
    "codespaces-mobile-plus/docs/06-architecture/tech-stack.md": "# Stack Tecnológico\n\nFlutter, GitHub API, WebView, OAuth2, clipboard."
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

print("\n✅ Repositorio inicial generado con éxito.")