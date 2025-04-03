from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

# Create your views here.
from django.shortcuts import render, redirect
from .models import Product

def product_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        discript = request.POST.get('discript')
        price = request.POST.get('price')
        
        # 새로운 상품 생성
        Product.objects.create(
            name=name,
            discript=discript,
            price=price
        )
        # 등록 후 목록 페이지(/shop)로 리다이렉트
        return redirect('/shop')
    
    # GET 요청 시 상품 등록 페이지 렌더링
    return render(request, 'create.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'read.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'detail.html', {'product': product})

def product_update(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.discript = request.POST.get('discript')
        product.price = request.POST.get('price')
        product.save()
        return redirect(f'/shop/{product.id}')
    # GET 요청 시 기존 정보를 edit.html에 표시
    return render(request, 'edit.html', {'product': product})

def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('/shop')
    # GET 요청 시 삭제 확인 페이지(delete.html) 렌더링
    return render(request, 'delete.html', {'product': product})