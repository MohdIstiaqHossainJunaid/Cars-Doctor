from django.db import models

# Create your models here.


class productlist(models.Model):
    name = models.CharField(max_length=120, null=False)
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
