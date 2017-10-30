from django.contrib import admin
from .models import UsuarioApp, Curso, SesionCurso, Asistencia

# Register your models here.
admin.site.register(UsuarioApp)
admin.site.register(Curso)
admin.site.register(SesionCurso)
admin.site.register(Asistencia)
