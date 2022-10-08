from django import forms
from django.forms import ModelForm, ValidationError
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    
    def clean_price(self):
        price = int(self.cleaned_data['price'])
        if price > 1000:
            raise ValidationError("Product is too expensive")
        
        return price

    def clean_description(self):
        description = self.cleaned_data['description']

        if len(description) <= 20:
            raise ValidationError("Product must have a good description")
        
        return description

