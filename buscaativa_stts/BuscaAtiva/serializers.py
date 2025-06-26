from rest_framework import serializers
from busca_ativa.models import BuscaAtiva
from alunos.serializers import AlunoSerializer

class BuscaAtivaSerializer(serializers.ModelSerializer):
    turma_display = serializers.CharField(
        source='get_turma_display',
        read_only=True,
        label="Turma (Descrição)"
    )
    
    class Meta:
        model = BuscaAtiva
        fields = [
            'id', 'discente', 'data', 'turma', 'turma_display',
            'numero', 'email', 'endereco', 'justificativa'
        ]
        extra_kwargs = {
            'turma': {'required': True},
        }