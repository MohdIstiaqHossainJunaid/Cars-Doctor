from django.db import models

# Create your models here.


class register(models.Model):

    email = models.EmailField(max_length=256, null=False)
    name = models.CharField(max_length=120, null=False)
    age = models.IntegerField(null=False)
    job_title = models.CharField(max_length=120, null=False)
    password = models.CharField(max_length=120, null=False)
