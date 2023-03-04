from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ,name='home'),
    path('Dashboard/', views.Dashboard , name='home'),
    path('products/', views.products, name='products'),
    path('Agregarproducto/', views.Agregarproducto, name='Agregarproducto'),
    path('agregarcategorias/', views.agregarcategorias, name='agregarcategorias'),
    path('categories/', views.categories, name='categories' ),
]