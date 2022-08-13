from django.db import models

# Create your models here.



class Product(models.Model):
    name = models.CharField( max_length=50)
    cost = models.IntegerField()
    price = models.IntegerField()
    


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Prodyct_detail", kwargs={"pk": self.pk})


class Image(models.Model):
    img = models.ImageField(upload_to='images/products', null=True,blank=True)
    prd = models.ForeignKey(Product,on_delete=models.CASCADE)    
    def __str__(self):
        return self.prd.name

    def get_absolute_url(self):
        return reverse("Image_detail", kwargs={"pk": self.pk})
