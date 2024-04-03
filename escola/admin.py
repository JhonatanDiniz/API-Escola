from django.contrib import admin
from escola.models import Aluno, Curso, Matricula

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('nome',)
    search_fields = ('nome', 'cpf')
admin.site.register(Aluno, AlunoAdmin)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('codigo_curso', 'descricao', 'nivel')
    list_display_links = ('codigo_curso',)
    search_fields =('codigo_curso', 'descricao',)
admin.site.register(Curso,CursoAdmin)

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('periodo', 'aluno', 'curso')
    list_display_links = ('periodo',)
admin.site.register(Matricula,MatriculaAdmin)
