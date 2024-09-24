from django.urls import path
from .views import PessoaCreateView, PessoaListView

urlpatterns = [
    path('cadastrar/', PessoaCreateView.as_view(), name='cadastrar_pessoa'),
    path('listar/', PessoaListView.as_view(), name='listar_pessoas'),
]