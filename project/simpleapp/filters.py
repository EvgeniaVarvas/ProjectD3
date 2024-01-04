from django_filters import FilterSet, ModelChoiceFilter
from .models import Product, Category

class ProductFilter(FilterSet):
    category = ModelChoiceFilter(
        queryset=Category.objects.all(),
        field_name='category',
        to_field_name='name',
        label='Категория',
    )

    class Meta:
        model = Product
        fields = ['category']
    class Meta:
        model = Product
        fields = ['category__name']
# class ProductFilter(FilterSet):
#     category = ModelChoiceFilter(
#         field_name='category__name',
#         queryset=Product.objects.all(),
#         label='Категория',
#     )

#     class Meta:
#         model = Product
#         fields = {
#             # 'category__name': ['icontains'],
#             # другие поля фильтрации, но не включайте 'name__icontains' здесь, если не хотите его в форме
#         }
