from django.db import models

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

class ClassCleanliness(models.Model):
    date = models.DateField()
    class_name = models.CharField(max_length=100)
    cleanliness_score = models.IntegerField()

    def __str__(self):
        return f"{self.class_name} - {self.date}"

class ClubReport(models.Model):
    date = models.DateField()
    club_name = models.CharField(max_length=100)
    report = models.TextField()

    def __str__(self):
        return f"{self.club_name} - {self.date}"

class LogBook(models.Model):
    date = models.DateField()
    entry = models.TextField()

    def __str__(self):
        return f"LogBook Entry - {self.date}"

class ReadingLog(models.Model):
    date = models.DateField()
    student_name = models.CharField(max_length=100)
    book_title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.student_name} - {self.book_title}"

class StaffAttendance(models.Model):
    date = models.DateField()
    teacher_name = models.CharField(max_length=100)
    present = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.teacher_name} - {self.date}"

class SUPWReport(models.Model):
    date = models.DateField()
    activity_name = models.CharField(max_length=100)
    report = models.TextField()

    def __str__(self):
        return f"{self.activity_name} - {self.date}"

class TeachersSubstitution(models.Model):
    date = models.DateField()
    teacher_name = models.CharField(max_length=100)
    substitute_teacher = models.CharField(max_length=100)
    reason = models.TextField()

    def __str__(self):
        return f"{self.teacher_name} - {self.date}"

class TeachersTimetable(models.Model):
    date = models.DateField()
    teacher_name = models.CharField(max_length=100)
    timetable = models.TextField()

    def __str__(self):
        return f"{self.teacher_name} - {self.date}"

class TODReport(models.Model):
    date = models.DateField()
    report_details = models.TextField()

    def __str__(self):
        return f"TOD Report - {self.date}"

class OrganizationChart(models.Model):
    date = models.DateField()
    chart = models.TextField()

    def __str__(self):
        return f"Organization Chart - {self.date}"

class ProfessionalDevelopment(models.Model):
    date = models.DateField()
    activity_name = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return f"{self.activity_name} - {self.date}"

class PLCReport(models.Model):
    date = models.DateField()
    report = models.TextField()

    def __str__(self):
        return f"PLC Report - {self.date}"
