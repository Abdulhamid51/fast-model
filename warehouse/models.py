from fast_model.import_libs import *
    
class ProductCategory(BaseModel):
    """
    Product category model
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Product Category")
        verbose_name_plural = _("Product Categories")
    
class BaseProduct(BaseModel):
    """
    Base product model
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    barcode = models.CharField(max_length=100, unique=True, blank=True, null=True)
    category = models.ForeignKey('fast_model.ProductCategory', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Base Product")
        verbose_name_plural = _("Base Products")

class Warehouse(BaseModel):
    """
    Warehouse model
    """
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    can_use_users = models.ManyToManyField('fast_model.CustomUser', related_name="warehouses", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Warehouse")
        verbose_name_plural = _("Warehouses")

class ProductLocation(BaseModel):
    """
    Product location model
    """
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    warehouse = models.ForeignKey('fast_model.Warehouse', on_delete=models.CASCADE)
    barcode = models.CharField(max_length=100, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Product Location")
        verbose_name_plural = _("Product Locations")

class ProductCharacter1(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Character1")
        verbose_name_plural = _("Character1s")

class ProductCharacter2(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Character2")
        verbose_name_plural = _("Character2s")

class ProductCharacter3(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Character3")
        verbose_name_plural = _("Character3s")

class Product(BaseModel):
    """
    Product model
    """
    base = models.ForeignKey('fast_model.BaseProduct', on_delete=models.CASCADE, related_name="products")
    measure = models.ForeignKey('fast_model.Measure', on_delete=models.CASCADE, null=True, blank=True)
    amount = models.FloatField(default=0)
    warehouse = models.ForeignKey('fast_model.Warehouse', on_delete=models.CASCADE)
    location = models.ForeignKey('fast_model.ProductLocation', on_delete=models.CASCADE, null=True, blank=True)
    character1 = models.ForeignKey('fast_model.ProductCharacter1', on_delete=models.CASCADE, null=True, blank=True)
    character2 = models.ForeignKey('fast_model.ProductCharacter2', on_delete=models.CASCADE, null=True, blank=True)
    character3 = models.ForeignKey('fast_model.ProductCharacter3', on_delete=models.CASCADE, null=True, blank=True)
    start_amount = models.FloatField(default=0)

    def __str__(self):
        return f"{self.base.name} - {self.amount}"

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

class BatchNumber(BaseModel):
    """
    When company works with batch number, this model is used
    """
    product = models.ForeignKey('fast_model.Product', on_delete=models.CASCADE)
    location = models.ForeignKey('fast_model.ProductLocation', on_delete=models.CASCADE, null=True, blank=True)
    number = models.CharField(max_length=100)
    amount = models.FloatField(default=0)
    year = models.IntegerField(default=0)
    start_amount = models.FloatField(default=0)

    def __str__(self):
        return f"{self.product.base.name} - {self.number}"

    class Meta:
        verbose_name = _("Batch Number")
        verbose_name_plural = _("Batch Numbers")

class ProductHistory(BaseModel):
    """
    All in and out of product is recorded here
    """
    product = models.ForeignKey('fast_model.Product', on_delete=models.CASCADE)
    batch_number = models.ForeignKey('fast_model.BatchNumber', on_delete=models.CASCADE, null=True, blank=True)
    warehouse = models.ForeignKey('fast_model.Warehouse', on_delete=models.CASCADE, null=True, blank=True)
    shopping_item = models.ForeignKey('fast_model.ShoppingItem', on_delete=models.CASCADE, null=True, blank=True)
    amount = models.FloatField(default=0)
    amount_old = models.FloatField(default=0)
    amount_new = models.FloatField(default=0)
    amount_batch_old = models.FloatField(default=0)
    amount_batch_new = models.FloatField(default=0)
    HISTORY_TYPE_CHOICES = (
        ("in", _("In")),
        ("out", _("Out")),
    )
    history_type = models.CharField(max_length=10, choices=HISTORY_TYPE_CHOICES, default="in")
    ACTION_TYPE_CHOICES = (
        ("shopping", _("Shopping")),
        ("transfer", _("Transfer")),
        ("adjustment", _("Adjustment")),
    )
    action_type = models.CharField(max_length=10, choices=ACTION_TYPE_CHOICES, default="shopping")
    
    def __str__(self):
        return f"{self.product.base.name} - {self.amount}"

    class Meta:
        verbose_name = _("Product History")
        verbose_name_plural = _("Product Histories")
