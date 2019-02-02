from django.db import models

# Create your models here.

from django.db import models

class Contact(models.Model):
    contact_name=models.CharField(max_length=50)
    email = models.CharField(max_length=50,unique=True)


