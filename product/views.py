from .forms import form_categorias
from .models import Product, Categories
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


#Views de Admin
def Dashboard(request):
    return HttpResponse('Esta es la vista para el Admin')



#View Principal
def home(request):
    Ecommerce = Product.objects.all()
    context={'home':home}
    return render(request, 'home.html', context)


#Views de Productos
def products(request):
    return render (request,'products.html')
    return HttpResponse('Esta es la vista para los prodructos XD')


def Agregarproducto(request, id):
    Product = Product.objects.get (id=id)
    if request.method == 'POST':
        form = form_categorias(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products.html')



    
#Views de categorias
def categories(request):
    categories = Categories.objects.all()
    context={'categories':categories}
    return render (request,'categories/index_categories.html',context)


def agregarcategorias(request):
    if request.method == 'POST':
        form = form_categorias(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories.html')
    else:
        form = form_categorias()
        return render(request, 'categories.html', {'form':form})
