"""Копирует собранный сайт из site/_site в docs/ (оттуда его публикует GitHub Pages).

Запускается Quarto автоматически после каждой сборки (post-render в _quarto.yml).
Quarto не поддерживает output-dir за пределами проекта, поэтому сайт собирается
в стандартную папку _site и затем переносится.
"""

import os
import shutil
from pathlib import Path

# Полную пересборку отличаем от предпросмотра отдельной страницы
if os.environ.get("QUARTO_PROJECT_RENDER_ALL") != "1":
    raise SystemExit(0)

site_dir = Path(__file__).resolve().parent
built = site_dir / "_site"
docs = site_dir.parent / "docs"

# docs/ целиком заменяется свежей сборкой
if docs.exists():
    shutil.rmtree(docs)
shutil.copytree(built, docs)

# Без этого файла GitHub Pages обрабатывает сайт Jekyll'ом
(docs / ".nojekyll").touch()

print(f"Сайт скопирован в {docs}")
