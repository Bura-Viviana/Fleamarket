from django.db import models
from django.contrib.auth import get_user_model
from fleamarket.models import CustomModel

AuthUserModel = get_user_model()


# Create your models here.
class Producer(CustomModel):
    user = models.OneToOneField(AuthUserModel, on_delete=models.CASCADE, primary_key=True, related_name='producer')
    picture = models.ImageField(upload_to='producers', default='producers/default.jpg')
    about = models.TextField(max_length=500, default="Utilizatorul nu a adaugat descriere")
