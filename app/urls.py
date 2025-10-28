<<<<<<< HEAD
from django.urls import path, include
from app import views

urlpatterns = [
    path("main-page/", views.index, name="index"),
=======
from django.urls import path
from app import views

urlpatterns = [
    path("main-page/", views.index, name="index")
>>>>>>> 525a4ba (Сделана первая версия МП для ДЗ)
]