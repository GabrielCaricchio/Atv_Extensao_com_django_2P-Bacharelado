
from django.urls import path
from app_site import views

#rota(url.py) > views.py > html
#rota, view responsavel, nome de referência
urlpatterns = [
    path('', views.index, name='index')
    path('', views.quiz, name='quiz')
]