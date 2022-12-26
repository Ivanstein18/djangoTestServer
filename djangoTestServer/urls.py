"""djangoTestServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app1.views import index_page
from app1.views import test_page
from app1.views import test_param


url_patterns = [
    path('', test_param)
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('test/', test_page),
    path('test/<name>', test_page),
    path('test/<name>/<age>', test_page),
    path('param/', include(url_patterns)),
]
