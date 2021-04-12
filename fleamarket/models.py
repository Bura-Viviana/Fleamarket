from django.db import models


class CustomModel(models.Model):
    class Meta:
        abstract = True
    # required to fix warning from pycharm accesing objects at - producers\views.py
    # current_producer = Producer.objects.filter
    objects = models.Manager()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

# importam ( from fleamarket.models import CustomModel )   in fiecare fisier de modele !!!!