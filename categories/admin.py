from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'parent_category', 'created_at',)
    list_filter = ('created_at', 'category_name',)
    search_fields = ('category_name',)


# Register your models here.
admin.site.register(Category, CategoryAdmin)
