from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from escola.views import AlunoViewSet, CursoViewSet

router = routers.DefaultRouter()
router.register('alunos', AlunoViewSet, basename='alunos')
router.register('cursos', CursoViewSet, basename='cursos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
