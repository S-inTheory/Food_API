"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from djangoProject.views import recipients_list, recipient_detail, data_list, data_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipients', recipients_list, name='recipients-list'),
    path('recipients/<id>', recipient_detail, name='recipient-detail'),
    path('product-sets', data_list, name='data-list'),
    path('product-sets/<id>', data_detail, name='data-detail'),
    path('product-sets/?min_price=N', data_list, name='data-list-price'),
    path('product-sets/?min_weight=N', data_list, name='data-list-weight'),
]
