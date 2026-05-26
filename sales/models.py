from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    email = models.EmailField(unique=True, verbose_name="Email")
    enrollment_date = models.DateField(verbose_name="Enrollment Date")
    
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class StudentIDCard(models.Model):
    """Model for student ID cards - One-to-One relationship with Student"""
    student = models.OneToOneField(Student,on_delete=models.CASCADE,related_name='id_card',verbose_name="Student")
    card_number = models.CharField(max_length=20, unique=True, verbose_name="Card Number")
    issue_date = models.DateField(verbose_name="Issue Date")
    expiry_date = models.DateField(verbose_name="Expiry Date")
    
    class Meta:
        verbose_name = "Student ID Card"
        verbose_name_plural = "Student ID Cards"
    
    def __str__(self):
        return f"Student ID Card {self.card_number} - {self.student}"


class Professor(models.Model):
    """Model for professors"""
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    email = models.EmailField(unique=True, verbose_name="Email")
    department = models.CharField(max_length=200, verbose_name="Department")
    
    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professors"
    
    def __str__(self):
        return f"Prof. {self.first_name} {self.last_name}"


class Semester(models.Model):
    name = models.CharField(max_length=100,unique=True,verbose_name="Semester Name",help_text="Ex: Summer Semester 2025")
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date")
    
    class Meta:
        verbose_name = "Semester"
        verbose_name_plural = "Semesters"
        ordering = ['-start_date']
    
    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200, verbose_name="Course Name")
    code = models.CharField(max_length=20, unique=True, default="", verbose_name="Course Code")    
    professor = models.ForeignKey(Professor,on_delete=models.CASCADE,related_name='courses',verbose_name="Professor")
    semester = models.ForeignKey(Semester,on_delete=models.CASCADE,related_name='courses',verbose_name="Semester")
    students = models.ManyToManyField(Student,related_name='courses',verbose_name="Enrolled Students",blank=True)
    
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
    
    def __str__(self):
        return f"{self.code} - {self.name}"


class CourseDescription(models.Model):
    course = models.OneToOneField(Course,on_delete=models.CASCADE,related_name='description',verbose_name="Course")
    content = models.TextField(verbose_name="Content")
    objectives = models.TextField(verbose_name="Objectives")
    prerequisites = models.TextField(blank=True, verbose_name="Prerequisites")
    
    class Meta:
        verbose_name = "Course Description"
        verbose_name_plural = "Course Descriptions"
    
    def __str__(self):
        return f"Description for {self.course.name}"