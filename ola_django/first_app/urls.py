from django.urls import path
from .views import PessoaCreateView, PessoaDeleteView, PessoaListView, PessoaUpdateView, PessoaDetailView

urlpatterns = [
    path('cadastrar/', PessoaCreateView.as_view(), name='cadastrar_pessoa'),
    path('<int:pk>/editar/', PessoaUpdateView.as_view(), name='editar_pessoa'),
    path('<int:pk>/detalhar/', PessoaDetailView.as_view(), name='detalhar_pessoa'),
    path('<int:pk>/deletar/', PessoaDeleteView.as_view(), name='deletar_pessoa'),
    path('listar/', PessoaListView.as_view(), name='listar_pessoas'),
]