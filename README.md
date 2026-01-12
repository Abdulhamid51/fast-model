# fast_model

A reusable Django app for sharing database models across multiple projects.

## Overview

fast_model is a standalone Django application designed to keep common database models in a single repository and reuse them across multiple Django projects using pip and Git.

## Project Structure

```
fast_model/
├── fast_model/
│   ├── __init__.py
│   ├── models.py
│   └── apps.py
├── pyproject.toml
└── README.md
```
## Installation

Public repository:
```
pip install git+https://github.com/your-username/fast_model.git
```
Private repository (SSH):
```
pip install git+ssh://git@github.com/your-username/fast_model.git
```
Install a specific version:
```
pip install git+https://github.com/your-username/fast_model.git@v1.0.0
```
## Django Configuration

Add the app to INSTALLED_APPS:
```
INSTALLED_APPS = [
    ...
    'fast_model',
]
```
## AppConfig

fast_model/apps.py:
```
from django.apps import AppConfig

class FastModelConfig(AppConfig):
    name = 'fast_model'
```
## Defining Models

All shared models must be defined in fast_model/models.py

Example:
```
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```
## Using Models

Import models in any Django project:
```
from fast_model.models import Product
```
## Database Migrations

Migrations must be created and applied inside each Django project:
```
python manage.py makemigrations fast_model
python manage.py migrate
```
## Updating

Update the package:
```
pip install --upgrade git+https://github.com/your-username/fast_model.git
```
## Versioning

Create a version tag:
```
git tag v1.0.0
git push origin v1.0.0
```
Install a specific version:
```
pip install git+https://github.com/your-username/fast_model.git@v1.0.0
```
## Notes

- Do not run migrations inside the fast_model repository
- Always manage migrations from the main Django project
- __init__.py is required
- Django versions should be compatible across projects

## License

MIT License
