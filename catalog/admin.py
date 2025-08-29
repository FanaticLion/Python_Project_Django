from django.contrib import admin
from .models import Category, Product,Contact

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    list_filter = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'created_at')
    list_display_links = ('id', 'name')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description', 'category__name')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'category', 'price')
        }),
        ('Изображение', {
            'fields': ('image',),
            'classes': ('collapse',)
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
        list_display = ('name', 'email', 'phone', 'created_at')
        list_filter = ('created_at',)
        search_fields = ('name', 'email', 'phone')
        readonly_fields = ('created_at',)
        list_display_links = ('name', 'email')