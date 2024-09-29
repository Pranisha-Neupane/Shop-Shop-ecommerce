
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Customer"  
    
    def __str__(self):               
        return self.user.username

    #extra fiels will be come here
    phone_field=models.CharField(max_length=10,blank=False)


class Product(models.Model):
    CATAGORY_CHOICES=[
        ('Electronics','Electronics'),
        ('Clothing','Clothing'),
    ]

    name=models.CharField(max_length=255)
    category=models.CharField(max_length=50,choices=CATAGORY_CHOICES ,default='Electronics')
    price=models.DecimalField(max_digits=10,decimal_places=2)
    discounted_price=models.IntegerField(default=True)
    image=models.ImageField(upload_to='products/',blank=True,null=True)
    # description=models.TextField(blank=True,null=True)
    description = models.TextField() 

    def __str__(self):
        return self.name