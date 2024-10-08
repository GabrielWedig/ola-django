from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from .forms import FormDeletePessoa, PessoaForm
from .models import Pessoa, InteracaoPessoa
from django.contrib import messages

class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = 'cadastrar_pessoa.html'
    success_url = reverse_lazy('listar_pessoas')

    def form_valid(self, form):
        response = super().form_valid(form)
        interation = form.cleaned_data['interacao']

        if(not interation):
            InteracaoPessoa.objects.create(
                pessoa = self.object,
                mensagem = form.cleaned_data['interacao']
            )

        messages.success(self.request, "Pessoa cadastrada com sucesso")
        return response

class PessoaListView(ListView):
    model = Pessoa
    template_name = 'lista_pessoas.html'

class PessoaUpdateView(UpdateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = 'editar_pessoa.html'
    success_url = reverse_lazy('listar_pessoas')

class PessoaDetailView(DetailView):
    model = Pessoa
    template_name = 'detalhar_pessoa.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pessoa = self.get_object
        interacoes = InteracaoPessoa.objects.filter(pessoa=pessoa)
        interacoes_formatada = [{
            'data_hora'
        }]

        context['interacoes_formatada'] = interacoes
        return context

class PessoaDeleteView(DeleteView):
    model = Pessoa
    form_class = FormDeletePessoa
    template_name = 'deletar_pessoa.html'
    success_url = reverse_lazy('listar_pessoas')
    
