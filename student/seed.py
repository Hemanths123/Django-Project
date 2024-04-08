from faker import Faker
fake = Faker()
from .models import *

import random

def seed_db(n=10) -> None:
    try:
        for _ in range(0, n):
            department_objs = Department.objects.all()
            random_index = random.randint(0, len(department_objs)-1)
            department = department_objs[random_index]
            student_id = f'STU-{random.randint(100, 999)}'
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(18, 100)
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(student_id=student_id)

            student_obj = Student.objects.create(student_name=student_name,
                                                department=department, 
                                                student_email=student_email, 
                                                student_age=student_age,
                                                student_address=student_address,
                                                student_id=student_id_obj)
    except Exception as e:
        print(e)


def create_subject_marks():
    try:
        student_objs = Student.objects.all()
        for student in student_objs:
            subject_obj = Subject.objects.all()
            for subject in subject_obj:
                SubjectMarks.objects.create(student=student,
                                            subject=subject,
                                            marks=random.randint(0,100))
    except Exception as e:
        print(e)
    
