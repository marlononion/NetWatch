from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),  # Página inicial
    path('results/', views.ResultsView.as_view(), name='results'),  # Página de resultados
]