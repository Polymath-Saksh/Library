"""Library URL Configuration

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
from django.urls import include,path
from issue import views as iviews
from mng import views as mviews
from book_add import views as baviews
from book_delete import views as bdviews
from returns import views as rviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('issue/',iviews.i),
    path('mng/',mviews.m),
    path('book_add/',baviews.ba),
    path('book_delete/',bdviews.bd),
    path('returns/',rviews.r)
]
