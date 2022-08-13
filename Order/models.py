from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    addres = models.CharField(max_length=50, null = True, blank = True)
    cart = models.OneToOneField("Cart", on_delete=models.CASCADE,null = True, blank = True)
    

    def __str__(self):
        return self.user.username

    

    

    

class OrderUnit(models.Model):
    product = models.ForeignKey("Product.Product",on_delete=models.CASCADE)
    quan = models.IntegerField()
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE)

    

    def __str__(self):
        return self.name

    
    @property
    def get_total(self):
        quan = self.quan
        price = self.product.price
        total = price * quan
        return total
        

class Cart(models.Model):
    open = models.BooleanField()
    

    @property
    def get_total(self):
        order_units = OrderUnit.objects.filter(cart= Cart.objects.get(pk=self.pk))
        
        order_units_price = 0
        for order in order_units:
            order_units_price+= order.get_total
        return order_units_price