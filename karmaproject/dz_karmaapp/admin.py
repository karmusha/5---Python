from django.contrib import admin
from.models import Category, Product, Client

@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)

class ProductAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['name', 'category', 'quantity']
    ordering = ['category', '-quantity']
    list_filter = ['date_insert', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_quantity]

    """Отдельный продукт."""
    # fields = ['name', 'description', 'category', 'date_insert']
    readonly_fields = ['date_insert', 'rating']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                'fields': ['category', 'description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity']
            }
        ),
        (
            'Рейтинг и прочее',
            {
                'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
                'fields': ['rating', 'date_insert'],
            }
        ),
    ]

class ClientAdmin(admin.ModelAdmin):
    """Список клиентов."""
    list_display = ['name', 'email', 'registration_date']
    ordering = ['name']
    list_filter = ['registration_date']
    search_fields = ['email']

    """Отдельный продукт."""
    readonly_fields = ['registration_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'email'],
            },
        ),
        (
            'Подробная инфомация',
            {
                'classes': ['collapse'],
                'description': 'Контактая информация',
                'fields': ['address', 'tel'],
            },
        ),
        (
            'Дата регистрации',
            {
                'description': 'Дата регистрации',
                'fields': ['registration_date'],
            }
        ),
    ]

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
