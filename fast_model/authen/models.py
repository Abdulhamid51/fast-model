from fast_model.import_libs import *

class Currency(BaseModel):
    """
    Only Developer can add currency!!!
    """
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10, unique=True)
    symbol = models.CharField(max_length=5)
    is_base = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_base:
            Currency.objects.filter(is_base=True).update(is_base=False)
        super().save(*args, **kwargs)

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
    impact_sources = models.ManyToManyField('fast_model.PaymentSource', related_name='active_companies')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")

class PermissionGroup(BaseModel):
    """
    actions: can_add_, can_edit_, can_delete_
    model: exm ModelName = model_name
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    # --- Authen ---
    can_add_permission_group = models.BooleanField(default=False)
    can_edit_permission_group = models.BooleanField(default=False)
    can_delete_permission_group = models.BooleanField(default=False)

    can_add_custom_user = models.BooleanField(default=False)
    can_edit_custom_user = models.BooleanField(default=False)
    can_delete_custom_user = models.BooleanField(default=False)

    # --- Warehouse ---
    can_add_product_category = models.BooleanField(default=False)
    can_edit_product_category = models.BooleanField(default=False)
    can_delete_product_category = models.BooleanField(default=False)

    can_add_base_product = models.BooleanField(default=False)
    can_edit_base_product = models.BooleanField(default=False)
    can_delete_base_product = models.BooleanField(default=False)

    can_add_warehouse = models.BooleanField(default=False)
    can_edit_warehouse = models.BooleanField(default=False)
    can_delete_warehouse = models.BooleanField(default=False)

    can_add_product_location = models.BooleanField(default=False)
    can_edit_product_location = models.BooleanField(default=False)
    can_delete_product_location = models.BooleanField(default=False)

    can_add_product = models.BooleanField(default=False)
    can_edit_product = models.BooleanField(default=False)
    can_delete_product = models.BooleanField(default=False)

    can_add_batch_number = models.BooleanField(default=False)
    can_edit_batch_number = models.BooleanField(default=False)
    can_delete_batch_number = models.BooleanField(default=False)

    can_add_product_history = models.BooleanField(default=False)
    can_edit_product_history = models.BooleanField(default=False)
    can_delete_product_history = models.BooleanField(default=False)

    can_add_product_character1 = models.BooleanField(default=False)
    can_edit_product_character1 = models.BooleanField(default=False)
    can_delete_product_character1 = models.BooleanField(default=False)

    can_add_product_character2 = models.BooleanField(default=False)
    can_edit_product_character2 = models.BooleanField(default=False)
    can_delete_product_character2 = models.BooleanField(default=False)

    can_add_product_character3 = models.BooleanField(default=False)
    can_edit_product_character3 = models.BooleanField(default=False)
    can_delete_product_character3 = models.BooleanField(default=False)

    # --- Finance ---
    can_add_base_cash = models.BooleanField(default=False)
    can_edit_base_cash = models.BooleanField(default=False)
    can_delete_base_cash = models.BooleanField(default=False)

    can_add_cash = models.BooleanField(default=False)
    can_edit_cash = models.BooleanField(default=False)
    can_delete_cash = models.BooleanField(default=False)

    can_add_person_account = models.BooleanField(default=False)
    can_edit_person_account = models.BooleanField(default=False)
    can_delete_person_account = models.BooleanField(default=False)

    can_add_conversion = models.BooleanField(default=False)
    can_edit_conversion = models.BooleanField(default=False)
    can_delete_conversion = models.BooleanField(default=False)

    can_add_payment = models.BooleanField(default=False)
    can_edit_payment = models.BooleanField(default=False)
    can_delete_payment = models.BooleanField(default=False)

    # --- Sale ---
    can_add_shopping_status = models.BooleanField(default=False)
    can_edit_shopping_status = models.BooleanField(default=False)
    can_delete_shopping_status = models.BooleanField(default=False)

    can_add_shopping = models.BooleanField(default=False)
    can_edit_shopping = models.BooleanField(default=False)
    can_delete_shopping = models.BooleanField(default=False)

    can_add_shopping_item = models.BooleanField(default=False)
    can_edit_shopping_item = models.BooleanField(default=False)
    can_delete_shopping_item = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Permission Group")
        verbose_name_plural = _("Permission Groups")

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
    permission_group = models.ForeignKey(PermissionGroup, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Custom User")
        verbose_name_plural = _("Custom Users")