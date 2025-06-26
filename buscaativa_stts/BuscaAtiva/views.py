from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from busca_ativa.models import BuscaAtiva
from busca_ativa.serializers import BuscaAtivaSerializer

class BuscaAtivaAPIView(APIView):
    # Listar todas as buscas ativas (GET)
    def get(self, request):
        buscas = BuscaAtiva.objects.all()
        serializer = BuscaAtivaSerializer(buscas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Criar nova busca ativa (POST)
    def post(self, request):
        serializer = BuscaAtivaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BuscarAlunoView(APIView):
    # Buscar aluno por matrícula e retornar dados para autopreenchimento (GET)
    def get(self, request, matricula):
        try:
            aluno = Aluno.objects.get(matricula=matricula)
            return Response({
                'nome': aluno.nome,
                'email': aluno.email,
                'telefone': aluno.telefone,
                'endereco': f"{aluno.endereco.logradouro}, {aluno.endereco.numero}" if hasattr(aluno, 'endereco') else '',
                'turma_sugerida': aluno.turma if hasattr(aluno, 'turma') else None  # Se o aluno já tiver turma cadastrada
            }, status=status.HTTP_200_OK)
        except Aluno.DoesNotExist:
            return Response(
                {"erro": "Aluno não encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )