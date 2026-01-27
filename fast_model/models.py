from fast_model.authen.models import *
from fast_model.warehouse.models import *
from fast_model.finance.models import *
from fast_model.sale.models import *

class CustomUser(AbstractUser):
    """
    When you want to use user, you should use this model.
    User types:
    super_admin, admin, customer, deliver, partner
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    company = models.ForeignKey('fast_model.Company', on_delete=models.CASCADE, null=True, blank=True)
    USER_TYPE_CHOICES = (
        ("super_admin", _("Super Admin")),
        ("admin", _("Admin")),
        ("customer", _("Customer")),
        ("deliver", _("Deliver")),
        ("partner", _("Partner")),
        ("lead", _("Lead")),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default="customer")
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    phone2 = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
