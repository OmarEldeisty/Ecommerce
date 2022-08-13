from django.test import TestCase
from .models import Product,Image
# Create your tests here.

class TestProduct(TestCase):
    
    def setUp(self):
        self.product = Product.objects.create(name="hi",cost=11,price=12)
    
    def test_product_content(self):
        
        self.assertEqual(self.product.name, "hi")
        self.assertEqual(self.product.cost, 11)
        self.assertEqual(self.product.price, 12)
        
class TestImage(TestCase):
    
    def setUp(self):
        self.product = Product.objects.create(name="hi",cost=11,price=12)
        self.Image = Image.objects.create(prd=Product.objects.get(id=1))
    def test_img(self):
        self.assertEqual(self.Image.prd, self.product)
        
