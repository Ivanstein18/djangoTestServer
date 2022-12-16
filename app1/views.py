from django.shortcuts import render
from .models import Register_users
from django.http import JsonResponse


# Create your views here.
def index_page(request):
    # all_users = Register_users.objects.all()
    user = "Vasia"
    return JsonResponse({'user': user, 'age': 38})