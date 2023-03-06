from .forms import form_categorias, form_Product
from .models import Product, Categories
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


#Views de Admin
def Dashboard(request):
    products = Product.objects.all()
    categories = Categories.objects.all()
    context = {'products':products , 'categories':categories}
    return render(request, 'Dashboard.html', context)


#View Principal
def home(request):
    Ecommerce = Product.objects.all()
    context={'Ecommerce':Ecommerce}
    return render(request, 'home.html', context)

#Views de categorias
'''def categories(request):
    categories = Categories.objects.all()
    context={'categories':categories}
    return render (request,'categories/index_categories.html',context)'''

# add categorias
def add_categories(request):
    if request.method == 'POST':
        form = form_categorias(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Dashboard')
    else:
        form = form_categorias()
        context = {'form':form}
        return render(request, 'categories/add_categories.html',context)

# edit categorias
def edit_categories(request, id):
    categorias = Categories.objects.get(id=id)
    if request.method == 'POST':
        form = form_categorias(request.POST,instance=categorias)
        if form.is_valid():
            form.save()
            return redirect('Dashboard')
    else:
        form = form_categorias(instance=categorias)
        context = {'form':form}
        return render(request, 'categories/edit_categories.html', context)
# delete categorias
def delete_categories(request, id):
    categories = Categories.objects.get(id=id)
    categories.delete()
    return redirect('Dashboard')


#Views de Productos
'''def products(request):
    products = Product.objects.all()
    context={'products':products}
    return render (request,'products/index_products.html',context)'''

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
def edit_products(request, id):
    producto = Product.objects.get(id=id)
    if request.method == 'POST':
        form = form_Product(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('Dashboard')
    else:
        form = form_Product(instance=producto)
        context = {'form':form}
        return render(request, 'products/edit_products.html', context)
        

# delete productos
def delete_products(request, id):
    delete_product = Product.objects.get(id=id)
    delete_product.delete()
    return redirect('Dashboard')

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
