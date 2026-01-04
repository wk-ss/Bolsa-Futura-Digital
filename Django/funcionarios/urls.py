from django.urls import path
from .views import lista_funcionarios

urlpatterns = [
    path('', lista_funcionarios),
]
