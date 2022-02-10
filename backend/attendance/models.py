from django.db import models
from django.contrib.auth.models import User

CLASS_CHOICES = [
    ('CREC', 'Creche'),
    # ()
    ('PRIM1', 'Primary 1'),
    ('PRIM2', 'Primary 2'),
    ('PRIM3', 'Primary 3'),
    ('PRIM4', 'Primary 4'),
    ('PRIM5', 'Primary 5'),
    ('PRIM6', 'Primary 6'),
    ('JHS1', 'JHS 1'),
    ('JHS2', 'JHS 2'),
    ('JHS3', 'JHS 3'),
]

# Same as class. Choose level because of class is reserved keyword
# class Level(models.Model):
#     name = models.CharField(max_length=5, choices=CLASS_CHOICES)
#     # classroom = models.


class Subject(models.Model):
    subject_name = models.CharField(max_length=100)


class Student(models.Model):
    first_name = models.CharField(max_length= 36)
    last_name = models.CharField(max_length= 36)
    level = models.CharField(max_length=5, choices=CLASS_CHOICES)

class Attendance(models.Model):
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=False)
    leave = models.BooleanField(default=False)   
    offday = models.BooleanField(default=False)
    remarks = models.TextField(max_length=100)

class StudentAcademics(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    year = models.DateField()
    score = models.IntegerField()
    attitude_remark = models.TextField(max_length=100)