from rest_framework import serializers
from .models import UsuarioApp
from .models import Curso
from .models import SesionCurso
from .models import Asistencia


class UsuarioAppSerializer(serializers.ModelSerializer):
    class Meta:
        model=UsuarioApp
        fields=('id','username','password','rol')

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Curso
        fields=('id','name','owner','fechaCreacion', 'habilitado')

class SessionCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model=SesionCurso
        fields=('id','fechaSesion','name','qrCode', 'curso')

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Asistencia
        fields=('id','fechaAsistencia','curso','asistencia', 'estudiante')