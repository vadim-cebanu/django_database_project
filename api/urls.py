from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    StudentViewSet, ProfessorViewSet, 
    SemesterViewSet, CourseViewSet, StudentIDCardViewSet,
    CourseDescriptionViewSet
)

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')
router.register(r'professors', ProfessorViewSet, basename='professor')
router.register(r'semesters', SemesterViewSet, basename='semester')
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'id-cards', StudentIDCardViewSet, basename='id-card')
router.register(r'course-descriptions', CourseDescriptionViewSet, basename='course-description')

urlpatterns = [
    path('', include(router.urls)),
]
