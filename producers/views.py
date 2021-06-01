from django.shortcuts import render

from django.shortcuts import redirect, reverse, Http404, render
from django.views.generic import ListView
from django.core.paginator import Paginator
from producers.forms.filter import SearchAndFilterProducers, SearchAndFilterProducts
# from utils.cart import Cart

# Create your views here.
from django.http import HttpResponse

from producers.models import Producers


def index(request):
    current_producer = Producers.objects.filter(user__username=request.user).first()
    print(current_producer.user.first_name, current_producer.user.last_name)
    return HttpResponse(f"Hello, world. You're at the producers index."
                        f"Current user is {request.user.first_name}"
                        f"<br>"
                        f'<img src="{current_producer.picture.url}">')


def producers_list_view(request):
    form = SearchAndFilterProducers(request.GET)
    producers_list = form.get_filtered_producers()
    paginator = Paginator(producers_list, 2)
    page_number = request.GET.get('page', 1)
    one_page = paginator.get_page(page_number)

    return render(request, 'producers/producers_list.html', {
        'page_obj': one_page,
        'form': form,
    })


def products_list_view(request):
    form = SearchAndFilterProducts(request.GET)
    products_list = form.get_filtered_products()
    paginator = Paginator(products_list, 2)
    page_number = request.GET.get('page', 1)
    one_page = paginator.get_page(page_number)

    return render(request, 'products/products_list.html', {
        'page_obj': one_page,
        'form': form,
    })
