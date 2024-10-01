from django.urls import path
from .views import PessoaCreateView, PessoaListView, PessoaUpdateView

urlpatterns = [
    path('cadastrar/', PessoaCreateView.as_view(), name='cadastrar_pessoa'),
    path('<int:pk>/editar/', PessoaUpdateView.as_view(), name='editar_pessoa'),
    path('listar/', PessoaListView.as_view(), name='listar_pessoas'),
]