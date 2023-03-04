from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ,name='home'),
    path('products/', views.products, name='products'),
    path('Agregarproducto/', views.Agregarproducto, name='Agregarproducto'),
    path('agregarcategorias/', views.agregarcategorias, name='agregarcategorias'),
    path('categories/', views.categories, name='categories' ),
    path('Editarproducto/<int:id>', views.Editarproducto, name='Editarproducto'),
    #path('edit_products/', views.edit_products, name='edit_products'),
    #path('delete/<int:id>', views.delete, name='delete'),
    # path('update/<int:id>', views.update, name='update'),
    #path('delete_categoria/<int:id>', views.delete_categoria, name='delete_categoria'),
]