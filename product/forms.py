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
        widgets = {
            'Product': forms.TextInput(attrs={'class': 'form-group'}),
            'category': forms.Select(attrs={'class': 'form-group'}),
            'name_categories': forms.Select(attrs={'class': 'form-group'}),
            'description': forms.Textarea(attrs={'class': 'form-group'}),
            'price': forms.NumberInput(attrs={'class': 'form-group'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-group'}),
        }