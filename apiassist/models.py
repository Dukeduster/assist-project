from django.db import models

# Create your models here.

class UsuarioApp(models.Model):
	id=models.AutoField(primary_key=True)
	username=models.CharField(max_length=50)
	password=models.CharField(max_length=50)
	rol=models.CharField(max_length=12)
	def __str__(self):
		return self.id

class Curso(models.Model):
	id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=50)
	owner=models.ForeignKey('UsuarioApp', on_delete=models.CASCADE)
	fechaCreacion=models.DateTimeField(auto_now_add=True)
	habilitado=models.BooleanField(default=True)
	def __str__(self):
		return self.id

class SesionCurso(models.Model):
	id=models.AutoField(primary_key=True)
	fechaSesion=models.DateTimeField(null=False)
	name=models.CharField(max_length=50)
	qrCode=models.CharField(max_length=100)
	curso=models.ForeignKey('Curso', on_delete=models.CASCADE)
	def __str__(self):
		return self.id

class Asistencia(models.Model):
	id=models.AutoField(primary_key=True)
	fechaAsistencia=models.DateTimeField(null=False)
	curso=models.ForeignKey('Curso', on_delete=models.CASCADE)
	sesion=models.ForeignKey('SesionCurso', on_delete=models.CASCADE)
	estudiante=models.ForeignKey('UsuarioApp', on_delete=models.CASCADE)
	def __str__(self):
		return self.id
