from django.db import models


class CustomModel(models.Model):
    class Meta:
        abstract = True
    objects = models.Manager()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

# importam ( from fleamarket.models import CustomModel )   in fiecare fisier de modele !!!!