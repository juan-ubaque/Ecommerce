from .forms import form_categorias, form_Product
from .models import Product, Categories
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


#Views de Admin
def Dashboard(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'Dashboard.html', context)


#View Principal
def home(request):
    Ecommerce = Product.objects.all()
    context={'home':home}
    return render(request, 'home.html', context)


#Views de Productos
def products(request):
    products = Product.objects.all()
    context={'products':products}
    return render (request,'Dashboard.html',context)

#Views de agregar productos

def add_products(request):
    if request.method == 'POST':
        form = form_Product(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Dashboard')
    else:
        form = form_Product()
        context = {'form':form}
        return render(request, 'products/add_products.html', context)

#Views de editar productos
def Editarproducto(request, id):
    Product = Product.objects.get(id=id)
    if request.method == 'GET':
        form = form_Product(instance=Product)
    else:
        form = form_Product(request.POST, instance=Product)
        if form.is_valid():
            form.save()
        return redirect('edit_products.html')
    return render(request, 'Editarproducto.html', {'form':form})

#Views de categorias
def categories(request):
    categories = Categories.objects.all()
    context={'categories':categories}
    return render (request,'categories/index_categories.html',context)

# add categorias
def agregarcategorias(request):
    if request.method == 'POST':
        form = form_categorias(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories.html')
    else:
        form = form_categorias()
        return render(request, 'categories.html', {'form':form})

# edit categorias
def Editarcategorias(request, id):
    categories = Categories.objects.get(id=id)
    if request.method == 'GET':
        form = form_categorias(instance=categories)
    else:
        form = form_categorias(request.POST, instance=categories)
        if form.is_valid():
            form.save()
        return redirect('edit_categories.html')
    return render(request, 'Editarcategorias.html', {'form':form})

# delete categorias
def delete_categories(request, id):
    categories = Categories.objects.get(id=id)
    if request.method == 'POST':
        categories.delete()
        return redirect('categories.html')
    return render(request, 'delete_categories.html', {'categories':categories})

# delete productos
def delete_products(request, id):
    Product = Product.objects.get(id=id)
    if request.method == 'POST':
        Product.delete()
        return redirect('products.html')
    return render(request, 'delete_products.html', {'Product':Product})

# # update productos
# def update_products(request, id):
#     Product = Product.objects.get(id=id)
#     if request.method == 'GET':
#         form = form_Product(instance=Product)
#     else:
#         form = form_Product(request.POST, instance=Product)
#         if form.is_valid():
#             form.save()
#         return redirect('products.html')
#     return render(request, 'update_products.html', {'form':form})
