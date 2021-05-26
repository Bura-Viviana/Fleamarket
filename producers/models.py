from django.db import models
from django.contrib.auth import get_user_model
from fleamarket.models import CustomModel

AuthUserModel = get_user_model()


# Create your models here.
class Producers(CustomModel):
    user = models.OneToOneField(AuthUserModel, on_delete=models.CASCADE, primary_key=True, related_name='producer')
    picture = models.ImageField(upload_to='producers', default='producers/default.jpg')
    about = models.TextField(max_length=500, default="Utilizatorul nu a adaugat descriere")


class ProductCategories(CustomModel):
    name = models.CharField(max_length=50, unique=True)


class Products(CustomModel):
    category = models.ForeignKey(ProductCategories, on_delete=models.CASCADE)
    owner = models.ForeignKey(Producers, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    unit = models.CharField(max_length=10)
    quantity = models.IntegerField(null=False, default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


class Pictures(CustomModel):
    picture = models.ImageField(upload_to='pictures', default=None)
    id_products = models.ForeignKey(Products, on_delete=models.CASCADE)
