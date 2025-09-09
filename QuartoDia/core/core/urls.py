from django.urls import path
from . import views

urlpatterns = [
    path('consulta-cep/', views.consulta_cep, name='consulta_cep'),
    path('', views.home, name='home'),
]
