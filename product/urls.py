from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home ,name='home'),
    path('login/', views.login ,name='login'),

    # dashboard
    path('Dashboard/', views.Dashboard , name='Dashboard'),

    # categorias
    # path('categories/', views.categories, name='categories' ),
    path('categories/add_categories/', views.add_categories, name='add_categories'),
    path('edit_categories/<int:id>', views.edit_categories, name='edit_categories'),
    path('delete_categories/<int:id>', views.delete_categories, name='delete_categories'),

    # productos
    # path('products/', views.Dashboard, name='products'),
    path('add_products/', views.add_products, name='add_products'),
    path('edit_products/<int:id>', views.edit_products, name='edit_products'),
    path('delete_products/<int:id>', views.delete_products, name='delete_products'),
    

    # path('update/<int:id>', views.update, name='update'),
    path('post/<int:year>/<int:month>/<slug:slug>/', views.post_detail, name='post_detail'),

    path('productos/categoria/<int:category_id>/', views.products_by_category, name='products_by_category'),
    # pasarela de pagos
    #path('pasarela/', views.pasarela, name='pasarela'),
    # path('recoverPassword/', views.crear_recoverPassword , name= ('recoverPassword'))

]
