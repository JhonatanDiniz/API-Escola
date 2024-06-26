from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    nome_aluno = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno', 'nome_aluno', 'curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()

class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    nome_aluno = serializers.ReadOnlyField(source='aluno.nome')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['aluno', 'nome_aluno', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()