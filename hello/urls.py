"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from hello.views import hello, GenreListView, AddGenreView, AddPersonView, AddProducerView, ProducerListView

urlpatterns = [

    path('', hello, name='hello'),
    path('accounts/', include('accounts.urls')),
    path('genre/list/', GenreListView.as_view(), name='genrelist'),
    path('genre/add/', AddGenreView.as_view(), name='addgenre'),
    path('person/add/', AddPersonView.as_view(), name='addperson'),
    path('producer/add/', AddProducerView.as_view(), name='producerform'),
    path('producer/list/', ProducerListView.as_view(), name='producerlist')

]
