from itertools import product
from unicodedata import name
from django.test import TestCase
from .models import (Order, OrderUnit ,Cart)
from Product.models import Product
from django.contrib.auth.models import User
# Create your tests here.
Cart.objects.create(open = True)
cart = Cart.objects.get(id = 1)
Product.objects.create(name= "test", cost= 50, price = 60)
prd = Product.objects.get(id = 1)
OrderUnit.objects.create(product= prd, quan= 5, cart = cart)
ordunt = OrderUnit.objects.get(id=1)
orduntotal = ordunt.get_total
crtotal = cart.get_total


class TestCart(TestCase):
    def test_cart_content(self):
        self.assertEqual(cart.open, True)
        self.assertEqual(crtotal, orduntotal)

class TestOrderUnit(TestCase):
    def test_ordunt_content(self):
        self.assertEqual(ordunt.product,prd)
        self.assertEqual(ordunt.quan,5)
        self.assertEqual(orduntotal, 60*5)
