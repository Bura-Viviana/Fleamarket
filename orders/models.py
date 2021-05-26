from django.db import models
from django.contrib.auth import get_user_model
from fleamarket.models import CustomModel

AuthUserModel = get_user_model()


class Orders(CustomModel):
    id_client = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE, related_name='client_orders')
    id_producer = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE, related_name='producer_orders')
    order_data = models.DateTimeField(auto_now_add=True)
    completion_date = models.DateTimeField()

    class Status(models.TextChoices):
        created = "the order was placed"
        processing = "processing order"
        ready_for_pickup = "the order is ready"
        completed = "client received the order"
    status = models.TextField(choices=Status.choices, null=False, default=Status.created)

    # class Review(models.IntegerChoices):
    #     is_target=1
    #     is_writher=2
    # type = models.IntegerField(choices=Review.choices, null=False)

# class Products(CustomModel):
#     id_category = models.ForeignKey(ProductCategories, on_delete=models.CASCADE)
#     id_owner = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=500)
#     unit = models.CharField(max_length=10)
#     quantity = models.IntegerField(null=False, default=1)
#     price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


# Create your models here.
