from django.shortcuts import render,redirect,get_object_or_404
from website.forms import Contacfrom
from website.models import Banner,Category,Brand,Product,Cart,Wishlist,Order,OrderItem,ShippingAddress
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.,

def index(request):
    banner = Banner.objects.all()
    category = Category.objects.all()
    brand = Brand.objects.all()
    product = Product.objects.all()
    
    context = {
        'banner' : banner,
        'category' : category,
        'brand' : brand,
        'product' : product
    }

    return render(request,'website/index.html',context)

def about(request):
    return render(request,'website/about.html')

def contact(request):
    if request.method == 'POST':
        form = Contacfrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = Contacfrom()
    return render(request,'website/contact.html',{'form':form})

def pro_deta(request,pk):

    pro = Product.objects.get(pk=pk)
    related_produtd = Product.objects.filter(category=pro.category).exclude(id=pro.pk).order_by('?')[:11]
    context = {
        'pro':pro,
        'related_produtd' : related_produtd, 
    }
    return render(request,'website/product.html',context)

def product_search(request):
    query = request.GET['q']
    lookup = (
        Q(name__icontains=query) |
        Q(category__name__icontains=query) | 
        Q(brand__name__icontains=query)
        )
    search_product = Product.objects.filter(lookup)

    context = {
        'search_product': search_product
    }
    return render(request,'website/product_search.html',context)


def categories_product(request,pk):
    filtering = Category.objects.get(pk=pk)  
    product_filter= Product.objects.filter(category=filtering.id)
    return render(request,'website/categories_product.html',{'product_filter':product_filter})

# def product_search(request):
#     query = request.GET.get('q')  # Safely fetch the search query
#     if query:
#         lookup = (
#             Q(name__icontains=query) |
#             Q(category__name__icontains=query) |  # Assuming 'category' is a ForeignKey to a model with a 'name' field
#             Q(brand__name__icontains=query)       # Assuming 'brand' is a ForeignKey to a model with a 'name' field
#         )
#         search_product = Product.objects.filter(lookup)
#     else:
#         search_product = Product.objects.none()  # Return empty queryset if no query is provided

#     context = {
#         'search_product': search_product
#     }
#     return render(request, 'website/product_search.html', context)


# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     cart_item, created = cart.objects.get_or_create(user=request.user, product=product)
    
#     if not created:
#         cart_item.quantity += 1
#         cart_item.save()
#     return redirect('contact')

###############last###########

@login_required(login_url = 'login_page')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity +=1
        cart_item.save()
    
    return redirect('cart')

@login_required(login_url='login_page')
def increment_cart_item(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')


@login_required(login_url='login_page')
def decrement_cart_item(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()  # Remove item if quantity is 1 and decrement is pressed
    return redirect('cart')

@login_required(login_url = 'login_page')
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.product.regular_price * item.quantity for item in cart_items)
    return render(request, 'website/cart.html', {'cart_items': cart_items, 'total': total})

def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    return redirect('/')

@login_required
def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'website/wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def checkout(request):
    if request.method == 'POST':
        cart_items = Cart.objects.filter(user=request.user)
        total_price = sum(item.product.regular_price * item.quantity for item in cart_items)

        # Handle shipping address
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        delivery_area = request.POST.get('delivery_area')

        # Add delivery charge
        if delivery_area == 'inside_dhaka':
            delivery_charge = 100
        else:
            delivery_charge = 150

        # Add the delivery charge to the total price
        total_price += delivery_charge

        # Create order and order items
        order = Order.objects.create(user=request.user, total_price=total_price)
        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                price=cart_item.product.regular_price
            )

        # Clear the cart
        cart_items.delete()

        return redirect('/', order_id=order.id)

    # Calculate total price for GET requests
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.regular_price * item.quantity for item in cart_items)

    # Prepare context for the template
    delivery_area_charge = {
        'inside_dhaka': 100,
        'outside_dhaka': 150
    }

    context = {
        'total_price': total_price,
        'delivery_area_charge': delivery_area_charge,
    }

    return render(request, 'website/checkout.html', context)