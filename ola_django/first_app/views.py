from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import PessoaForm
from .models import Pessoa

class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = 'cadastrar_pessoa.html'
    success_url = reverse_lazy('listar_pessoas')

class PessoaListView(ListView):
    model = Pessoa
    template_name = 'lista_pessoas.html'
    
