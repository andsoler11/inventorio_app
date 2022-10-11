from django.shortcuts import render, redirect
from .models import Products
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def renderProduct(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        cantidad = request.POST.get('cantidad')
        precio = request.POST.get('precio')
        descripcion = request.POST.get('descripcion')
        profile = request.user

        product = Products(nombre=nombre, cantidad=cantidad, precio=precio, descripcion=descripcion, profile=profile)
        product.save()

    products = Products.objects.filter(profile_id=request.user.id)
    context = {'page': 'inventario', 'products': products}

    return render(request, 'inventario.html', context)

@login_required(login_url='login')
def editProduct(request, pk):
    product = Products.objects.get(id=pk)

    if request.method == 'POST':
        Products.objects.filter(id=pk).update(
            nombre=request.POST.get('nombre'),
            cantidad=request.POST.get('cantidad'),
            precio=request.POST.get('precio'),
            descripcion=request.POST.get('descripcion')
        )
        return redirect('product')

    context = {'page': 'inventario', 'product': product}
    return render(request, 'edit_inventario.html', context)

@login_required(login_url='login')
def deleteProduct(request, pk):
    product = Products.objects.get(id=pk)
    product.delete()
    return renderProduct(request)

