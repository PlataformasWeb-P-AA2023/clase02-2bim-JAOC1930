from django.contrib import admin

# Register your models here.

from miapp.models import Estudiante, Pais

class EstudianteAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str)
    # de la clase
    list_display = ('nombre', 'apellido', 'cedula', 'edad', 'tipo_estudiante')
    search_fields = ('nombre', 'cedula', 'apellido')

class PaisAdmin(admin.ModelAdmin):

    list_display = ('id','nombre', 'capital')
    search_fields = ('id', 'nombre', 'capital')


admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Pais, PaisAdmin)