from django.db import models
#from alunos.models import Aluno

# Opções de turma pré-definidas
TURMA_CHOICES = [
    ('ADM1', 'Administração / 1° ano'),
    ('ADM2', 'Administração / 2° ano'),
    ('ADM3', 'Administração / 3° ano'),
    ('INFO1', 'Informática / 1° ano'),
    ('INFO2', 'Informática / 2° ano'),
    ('INFO3', 'Informática / 3° ano'),
]

class BuscaAtiva(models.Model):
    discente = models.ForeignKey(
        #Aluno,
        on_delete=models.CASCADE,
        verbose_name="Aluno"
    )
    data = models.DateField(auto_now_add=True, verbose_name="Data da Busca")
    turma = models.CharField(
        max_length=10,
        choices=TURMA_CHOICES,
        verbose_name="Turma"
    )
    numero = models.CharField(max_length=20, verbose_name="Número de Contato")
    email = models.EmailField(verbose_name="E-mail")
    endereco = models.TextField(verbose_name="Endereço Completo")
    justificativa = models.TextField(verbose_name="Justificativa da Busca")

    def __str__(self):
        return f"Busca de {self.discente.nome} (Turma: {self.get_turma_display()})"

    class Meta:
        verbose_name = "Busca Ativa"
        verbose_name_plural = "Buscas Ativas"