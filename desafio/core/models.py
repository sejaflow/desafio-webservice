from django.db import models

# Create your models here.

class Profissao(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    def __str__(self):
        return self.nome

class Candidato(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    cpf = models.CharField(max_length=13, null=False, blank=False, unique=True)
    data_nascimento = models.DateField()
    profissoes = models.ManyToManyField(Profissao)
    
    def __str__(self):
        return self.nome + "-" + self.cpf

class Orgao (models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    sigla = models.CharField(max_length=5, null=False, blank=False)

    def __str__(self):
        return self.sigla +" - "+ self.nome

class Concurso(models.Model):
    orgao = models.ForeignKey(Orgao,on_delete=models.CASCADE)
    edital = models.CharField(max_length=10, null=False, blank=False)
    codigo_concurso = models.CharField(max_length=10, null=False, blank=False,unique=True)
    profissoes = models.ManyToManyField(Profissao)

    def __str__(self):
        return self.orgao.sigla +" - "+ self.edital + "-"+self.codigo_concurso
