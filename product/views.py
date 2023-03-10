from .forms import form_categorias, form_Product
from .models import Product, Categories
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
#Views de Productos
def products(request):
    products = Product.objects.all()
    context={'products':products}
    return render (request,'products/index_products.html',context)

# Create your views here.

def post_detail(request, year, month, slug):
    post = get_object_or_404(Post, published_date__year=year, published_date__month=month, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

#Views de Admin
def Dashboard(request):
    products = Product.objects.all()
    categories = Categories.objects.filter()
    context = {'products':products , 'categories':categories}
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

# add categorias
def add_categories(request):
    if request.method == 'POST':
        form = form_categorias(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Dashboard')
    else:
        form = form_categorias()
        return render(request, 'categories/add_categories.html', {'form':form})


# delete categorias
def delete_categories(request, id):
    categories = Categories.objects.get(id=id)
    categories.delete()
    return redirect('Dashboard')

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
        return render(request, 'categories/add_categories.html', context)



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
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('Dashboard')

#Views de editar productos
def edit_products(request, id):
    productos  = Product.objects.get(id=id)
    if request.method == 'POST':
        form = form_Product(request.POST, instance=productos)
        if form.is_valid():
            form.save()
            return redirect('Dashboard')
    else:
        form = form_Product(instance=productos)
        context = {'form':form}
        return render(request, 'products/add_products.html', context)

#filter information
def products_by_category(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    categories = Categories.objects.all()
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'Dashboard.html', context)