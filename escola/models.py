from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome
class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediario'),
        ('A', 'Avançado')
    )

    codigo_curso = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False)

    def __str__(self):
        return self.descricao
