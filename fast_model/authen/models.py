from fast_model.import_libs import *

class Currency(BaseModel):
    """
    Only Developer can add currency!!!
    """
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10, unique=True)
    symbol = models.CharField(max_length=5)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _("Currency")
        verbose_name_plural = _("Currencies")

class Measure(BaseModel):
    """
    Only Developer can add measure!!!
    """
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Measure")
        verbose_name_plural = _("Measures")

class Company(BaseModel):
    """
    Only Developer can add company!!!
    """
    company = None 
    
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    available_currencies = models.ManyToManyField('fast_model.Currency', related_name='active_companies')
    available_measures = models.ManyToManyField('fast_model.Measure', related_name='active_companies')
    local_barcode_length = models.IntegerField(default=12)
    product_character1_name = models.CharField(max_length=300, default="Character 1")
    product_character2_name = models.CharField(max_length=300, default="Character 2")
    product_character3_name = models.CharField(max_length=300, default="Character 3")
    work_product_with_batch_number = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")

class CustomUser(BaseModel):
    """
    Profile model for standard Django User.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="custom")
    USER_TYPE_CHOICES = (
        ("super_admin", _("Super Admin")),
        ("admin", _("Admin")),
        ("customer", _("Customer")),
        ("deliver", _("Deliver")),
        ("partner", _("Partner")),
        ("lead", _("Lead")),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default="customer")
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    phone2 = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Custom User")
        verbose_name_plural = _("Custom Users")