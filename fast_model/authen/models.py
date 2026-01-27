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
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    available_currencies = models.ManyToManyField('fast_model.Currency')
    available_measures = models.ManyToManyField('fast_model.Measure')
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
