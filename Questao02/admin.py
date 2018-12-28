

from django.contrib import admin
from .models import Curso,Turma,Professor


class AdminTurma(admin.TabularInline):
    model = Turma
    extra = 1


class ProfessorAdmin(admin.ModelAdmin):
    inlines = [AdminTurma]






admin.site.register(Curso)
admin.site.register(Turma)
admin.site.register(Professor,ProfessorAdmin)
