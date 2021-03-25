
from django.shortcuts import render


def homepage(request):
    return render(request, 'my_homepage.html',{"brand":"Piata Volanta"})

def contact_view(request):
    return render(request, "contact.html")