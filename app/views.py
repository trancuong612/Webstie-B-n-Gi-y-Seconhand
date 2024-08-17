from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
import json
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def home(request):
    categories = DanhMuc.objects.all()
    SP_theoDM = {}
    for danh_muc in categories:
        SP_theoDM[danh_muc] = SanPham.objects.filter(category = danh_muc)[:4]
    if request.user.is_authenticated:
        is_authenticated = request.user.is_authenticated
        customer = request.user
        order, created = GioHang.objects.get_or_create(customer = customer, complete = False)
        items = order.donhang_set.all()
        cartItems = order.get_cart_items
        
    else:
        items = []
        order = {'get_cart_items': 0,'get_cart_total': 0}
        cartItems = order['get_cart_items']
        is_authenticated = []
    product = SanPham.objects.all()
    context = {'product': product, 'cartItems': cartItems,  'is_authenticated': is_authenticated, 'SP_theoDM': SP_theoDM}
    return render(request, 'app/index.html', context)

def about(request):
    context = {}
    return render(request, 'app/about.html', context)

def checkout(request):
    if request.user.is_authenticated:
        is_authenticated = request.user.is_authenticated
        customer = request.user
        order, created = GioHang.objects.get_or_create(customer = customer, complete = False)
        items = order.donhang_set.all()
        cartItems = order.get_cart_items
        
    else:
        items = []
        order = {'get_cart_items': 0,'get_cart_total': 0 }
        cartItems = order['get_cart_items']
        is_authenticated = []
    context = {'items': items, 'order': order, 'cartItems':cartItems, 'is_authenticated': is_authenticated}
    return render(request, 'app/checkout.html', context)

def contact(request):
    context = {}
    return render(request, 'app/contact.html', context)

def products(request):
    tatcasp = SanPham.objects.all()
    items_per_page = 6
    paginator = Paginator(tatcasp, items_per_page)
    page = request.GET.get('page')
    sanphams = paginator.get_page(page)
    if request.user.is_authenticated:  
        is_authenticated = request.user.is_authenticated
        customer = request.user
        order, created = GioHang.objects.get_or_create(customer = customer, complete = False)
        items = order.donhang_set.all()
        cartItems = order.get_cart_items
        
    else:
        items = []
        order = {'get_cart_items': 0,'get_cart_total': 0 }
        cartItems = order['get_cart_items']
        is_authenticated = []
    context = {'sanphams': sanphams, 'cartItems':cartItems, 'is_authenticated': is_authenticated,}
    return render(request, 'app/products.html', context)

def single_product(request):
    if request.user.is_authenticated:
        is_authenticated = request.user.is_authenticated
        customer = request.user
        order, created = GioHang.objects.get_or_create(customer = customer, complete = False)
        items = order.donhang_set.all()
        cartItems = order.get_cart_items
        
    else:
        items = []
        order = {'get_cart_items': 0,'get_cart_total': 0 }
        cartItems = order['get_cart_items']
        is_authenticated = []
    id = request.GET.get('id', '')
    products = SanPham.objects.filter(id = id)
    context = {'products': products, 'items': items, 'order': order, 'cartItems':cartItems, 'is_authenticated': is_authenticated}
    return render(request, 'app/single_product.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = GioHang.objects.get_or_create(customer = customer, complete = False)
        items = order.donhang_set.all()
        
    else:
        items = []
        order = {'get_cart_items': 0,'get_cart_total': 0 }
    context = {'items': items, 'order': order}
    return render(request, 'app/cart.html', context)

def UpdateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user
    product = SanPham.objects.get(id = productId)
    order, created = GioHang.objects.get_or_create(customer = customer, complete = False)
    orderItem, created = DonHang.objects.get_or_create(order = order, product = product)
    if action == 'add':
        orderItem.quantity +=1
    elif action =='remove':
        orderItem.quantity -=1
    orderItem.save()
    if orderItem.quantity <=0:
        orderItem.delete()
    return JsonResponse('added', safe=False)

def register(request):
    form = TaiKhoan()  
    if request.method == "POST":
        form = TaiKhoan(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'app/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('Home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.info(request, 'Tài khoản Hoặc Mật Khẩu Không Đúng')
    context = {}
    return render(request, 'app/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')