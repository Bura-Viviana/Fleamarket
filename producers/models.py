from django.db import models
from django.contrib.auth import get_user_model
from fleamarket.models import CustomModel

AuthUserModel = get_user_model()


# Create your models here.
class Producer(CustomModel):
    user = models.OneToOneField(AuthUserModel, on_delete=models.CASCADE, primary_key=True, related_name='producer')
    picture = models.ImageField(upload_to='producers', default='producers/default.jpg')
    about = models.TextField(max_length=500, default="Utilizatorul nu a adaugat descriere")


class ProductCategories(CustomModel):
    name = models.TextField(max_length=50)


class Products(CustomModel):
    id_category = models.ForeignKey(ProductCategories, on_delete=models.CASCADE)
    id_owner = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
    name=models.TextField(max_length=50)
    description=models.TextField(max_length=500)
    quantity=models.IntegerField(null=False, default=1)
    price=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)