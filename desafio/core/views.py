from rest_framework import viewsets
from .models import *
from .serializers import *

class ProfissaoViewSet(viewsets.ModelViewSet):
    
    queryset = Profissao.objects.all().order_by('nome')
    serializer_class = ProfissaoSerializer
class CandidatoViewSet(viewsets.ModelViewSet):
    
    queryset = Candidato.objects.all().order_by('nome')
    serializer_class = CandidatoSerializer
    
class ConcursoViewSet(viewsets.ModelViewSet):
    
    queryset = Concurso.objects.all().order_by('edital')
    serializer_class = ConcursoSerializer

class OrgaoViewSet(viewsets.ModelViewSet):
    
    queryset = Orgao.objects.all().order_by('nome')
    serializer_class = OrgaoSerializer