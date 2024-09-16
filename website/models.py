from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class ContactInfo(models.Model):
    Name = models.CharField(max_length=300)
    Email = models.EmailField()
    Phone_Number = models.CharField(max_length=13)
    Subject = models.CharField(max_length=450)
    Message = models.TextField()

    class Meta:
       verbose_name_plural = "Contact-Infos" 
    def __str__(self):
        return self.Name

class Banner(models.Model):
    name_Promotions = models.CharField(max_length=300)
    intro_title1 = models.CharField(max_length=400,null=True, blank=True)
    intro_title2 = models.CharField(max_length=400,null=True, blank=True)
    old_price = models.CharField(max_length=14)
    new_price = models.CharField(max_length=14)
    new_price_sub = models.CharField(max_length=14)
    image = models.ImageField(upload_to='banner_image/')
    class Meta:
        verbose_name_plural =("Banner")

    def __str__(self):
        return self.name_Promotions

class Category(models.Model):
    name = models.CharField(max_length=50, null=False)
    img = models.ImageField(upload_to='category_images/', null=False)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 

class Brand(models.Model):
    name = models.CharField(max_length=50, null=False)
    img = models.ImageField(upload_to='category_images/', null=False)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='ProducImage')
    regular_price= models.PositiveIntegerField()
    discount_price= models.PositiveIntegerField(blank=True,null=True)
    descriptions =  models.TextField()
    aditional_descriptions =  models.TextField()
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural =("Products")

    def __str__(self):
        return self.name + ' ' + self.category.name

# class cart(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     product = models.ForeignKey(Product,on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     added_at = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.product.name} - {self.quantity}"

########last###########last#######################################

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.user.username}'s wishlist - {self.product.name}"

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return f'{self.product.name} of {self.quantity}'

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    delivery_area = models.CharField(max_length=20, choices=[('inside_dhaka', 'Inside Dhaka'), ('outside_dhaka', 'Outside Dhaka')])
    
    def __str__(self):
        return f"{self.user.username} - {self.address}"