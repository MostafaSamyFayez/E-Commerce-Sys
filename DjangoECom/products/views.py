
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json
import datetime
from .models import Product,User,OrderItem,Order,ShippingAddress
from users.models import Customer
from .decorators import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.files.storage import FileSystemStorage
from products.models import *
# Create your views here.
def index(request):
    return render(request, "users/index.html")

def products(request):  #Products_Store
    products_list = Product.objects.all()
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
    else:
        cartItems=0
    # Paginator for products 
    page = request.GET.get('page', 1)
    paginator = Paginator(products_list, 8) #number of products in one page = 8
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products_list = paginator.page(paginator.num_pages)

    #we need to send all Category here to choose one form them in forntend
    context = {'products':products,'cartItems':cartItems}
    return render(request, 'products/products.html', context)

def productDetails(request):  #Products_Store
    productId=request.GET['productId']
    product=Product.objects.get(id=productId)
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
    else:
        cartItems=0
    context = {'product':product,'cartItems':cartItems}
    return render(request, 'products/productDetails.html', context)

    #we need to send all Category here to choose one form them in forntend
    context = {'products':products,'cartItems':cartItems}
    return render(request, 'products/products.html', context)
#@allowed_users(allowed_roles=['customer'])
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items =order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order ={'get_cart_total':0,'get_cart_items':0}
        cartItems = 0
    context ={'items':items , 'order':order, 'cartItems':cartItems}
    return render(request, 'products/cart.html',context)

@allowed_users(allowed_roles=['customer'])
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items =order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order ={'get_cart_total':0,'get_cart_items':0}
        cartItems = order['get_cart_items']

    context ={'items':items , 'order':order,'cartItems':cartItems}
    return render(request, 'products/cart.html',context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created =Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order,product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1 )
    elif action == 'delete':
        orderItem.quantity = (orderItem.quantity - orderItem.quantity)
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Done', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment submitted..', safe=False)

def dashboard(request):  #Products_Store
    seller=request.user
    products=seller.product_set.all()
    context = {'products':products,'seller':seller}
    return render(request, 'products/sellerDashboard.html', context)




def addProductView(request):  #Products_Store
    seller=request.user
    productId = "null"
    context = {'seller': seller,"productId":productId}
    return render(request, 'products/addProduct.html', context)

def editProductview(request):  #Products_Store
    productId=request.GET['productId']
    seller = request.user
    context = {'seller': seller,'productId':productId}
    return render(request, 'products/addProduct.html', context)

def addProduct(request):  #Products_Store
    productId=request.POST['productId']

    uploaded_file=request.FILES['Productimg']
    fs=FileSystemStorage()
    fs.save(uploaded_file.name,uploaded_file)
    image = uploaded_file.name

    seller=request.user
    name = request.POST["productName"]
    quantity = request.POST["Quantity"]
    price = request.POST["Price"]
    discount_price = request.POST["discountPercentage"]
    description=request.POST["Description"]
    category = request.POST["category"]
    label = "S"
    if(productId=="null"):

        product = Product.objects.create(
            name=name,
            price=price,
            quantity=quantity,
            discount_price=discount_price,
            description=description,
            image=image,
            category=category,
            label=label,
            seller=seller
        )
        product.save()
    else:
        Product.objects.filter(id=productId).update(
            name=name,
            price=price,
            quantity=quantity,
            discount_price=discount_price,
            description=description,
            image=image,
            category=category,
            label=label,
            seller=seller
        )

    products = seller.product_set.all()
    context = {'products': products, 'seller': seller}
    return render(request, 'products/sellerDashboard.html', context)

def profile(request):
    user=request.user
    context = {'user': user}
    return render(request,'products/profile.html', context)

def updateProfile(request):
    customer=request.user.customer
    customerId=customer.id

    uploaded_file = request.FILES['profileImg']
    fs = FileSystemStorage()
    fs.save(uploaded_file.name, uploaded_file)
    image = uploaded_file.name

    Customer.objects.filter(id=customerId).update(
        image=image,
    )

    user=request.user
    context = {'user': user}
    return render(request,'products/profile.html', context)


def UpdateWishList(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    wishList, created =WishList.objects.get_or_create(customer=customer)

    wishListItem, created = WishListItem.objects.get_or_create(wishList=wishList,product=product)

    if action == 'add':
        wishListItem.save()
    elif action == 'delete':
        wishListItem.delete()
    return JsonResponse('Done', safe=False)

def ViewWishList(request):
    customer = request.user.customer
    wishList,created = WishList.objects.get_or_create(customer=customer)
    items =wishList.wishlistitem_set.all()
    context ={'items':items , 'wishList':wishList}
    return render(request, 'products/wishlist.html',context)