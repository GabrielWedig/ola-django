from django import forms
from .models import Pessoa

class PessoaForm(forms.ModelForm): 
    interacao = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Pessoa
        fields = ['nome', 'idade', 'email', 'tipo_pessoa']

class FormDeletePessoa(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = []