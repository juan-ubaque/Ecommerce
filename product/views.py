from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Categories
from .forms import form_categorias

# Create your views here.

def products(request):
    return render (request,'products.html')


def categories(request):
    categories = Categories.objects.all()
    context={'categories':categories}
    return render (request,'categories/index_categories.html',context)

def home(request):
    Ecommerce = Product.objects.all()
    context={'home':home}
    return render(request, 'home.html', context)

def Agregarproducto(request):
    if request.method == 'POST':
        Product = request.POST['Product']
        category = request.POST['category']
        name_categories = request.POST['name_categories']
        description = request.POST['description']
        price = request.POST['price']
        Product = Product(Product=Product, category=category, name_categories=name_categories, description=description, price=price)
        Product.save()
        return redirect('agregarproducto.html')
    else:
        return render(request, 'Agregarproducto.html')


def agregarcategorias(request):
    if request.method == 'POST':
        form = form_categorias(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories.html')
    else:
        form = form_categorias()
        return render(request, 'categories.html', {'form':form})