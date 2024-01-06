from django import forms
from .models import Product
from django.core.exceptions import ValidationError

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
           'name',
           'description',
           'quantity',
           'category',
           'price',
       ]
    
    #Method1
    # def clean(self):
    #     clenaned_data = super().clean()
    #     description = clenaned_data.get("description")
    #     if description is not None and len(description) < 5:
    #         raise ValidationError({"description":"Описание должно быть больше 5 символов"})
    #     name = clenaned_data.get("name")
    #     if name == description:
    #         raise ValidationError("Название не должно быть идентично описанию")
    #     return clenaned_data
    #Method2
    # def clean(self):
    #     cleaned_data = super().clean()
    #     name = cleaned_data.get("name")
    #     description = cleaned_data.get("description")

    #     if name == description:
    #         raise ValidationError(
    #             "Описание не должно быть идентично названию."
    #         )          
    #     return cleaned_data

    def clean_name(self):
        name = self.cleaned_data["name"]
        if name[0].islower():
            raise ValidationError(
                "Название должно начинаться с заглавной буквы"
            )
        return name