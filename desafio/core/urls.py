from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'profissoes', ProfissaoViewSet)
router.register(r'candidatos', CandidatoViewSet)
router.register(r'concursos', ConcursoViewSet)
router.register(r'orgaos', OrgaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]