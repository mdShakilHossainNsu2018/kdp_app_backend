from rest_framework import serializers

from categories.models import Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    # subcategories = serializers.ManyRelatedField()
    patent_category_name = serializers.CharField(read_only=True, source="parent_category.category_name")

    class Meta:
        model = Category
        fields = ['id', 'category_name', 'parent_category', 'parent_category_id', 'patent_category_name', 'url', 'created_at', 'updated_at']
