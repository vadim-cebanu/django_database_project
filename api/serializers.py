from rest_framework import serializers
from university.models import Student, Professor, Semester, Course, StudentIDCard, CourseDescription


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class StudentIDCardSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.__str__', read_only=True)
    
    class Meta:
        model = StudentIDCard
        fields = '__all__'


class ProfessorSerializer(serializers.ModelSerializer):
    courses_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Professor
        fields = '__all__'
    
    def get_courses_count(self, obj):
        return obj.courses.count()


class SemesterSerializer(serializers.ModelSerializer):
    courses_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Semester
        fields = '__all__'
    
    def get_courses_count(self, obj):
        return obj.courses.count()


class CourseSerializer(serializers.ModelSerializer):
    professor_name = serializers.CharField(source='professor.__str__', read_only=True)
    semester_name = serializers.CharField(source='semester.name', read_only=True)
    students_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Course
        fields = '__all__'
    
    def get_students_count(self, obj):
        return obj.students.count()


class CourseDescriptionSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course.__str__', read_only=True)
    
    class Meta:
        model = CourseDescription
        fields = '__all__'


