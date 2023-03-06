from .forms import form_categorias, form_Product
from .models import Product, Categories
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

# Create your views here.

def post_detail(request, year, month, slug):
    post = get_object_or_404(Post, published_date__year=year, published_date__month=month, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

#Views de Admin
def Dashboard(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'Dashboard.html', context)


#View Principal
def home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'home.html', context)

# #Views de categorias
# def categories(request):
#     categories = Categories.objects.all()
#     context={'categories':categories}
#     return render (request,'categories/index_categories.html',context)

# #Views de Productos
# def products(request):
#     products = Product.objects.all()
#     context={'products':products}
#     return render (request,'products/index_products.html',context)



# add categorias
def add_categories(request):
    if request.method == 'POST':
        form = form_categorias(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_categories')
    else:
        form = form_categorias()
        return render(request, 'add_categories.html', {'form':form})
    
# delete categorias
def delete_categories(request, id):
    categories = Categories.objects.get(id=id)
    if request.method == 'POST':
        categories.delete()
        return redirect('categories')
    return render(request, 'delete_categories.html', {'categories':categories})

# edit categorias
def edit_categories(request, id):
    categories = Categories.objects.get(id=id)
    if request.method == 'GET':
        form = form_categorias(instance=categories)
    else:
        form = form_categorias(request.POST, instance=categories)
        if form.is_valid():
            form.save()
        return redirect('edit_categories.html')
    return render(request, 'edit_categories.html', {'form':form})





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
    
# delete productos
def delete_products(request, id):
    Product = Product.objects.get(id=id)
    Product.delete()
    return redirect('Dashboard.html')

#Views de editar productos
def edit_products(request, id):
    Product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = form_Product(request.POST, instance=Product)
        if form.is_valid():
            form.save()
            return redirect('Dashboard')
    else:
        form = form_Product(instance=Product)
        context = {'form':form}
        return render(request, 'products/add_products.html', context)

