1️⃣ Repo strukturasi
common_models/
├─ common_models/
│  ├─ __init__.py
│  ├─ models.py
│  └─ apps.py
├─ pyproject.toml
└─ README.md

2️⃣ apps.py
from django.apps import AppConfig

class CommonModelsConfig(AppConfig):
    name = 'common_models'

3️⃣ pyproject.toml
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

[project]
name = "common-models"
version = "0.1.0"
dependencies = ["Django>=3.2"]

4️⃣ GitHub’ga push qil
5️⃣ Django projectda o‘rnatish
pip install git+https://github.com/you/common_models.git

6️⃣ INSTALLED_APPS
INSTALLED_APPS = [
    ...
    'common_models',
]

7️⃣ Migratsiya
python manage.py makemigrations common_models
python manage.py migrate


✅ Natija:

Bitta models.py → ko‘p project

Git bilan versiya nazorati

Eng professional yechim

Xohlasang PyPI’ga chiqarish yoki versioning ham qilib beraman.
