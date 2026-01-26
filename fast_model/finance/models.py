from fast_model.import_libs import *

class BaseCash(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Base Cash")
        verbose_name_plural = _("Base Cashes")

class Cash(BaseModel):
    base = models.ForeignKey('fast_model.BaseCash', on_delete=models.CASCADE)
    start_amount = models.FloatField(default=0)
    amount = models.FloatField(default=0)
    currency = models.ForeignKey('fast_model.Currency', on_delete=models.CASCADE)

    def __str__(self):
        return self.base.name

    class Meta:
        verbose_name = _("Cash")
        verbose_name_plural = _("Cashes")

class PersonAccount(BaseModel):
    person = models.ForeignKey('fast_model.CustomUser', on_delete=models.CASCADE)
    start_amount = models.FloatField(default=0)
    amount = models.FloatField(default=0)
    currency = models.ForeignKey('fast_model.Currency', on_delete=models.CASCADE)

    def __str__(self):
        return self.person.username

    class Meta:
        verbose_name = _("Person Account")
        verbose_name_plural = _("Person Accounts")

class Conversion(BaseModel):
    from_currency = models.ForeignKey('fast_model.Currency', on_delete=models.CASCADE, related_name="from_currency")
    to_currency = models.ForeignKey('fast_model.Currency', on_delete=models.CASCADE, related_name="to_currency")
    currency_value = models.FloatField(default=0)
    custom_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.from_currency.name} >> {self.to_currency.name} = {self.currency_value}"

    class Meta:
        verbose_name = _("Conversion")
        verbose_name_plural = _("Conversions")
    

class Payment(BaseModel):
    custom_date = models.DateTimeField(default=timezone.now)
    cash = models.ForeignKey('fast_model.Cash', on_delete=models.CASCADE, blank=True, null=True)
    currency = models.ForeignKey('fast_model.Currency', on_delete=models.CASCADE)
    currency_value = models.FloatField(default=0)
    conversion = models.ForeignKey('fast_model.Conversion', on_delete=models.CASCADE, blank=True, null=True)
    cash_old = models.FloatField(default=0)
    cash_new = models.FloatField(default=0)
    shopping_paid = models.ForeignKey('fast_model.Shopping', on_delete=models.CASCADE, related_name="shopping_paid", blank=True, null=True)
    shopping_value = models.ForeignKey('fast_model.Shopping', on_delete=models.CASCADE, related_name="shopping_value", blank=True, null=True)
    person = models.ForeignKey('fast_model.CustomUser', on_delete=models.CASCADE, related_name="payments_person", blank=True, null=True)
    person_old = models.FloatField(default=0)
    person_new = models.FloatField(default=0)
    responsible_employee = models.ForeignKey('fast_model.CustomUser', on_delete=models.CASCADE, related_name="payments_responsible_employee", blank=True, null=True)
    PAYMENT_TYPE_CHOICES = (
        ("in", _("In")),
        ("out", _("Out")),
    )
    payment_type = models.CharField(max_length=10, choices=PAYMENT_TYPE_CHOICES, default="in")
    is_paid = models.BooleanField(default=False)
    deadline_date = models.DateTimeField(blank=True, null=True)
    amount = models.FloatField(default=0)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.person.username} - {self.amount} - {self.payment_type}"

    class Meta:
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")
    