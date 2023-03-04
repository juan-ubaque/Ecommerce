from django import forms 
from .models import Categories, Product

#Formulario de categorias
class form_categorias(forms.Form):
    """form_categorias definition."""
    name_categories = forms.CharField(max_length=120)

    class Meta:
        """Meta definition for form_categoriasform."""
        model = Categories
        fields = ('name_categories',)
    # TODO: Define form fields here

#Formulario de productos
class form_Product(forms.ModelForm):
    # """form_Product definition."""
    # Product = forms.CharField(max_length=120)
    # category = forms.CharField(max_length=120)
    # name_categories = forms.CharField(max_length=120)
    # description = forms.CharField(max_length=120)
    # price = forms.CharField(max_length=120)
    # image = forms.ImageField()
    class Meta:
        """Meta definition for form_Productform."""
        model = Product
        fields = ('Product','category','name_categories','description','price', 'image')




