"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('simple/', simple),
    path('stream/', stream),
    path('file_upload/', file_upload),
    path('get_object/<int:id>', get_object, name='get_object'),
    path('get_list/<int:school_id>', get_list, name='get_list'),
    path('create_comment/', create_comment, name='create_comment'),
    path('get_comment/', get_comment, name='get_comment'),
    path('view_comment/<int:id>', view_comment, name='view_comment'),
]
