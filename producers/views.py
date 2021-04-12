from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from producers.models import Producers


def index(request):
    current_producer = Producers.objects.filter(user__username=request.user).first()
    print(current_producer.user.first_name, current_producer.user.last_name)
    return HttpResponse(f"Hello, world. You're at the polls index."
                        f"Current user is {request.user.first_name}"
                        f"<br>"
                        f'<img src="{current_producer.picture.url}">')
