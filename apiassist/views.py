from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from .models import UsuarioApp, Curso, SesionCurso, Asistencia
from .serializers import UsuarioAppSerializer, CursoSerializer, SessionCursoSerializer, AsistenciaSerializer

# Create your views here.
class UsuarioAppView(generics.ListAPIView):
    serializer_class = UsuarioAppSerializer
    def get_queryset(self):
        queryset = UsuarioApp.objects.all()
        user = self.request.query_params.get('user', None)
        passw=self.request.query_params.get('passw', None)
        if user is not None:
            queryset = queryset.filter(username=user)
            queryset = queryset.filter(password=passw)
        return queryset

    def post(self, request):
        serializer = UsuarioAppSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS)


class CursoView(generics.ListAPIView):
    serializer_class = CursoSerializer
    def get_queryset(self):
            queryset = Curso.objects.all()
            owner = self.request.query_params.get('ownr', None)
            if owner is not None:
                queryset = queryset.filter(owner=ownr)
            return queryset


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
            serializer.save();
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

class AsistenciaViewByUser(generics.ListAPIView):
    serializer_class = AsistenciaSerializer
    def get_queryset(self):
            queryset = Asistencia.objects.all()
            user = self.request.query_params.get('usr', None)
            if user is not None:
                queryset = queryset.filter(estudiante=user)
            return queryset

class AsistenciaViewByCourse(generics.ListAPIView):
    serializer_class = AsistenciaSerializer
    def get_queryset(self):
            queryset = Asistencia.objects.all()
            curso = self.request.query_params.get('curso', None)
            if curso is not None:
                queryset = queryset.filter(curso=curso)
            return queryset

class AsistenciaViewBySession(generics.ListAPIView):
    serializer_class = AsistenciaSerializer
    def get_queryset(self):
            queryset = Asistencia.objects.all()
            session = self.request.query_params.get('session', None)
            if session is not None:
                queryset = queryset.filter(session=session)
            return queryset
