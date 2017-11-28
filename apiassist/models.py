from django.db import models

# Create your models here.

class UsuarioApp(models.Model):
	id=models.AutoField(primary_key=True)
	username=models.CharField(max_length=50)
	password=models.CharField(max_length=50)
	name=models.CharField(max_length=50)
	lastname=models.CharField(max_length=50)
	cedula=models.CharField(max_length=50)
	rol=models.CharField(max_length=12)
	def __str__(self):
		return str(self.username)

class Curso(models.Model):
	id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=50)
	owner=models.ForeignKey('UsuarioApp', on_delete=models.CASCADE)
	fechaCreacion=models.DateTimeField(auto_now_add=True)
	habilitado=models.BooleanField(default=True)
	descripcion=models.CharField(max_length=100, blank=True, null=True)
	fechaExpiracion=models.DateTimeField(blank=True,null=True)
	def __str__(self):
		return str(self.name)

class SesionCurso(models.Model):
	id=models.CharField(max_length=50, primary_key=True)
	fechaSesion=models.DateTimeField(null=False)
	name=models.CharField(max_length=50)
	curso=models.ForeignKey('Curso', on_delete=models.CASCADE)
	descripcion=models.CharField(max_length=50, blank=True, null=True)
	def __str__(self):
		return str(self.name)

class Asistencia(models.Model):
	id=models.AutoField(primary_key=True)
	fechaAsistencia=models.DateTimeField(null=False)
	fechaReporte=models.DateTimeField(auto_now_add=True)
	sesion=models.ForeignKey('SesionCurso', on_delete=models.CASCADE)
	estudiante=models.ForeignKey('UsuarioApp', on_delete=models.CASCADE)
	latitud=models.DecimalField(max_digits=9, decimal_places=6)
	longitud=models.DecimalField(max_digits=9, decimal_places=6)
	def __str__(self):
		return str(self.fechaAsistencia)
