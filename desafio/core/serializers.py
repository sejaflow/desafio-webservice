from rest_framework import serializers
from .models import *

class ProfissaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profissao
        fields = '__all__'

class ConcursoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Concurso
        fields = '__all__'

class OrgaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orgao
        fields = '__all__'

class CandidatoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Candidato
        fields = '__all__'
