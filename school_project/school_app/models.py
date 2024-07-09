from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    class_name = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)  # Add this line for gender

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Attendance(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.teacher} - {self.date} - {self.status}"


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student} - {self.subject}"


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title


class Todo(models.Model):
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task
