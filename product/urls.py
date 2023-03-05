from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ,name='home'),
    path('Dashboard/', views.Dashboard , name='Dashboard'),
    path('products/', views.products, name='products'),
    path('add_products/', views.add_products, name='add_prodcuts'),
    path('delete_products/<int:products.id>', views.delete_products, name='delete_products'),
    path('agregarcategorias/', views.agregarcategorias, name='agregarcategorias'),
    path('categories/', views.categories, name='categories' ),
    # path('Editarproducto/<int:id>', views.Editarproducto, name='Editarproducto'),
    # path('edit_products/', views.edit_products, name='edit_products'),
    # path('update/<int:id>', views.update, name='update'),
    # path('delete_categoria/<int:id>', views.delete_categoria, name='delete_categoria'),
]