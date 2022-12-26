from django.shortcuts import render
from .models import Register_users
from django.http import HttpResponse
import json


# Create your views here.
def index_page(request):
    user = "Ivanstein"
    with open("templates/index.html", "r") as f:
        page_data = f.read().format(user)
    return HttpResponse(page_data, content_type="text/html")


def test_page(request, name="Пупа", age=0):
    with open("templates/test.html", "r") as f:
        test_page = f.read().format(name, age)
    return HttpResponse(test_page, content_type="text/html")


def test_param(request):
    param = request.GET.get("param", 1234)
    with open("templates/param.html", "r") as f:
        param_page = f.read().format(param)
    return HttpResponse(param_page, content_type="text/html")