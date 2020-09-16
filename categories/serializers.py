from rest_framework import serializers

from categories.models import Category


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id']


class CategorySerializer(serializers.ModelSerializer):
    # subcategories = serializers.ManyRelatedField()
    patent_category_name = serializers.CharField(read_only=True, source="parent_category.category_name")
    subcategories = SubCategorySerializer()

    class Meta:
        model = Category
        fields = ['id', 'category_name', 'parent_category', 'subcategories', 'parent_category_id', 'patent_category_name', 'url',
                  'created_at', 'updated_at']

    # def get_fields(self):
    #     fields = super(CategorySerializer, self).get_fields()
    #     fields['subcategories'] = CategorySerializer(many=True)
    #     return fields

        # def get_related_field(self, model_field):
        #     # Handles initializing the `subcategories` field
        #     return CategorySerializer()
# CategorySerializer.base_fields['subcategories'] = CategorySerializer()