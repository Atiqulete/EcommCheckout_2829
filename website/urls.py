from django.urls import path
from website.views import index,contact,pro_deta,about,product_search,categories_product,add_to_cart,cart,wishlist,add_to_wishlist,increment_cart_item,decrement_cart_item,checkout

urlpatterns = [
    path('',index,name='index'),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),
    path('search/',product_search,name='product_search-page'),
    path('pro_deta/<int:pk>/',pro_deta,name='pro_deta'),
    path('categories_product/<int:pk>/',categories_product,name='categories_product_page'),

    path('add_to_cart/<int:product_id>/',add_to_cart, name='add_to_cart'),
    path('increment/<int:item_id>/',increment_cart_item, name='increment_cart_item'),
    path('decrement/<int:item_id>/',decrement_cart_item, name='decrement_cart_item'),
    path('cart/', cart, name='cart'),
    
    path('wishlist', wishlist, name='wishlist'),
    path('add_to_wishlist/<int:product_id>', add_to_wishlist, name='add_to_wishlist'),
    
    path('checkout',checkout, name='checkout'),
  
]