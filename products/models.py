from django.db import models
from accounts.models import NewUser

class Product(models.Model):
    user = models.ForeignKey(NewUser,on_delete=models.CASCADE,related_name="products")
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)