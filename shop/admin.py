from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Category  # ← ТОЧКИ!


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'get_preview', 'price', 'category_id']
    readonly_fields = ['get_preview']
    fieldsets = (
        ('Основное', {'fields': ('name', 'slug', 'category_id')}),
        ('Изображение', {'fields': ('image', 'get_preview')}),
        ('Цена/Количество', {'fields': ('price', 'stock')}),
    )


@admin.register(Category)  # ← УБЕРИ admin.site.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_preview', 'is_active', 'created_at']

    readonly_fields = ['get_preview']  # ← КЛЮЧЕВОЕ!
    fieldsets = (  # ← ОРГАНИЗУЕТ ПО БЛОКАМ
        ('Основное', {
            'fields': ('name', 'slug', 'is_active')
        }),
        ('Изображение', {  # ← НОВЫЙ БЛОК!
            'fields': ('image', 'get_preview')  # ← Превью ПОД изображением!
        }),
        ('Описание', {
            'fields': ('description',)
        }),
    )
