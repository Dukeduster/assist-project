from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import UsuarioApp, Curso, SesionCurso, Asistencia
from .serializers import UsuarioAppSerializer, CursoSerializer, SessionCursoSerializer, AsistenciaSerializer

# Create your views here.
class UsuarioAppView(APIView):
    
def get(self,request):
		usuario=UsuarioApp.objects.filter(username=self.request.user)
        return Response(usuario)

def post(self, request):
		serializer=UsuarioAppSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS)


class CursoView(APIView):
def post(self, request):
		serializer=CursoSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS)

class SesionCursoView(APIView):
def post(self, request):
		serializer=SessionCursoSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS)

class AsistenciaView(APIView):

def post(self, request):
		serializer=AsistenciaSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS)
