from django.db import models
from django.contrib.auth.models import AbstractUser, User
import math
import decimal
import numpy as np
from django.db.models import Sum, Avg, Max, Min, StdDev, Variance
from django.db.models.functions import Round, Floor, Ceil, Abs, Power, Sqrt
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.core.exceptions import PermissionDenied
from django.db import transaction


__all__ = [
    'models', 'User', 'AbstractUser', 'math', 'decimal', 'np', 
    'Sum', 'Avg', 'Max', 'Min', 'StdDev', 'Variance',
    'Round', 'Floor', 'Ceil', 'Abs', 'Power', 'Sqrt',
    '_', 'timezone', 'BaseModel', 'admin', 'UserAdmin', 'PermissionDenied'
]

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    company = models.ForeignKey(
        'fast_model.Company', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        related_name="%(app_label)s_%(class)s_related"
    )

    class Meta:
        abstract = True
