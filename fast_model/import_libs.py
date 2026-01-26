from django.db import models
from django.contrib.auth.models import AbstractUser
import math
import decimal
import numpy as np
from django.db.models import Sum, Avg, Max, Min, StdDev, Variance
from django.db.models.functions import Round, Floor, Ceil, Abs, Power, Sqrt
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    company = models.ForeignKey('fast_model.Company', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        abstract = True
