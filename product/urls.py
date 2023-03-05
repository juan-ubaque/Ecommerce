from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ,name='home'),
    # dashboard
    path('Dashboard/', views.Dashboard , name='Dashboard'),
    # categorias
    path('categories/', views.categories, name='categories' ),
    path('add_categories/', views.add_categories, name='add_categories'),
    path('delete_categories/<int:id>', views.delete_categories, name='delete_categories'),
    # productos
    path('products/', views.products, name='products'),
    path('edit_products/<int:id>', views.edit_products, name='edit_products'),
    path('add_products/', views.add_products, name='add_products'),
    path('products/delete/<int:id>', views.delete_products, name='delete_products'),
    
    # path('update/<int:id>', views.update, name='update'),

]