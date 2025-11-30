from django.db import models
from django.contrib.auth.models import AbstractUser


class UserDetails(AbstractUser):

    phone = models.CharField(max_length=10,null=True,blank=True)
    confirm_password = models.CharField(max_length=100,null=True,blank=True)
    photo=models.ImageField(upload_to='customer_photo/',null=True,blank=True)
    accno=models.IntegerField(unique=True,null=True,blank=True)
    balance=models.IntegerField(null=True,blank=True,default=0) 
 
    def __str__(self):
        return self.username  

class transaction_model(models.Model):
    customer_id=models.IntegerField(null=True,blank=True)
    transaction_date=models.DateField(auto_now=True,null=True,blank=True)
    transaction_type=models.CharField(max_length=20,null=True,blank=True)
    amount=models.IntegerField(null=True,blank=True)
    balance=models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return str(self.customer_id)