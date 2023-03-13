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
            'Product': forms.TextInput(attrs={'class': ' form-group text-success  visually-hidden visually-hidden form-label border-9 form-control ','placeholder':'ingrece el producto'}),
            'category': forms.Select(attrs={'class': 'form-group text-success form-control-lg visually-hidden form-label form-control'}),
            'name_categories': forms.Select(attrs={'class': 'form-group form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-group form-control  col-xs-4'}),
            'price': forms.NumberInput(attrs={'class': 'form-group form-control-sm col-xs-4'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-group form-control-sm'}),
        }