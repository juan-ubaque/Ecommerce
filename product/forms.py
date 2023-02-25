from django import forms 
from .models import Categories, Product

class form_categorias(forms.Form):
    """form_categorias definition."""
    name_categories = forms.CharField(max_length=120)

    class Meta:
        """Meta definition for form_categoriasform."""
        model = Categories
        fields = ('name_categories',)
    # TODO: Define form fields here
