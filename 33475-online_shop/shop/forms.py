from itertools import product
import json

from django import forms

from shop.models import Product

class CartForm(forms.Form):
  
    def __init__(self, *args, items , **kwargs):
        super().__init__(*args, **kwargs)
        
        for i in range(len(items)):
            product = Product.objects.get(id=items[i].id)

            number_field = 'number_' + str(product.id)
            color_field = 'color_' + str(product.id)

            name = items[i].name

            colors_queryset = product.colors_available.order_by('name')
            
            colorsـchoice = []

            for color in colors_queryset:
                colorsـchoice.append(((color.name), (color.name)))

            self.fields[number_field] = forms.IntegerField(initial=1, required=False, label=name)
            self.fields[color_field] = forms.ChoiceField(choices=colorsـchoice, initial=colorsـchoice[0], required=False, label='color')
    
    
    def clean(self):
        cleaned_data = super().clean()
        
        for key, val in self.fields.items():
            if isinstance(val, forms.IntegerField):

                if cleaned_data[key] is None:
                    cleaned_data[key] = 1

            elif isinstance(val, forms.ChoiceField):
                choice_id = int(key.split('_')[1])
                if cleaned_data[key] == '':
                    colors_queryset = Product.objects.get(id=choice_id).colors_available.all().order_by('name')
                    cleaned_data[key] = colors_queryset[0].name

        return cleaned_data