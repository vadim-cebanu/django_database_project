from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from datetime import datetime
from django_filters.rest_framework import DjangoFilterBackend

from university.models import Student, Professor, Semester, Course, StudentIDCard, CourseDescription
from .serializers import (
    StudentSerializer, ProfessorSerializer, SemesterSerializer,
    CourseSerializer, StudentIDCardSerializer, CourseDescriptionSerializer,
)


class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'email']
    ordering_fields = ['enrollment_date', 'last_name']


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'email', 'department']
    ordering_fields = ['last_name', 'department']


class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['start_date', 'end_date']
    ordering = ['-start_date']


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().select_related('professor', 'semester')
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'code']
    ordering_fields = ['code', 'name']
    filterset_fields = ['professor', 'semester']


class StudentIDCardViewSet(viewsets.ModelViewSet):
    queryset = StudentIDCard.objects.all().select_related('student')
    serializer_class = StudentIDCardSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['card_number', 'student__first_name', 'student__last_name']


class CourseDescriptionViewSet(viewsets.ModelViewSet):
    queryset = CourseDescription.objects.all().select_related('course')
    serializer_class = CourseDescriptionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['course__name', 'course__code', 'objectives']


 