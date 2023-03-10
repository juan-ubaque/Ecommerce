from django import forms 
from .models import Categories, Product

#Formulario de categorias
class form_categorias(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ('name_categories',)

#Formulario de productos
class form_Product(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('Product','category','name_categories','description','price', 'image')




