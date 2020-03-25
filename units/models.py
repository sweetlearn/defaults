from django.contrib.auth.models import User
from django.db import models

# CUSTOMERS:
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10)
    id_card = models.CharField(max_length=12)


    def __str__(self):
        return self.user


