#!/usr/bin/env python
"""
Script de testare pentru modelele aplicației university
"""
import os
import django
from datetime import date, timedelta

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_database_project.settings')
django.setup()

from university.models import Student, Professor, Semester, Course, StudentIDCard, CourseDescription

def test_models():
    print("\n" + "="*60)
    print("TESTARE MODELE DJANGO - APLICAȚIA UNIVERSITY")
    print("="*60 + "\n")
    
    # Test 1: Creare Student
    print("📝 Test 1: Creare Student...")
    student = Student.objects.create(
        first_name="Ion",
        last_name="Popescu",
        email="ion.popescu@student.md",
        enrollment_date=date.today()
    )
    print(f"✅ Student creat: {student}")
    
    # Test 2: Creare StudentIDCard
    print("\n📝 Test 2: Creare StudentIDCard...")
    id_card = StudentIDCard.objects.create(
        student=student,
        card_number="STU2026001",
        issue_date=date.today(),
        expiry_date=date.today() + timedelta(days=1825)  # 5 ani
    )
    print(f"✅ ID Card creat: {id_card}")
    
    # Test 3: Creare Professor
    print("\n📝 Test 3: Creare Professor...")
    professor = Professor.objects.create(
        first_name="Maria",
        last_name="Ionescu",
        email="maria.ionescu@university.md",
        department="Informatică"
    )
    print(f"✅ Profesor creat: {professor}")
    
    # Test 4: Creare Semester
    print("\n📝 Test 4: Creare Semester...")
    semester = Semester.objects.create(
        name="Semestrul I 2026",
        start_date=date(2026, 9, 1),
        end_date=date(2027, 1, 31)
    )
    print(f"✅ Semestru creat: {semester}")
    
    # Test 5: Creare Course
    print("\n📝 Test 5: Creare Course...")
    course = Course.objects.create(
        name="Baze de Date",
        code="BD101",
        professor=professor,
        semester=semester
    )
    # Adăugare student la curs
    course.students.add(student)
    print(f"✅ Curs creat: {course}")
    print(f"   Studenți înscriși: {course.students.count()}")
    
    # Test 6: Creare CourseDescription
    print("\n📝 Test 6: Creare CourseDescription...")
    description = CourseDescription.objects.create(
        course=course,
        content="Curs despre baze de date relaționale și SQL",
        objectives="Înțelegerea conceptelor de baze de date",
        prerequisites="Programare I, II"
    )
    print(f"✅ Descriere curs creată: {description}")
    
    # Test 7: Verificare relații
    print("\n📝 Test 7: Verificare relații...")
    print(f"   Student {student.first_name} are ID Card: {student.id_card.card_number}")
    print(f"   Profesorul {professor.first_name} predă {professor.courses.count()} curs(uri)")
    print(f"   Studentul {student.first_name} este înscris la {student.courses.count()} curs(uri)")
    print(f"   Cursul {course.code} are {course.students.count()} student(i)")
    
    # Test 8: Statistici
    print("\n📊 STATISTICI FINALE:")
    print(f"   Total studenți: {Student.objects.count()}")
    print(f"   Total profesori: {Professor.objects.count()}")
    print(f"   Total cursuri: {Course.objects.count()}")
    print(f"   Total semestre: {Semester.objects.count()}")
    print(f"   Total ID Cards: {StudentIDCard.objects.count()}")
    print(f"   Total descrieri cursuri: {CourseDescription.objects.count()}")
    
    print("\n" + "="*60)
    print("✅ TOATE TESTELE AU FOST FINALIZATE CU SUCCES!")
    print("="*60 + "\n")
    
    # Cleanup (șterge datele de test)
    print("🧹 Șterg datele de test...")
    Student.objects.all().delete()
    Professor.objects.all().delete()
    Semester.objects.all().delete()
    Course.objects.all().delete()
    print("✅ Date de test șterse!\n")

if __name__ == "__main__":
    test_models()
