from django.contrib import admin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget

from .models import Category
from import_export.admin import ImportExportModelAdmin




class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'parent_category', 'created_at',)
    list_filter = ('created_at', 'category_name',)
    search_fields = ('category_name',)

class CategoryResource(resources.ModelResource):
    # parent_category = fields.Field()
    # print(parent_category)

    class Meta:
        model = Category

    # def dehydrate_parent_category(self, category):
    #     return category.parent_category

# Register your models here.
# @admin.register(Category)
class ImportView(ImportExportModelAdmin):
    # list_display = ('name', 'school_id')
    resources_class = CategoryResource

admin.site.register(Category, ImportView)

