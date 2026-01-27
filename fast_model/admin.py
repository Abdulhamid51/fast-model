from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from fast_model.authen.models import Currency, Measure, Company, CustomUser
from fast_model.warehouse.models import (
    ProductCategory, BaseProduct, Warehouse, ProductLocation, 
    ProductCharacter1, ProductCharacter2, ProductCharacter3, 
    Product, BatchNumber, ProductHistory
)
from fast_model.finance.models import BaseCash, Cash, PersonAccount, Conversion, Payment
from fast_model.sale.models import ShoppingStatus, Shopping, ShoppingItem

# --- Authen ---
@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'symbol', 'is_active', 'company')
    list_filter = ('is_active', 'company')
    search_fields = ('code', 'name')

@admin.register(Measure)
class MeasureAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'is_active', 'company')
    list_filter = ('is_active', 'company')
    search_fields = ('name', 'symbol')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'local_barcode_length', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'user_type', 'company', 'is_staff', 'is_active')
    list_filter = ('user_type', 'company', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        (_('Custom Fields'), {'fields': ('user_type', 'company')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (_('Custom Fields'), {'fields': ('user_type', 'company')}),
    )

# --- Warehouse ---
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'is_active')
    list_filter = ('company', 'is_active')
    search_fields = ('name',)

@admin.register(BaseProduct)
class BaseProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'barcode', 'category', 'company', 'is_active')
    list_filter = ('category', 'company', 'is_active')
    search_fields = ('name', 'barcode')

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'is_active')
    list_filter = ('company', 'is_active')
    search_fields = ('name',)

@admin.register(ProductLocation)
class ProductLocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'warehouse', 'barcode', 'company', 'is_active')
    list_filter = ('warehouse', 'company', 'is_active')
    search_fields = ('name', 'barcode')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('base', 'amount', 'warehouse', 'location', 'company', 'is_active')
    list_filter = ('warehouse', 'location', 'company', 'is_active')
    search_fields = ('base__name',)

@admin.register(BatchNumber)
class BatchNumberAdmin(admin.ModelAdmin):
    list_display = ('product', 'number', 'amount', 'year', 'company')
    list_filter = ('year', 'company')
    search_fields = ('number', 'product__base__name')

@admin.register(ProductHistory)
class ProductHistoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'amount', 'history_type', 'action_type', 'created_at')
    list_filter = ('history_type', 'action_type', 'company')
    readonly_fields = ('created_at', 'updated_at')

# --- Finance ---
@admin.register(BaseCash)
class BaseCashAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'is_active')
    search_fields = ('name',)

@admin.register(Cash)
class CashAdmin(admin.ModelAdmin):
    list_display = ('base', 'amount', 'currency', 'company')
    list_filter = ('currency', 'company')

@admin.register(PersonAccount)
class PersonAccountAdmin(admin.ModelAdmin):
    list_display = ('person', 'amount', 'currency', 'company')
    list_filter = ('currency', 'company')

@admin.register(Conversion)
class ConversionAdmin(admin.ModelAdmin):
    list_display = ('from_currency', 'to_currency', 'currency_value', 'custom_date')
    list_filter = ('from_currency', 'to_currency')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('person', 'amount', 'payment_type', 'is_paid', 'custom_date', 'company')
    list_filter = ('payment_type', 'is_paid', 'company')
    search_fields = ('person__username', 'description')

# --- Sale ---
@admin.register(ShoppingStatus)
class ShoppingStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'shopping_type', 'sequence', 'company')
    list_filter = ('shopping_type', 'company')

class ShoppingItemInline(admin.TabularInline):
    model = ShoppingItem
    extra = 1

@admin.register(Shopping)
class ShoppingAdmin(admin.ModelAdmin):
    list_display = ('name', 'shopping_type', 'status', 'person', 'total_price', 'custom_date')
    list_filter = ('shopping_type', 'status', 'company')
    inlines = [ShoppingItemInline]

@admin.register(ShoppingItem)
class ShoppingItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'shopping', 'amount', 'price', 'total_price')
    list_filter = ('shopping__shopping_type', 'company')

# Character models (minimal admin)
admin.site.register(ProductCharacter1)
admin.site.register(ProductCharacter2)
admin.site.register(ProductCharacter3)
