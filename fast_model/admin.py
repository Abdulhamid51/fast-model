from fast_model.import_libs import *
from fast_model.models import *

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

class CustomUserInline(admin.StackedInline):
    model = CustomUser
    can_delete = False
    verbose_name_plural = 'Custom User Info'

# Standart UserAdmin ni kengaytirish
class MyUserAdmin(UserAdmin):
    inlines = (CustomUserInline,)
    list_display = UserAdmin.list_display + ('get_user_type', 'get_company')
    
    def get_user_type(self, obj):
        return obj.custom.user_type if hasattr(obj, 'custom') else '-'
    get_user_type.short_description = 'User Type'

    def get_company(self, obj):
        return obj.custom.company if hasattr(obj, 'custom') else '-'
    get_company.short_description = 'Company'

# CustomUser ni alohida ham ko'rish imkoniyati
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'user_type', 'company', 'is_active')
    list_filter = ('user_type', 'company', 'is_active')
    search_fields = ('user__username', 'user__email')

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'

# Standart UserAdmin ni qayta ro'yxatdan o'tkazish (agar kerak bo'lsa asosiy loyihada qilinadi)
# admin.site.unregister(User)
# admin.site.register(User, MyUserAdmin)

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
