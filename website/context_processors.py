from website.models import Category,Cart,Wishlist

def g_categories(request):
    g_cate = Category.objects.all()
    return {'g_cate': g_cate}

def g_cart(request):
    g_card = Cart.objects.count()
    return {'g_card': g_card}

def g_wishlist(request):
    wishlist = Wishlist.objects.count()
    return {'wishlist': wishlist}