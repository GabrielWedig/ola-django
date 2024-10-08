from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=45)
    idade = models.IntegerField()
    email = models.EmailField(max_length=60)
    tipo_pessoa = models.ForeignKey('TipoPessoa', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()
    
class TipoPessoa(models.Model):
    nome = models.CharField(max_length=45)
    descricao = models.CharField(max_length=60)

    def __str__(self) -> str:
        return super().__str__()
    
class InteracaoPessoa(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)
    mensagem = models.TextField()
