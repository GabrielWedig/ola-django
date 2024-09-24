from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=45)
    idade = models.IntegerField()
    email = models.EmailField(max_length=60)

    def __str__(self) -> str:
        return super().__str__()
