from django.db import models
from django.contrib.auth import get_user_model
from fleamarket.models import CustomModel


AuthUserModel = get_user_model()


class PhoneAndAddress(CustomModel):
    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
    city = models.CharField(max_length=30, null=False)
    street = models.CharField(max_length=30, null=False)
    number = models.IntegerField()
    phone = models.IntegerField()


class Reviews(CustomModel):
    comment = models.CharField(max_length=250)
    state = models.CharField(max_length=250, default='prcossesing')

    class Review(models.IntegerChoices):
        is_target = 1
        is_writer = 2
    type = models.IntegerField(choices=Review.choices, null=False)

    class Stars(models.IntegerChoices):
        one_star = 1
        two_stars = 2
        three_stars = 3
    star = models.IntegerField(choices=Stars.choices, null=False, default=3)

# Create your models here.
# class Reviews(models.Model):
#     id_target_user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
#     id_writer_user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
#     stars = models.IntegerField()
#     text = models.CharField(max_lenght=255, null=True)
#     state = models.CharField()


class Customer(CustomModel):
    user = models.OneToOneField(AuthUserModel, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='customers', null=True, default='customers/default.jpg')
