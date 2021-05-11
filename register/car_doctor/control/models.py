from django.db import models

# Create your models here.


class worker(models.Model):

    name = models.CharField(max_length=120, null=False)
    age = models.IntegerField(null=False)
    specialist_in = models.CharField(max_length=120, null=False)
    salary = models.IntegerField(null=False)
