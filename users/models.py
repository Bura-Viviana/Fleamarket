from django.db import models
from django.contrib.auth import get_user_model
from fleamarket.models import CustomModel

AuthUserModel = get_user_model()

class PhoneAndAddress(CustomModel):
    user=models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
    city=models.CharField(max_length=30, null=False)
    street=models.CharField(max_length=30, null=False )
    namber=models.IntegerField()
    phone=models.IntegerField()
#
# # Create your models here.
# class Reviews(models.Model):
#     user=models.ForeignKey(AuthUserModel, on_delete= models.CASCADE)
#     id_target_user=
#     od_writer_user=
#     is_anonymous=
#     stars=
#     text= models.CharField(max_lenght=255, null = True)
#     state=
