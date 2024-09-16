from django.contrib import admin
from .models import ContactInfo,Banner,Category,Brand,Product,Cart,Wishlist,Order,ShippingAddress,OrderItem

# Register your models here.
admin.site.register(ContactInfo)
admin.site.register(Banner)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(OrderItem)
admin.site.register(Wishlist)
admin.site.register(Order)
admin.site.register(ShippingAddress)

