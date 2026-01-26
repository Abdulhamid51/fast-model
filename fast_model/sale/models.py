from fast_model.import_libs import * 

SHOPPING_TYPE_CHOICES = (
    ("buy", _("Buy")),
    ("sell", _("Sell")),
)

class ShoppingStatus(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    sequence = models.IntegerField(default=0)
    shopping_type = models.CharField(max_length=10, choices=SHOPPING_TYPE_CHOICES, default="buy")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Shopping Status")
        verbose_name_plural = _("Shopping Statuses")

class Shopping(BaseModel):
    """
    Shopping is to buy from deliver and to sell to customer
    """
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    shopping_type = models.CharField(max_length=10, choices=SHOPPING_TYPE_CHOICES, default="buy")
    status = models.ForeignKey('fast_model.ShoppingStatus', on_delete=models.CASCADE, blank=True, null=True)
    person = models.ForeignKey('fast_model.CustomUser', on_delete=models.CASCADE, related_name="shoppings_person")
    responsible_employee = models.ForeignKey('fast_model.CustomUser', on_delete=models.CASCADE, related_name="shoppings_responsible_employee")
    custom_date = models.DateTimeField(default=timezone.now)
    total_price = models.FloatField(default=0)

    def __str__(self):
        return f"{self.name} - {self.total_price}"

    class Meta:
        verbose_name = _("Shopping")
        verbose_name_plural = _("Shoppings")

class ShoppingItem(BaseModel):
    shopping = models.ForeignKey('fast_model.Shopping', on_delete=models.CASCADE, related_name="items", blank=True, null=True)
    product = models.ForeignKey('fast_model.Product', on_delete=models.CASCADE)
    batch_number = models.ForeignKey('fast_model.BatchNumber', on_delete=models.CASCADE, null=True, blank=True)
    amount = models.FloatField(default=0)
    price = models.FloatField(default=0)
    total_price = models.FloatField(default=0)
    barcode = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.product.base.name} - {self.amount}"

    class Meta:
        verbose_name = _("Shopping Item")
        verbose_name_plural = _("Shopping Items")