from django.contrib import admin

from .models import revista,caixa,coleçao,emprestimo,Amigo

class AdminRevista(admin.TabularInline):
    model = revista
    extra = 1

class AdminColeçao(admin.ModelAdmin):
    inlines = [AdminRevista]

class AdminAmigo(admin.TabularInline):
    model = Amigo
    extra = 1

class AdminEmprestimo(admin.ModelAdmin):
    inlines = [AdminAmigo]
admin.site.register(revista)
admin.site.register(caixa)
admin.site.register(coleçao,AdminColeçao)
admin.site.register(emprestimo,AdminEmprestimo)
admin.site.register(Amigo)