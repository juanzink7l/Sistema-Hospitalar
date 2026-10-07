from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('novoPaciente/', views.novo_paciente, name='novo_paciente'),
    path('alterarDados/<int:codigo_paciente>/', views.alterar_dados, name='alterar_dados'),
    path('deletarPaciente/<int:codigo_paciente>', views.deletar_paciente, name='deletar_paciente'),
]