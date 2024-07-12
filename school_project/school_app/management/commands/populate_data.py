# school_app/management/commands/populate_db.py

from django.core.management.base import BaseCommand
from school_app.models import Student, Teacher, Attendance, Result, Event, Todo, ClassCleanliness, ClubReport, LogBook, ReadingLog, StaffAttendance, SUPWReport, TeachersSubstitution, TeachersTimetable, TODReport, OrganizationChart, ProfessionalDevelopment, PLCReport
import random
from datetime import date, datetime, timedelta

class Command(BaseCommand):
    help = 'Populates the database with Bhutanese details'

    def handle(self, *args, **kwargs):
        # Clear existing data
        self.clear_data()

        # Populate Students
        students = [
            ('Pema', 'Dorji', 'pema.dorji@example.com', '10A', 'Male'),
            ('Sonam', 'Choden', 'sonam.choden@example.com', '10B', 'Female'),
            ('Jigme', 'Wangchuk', 'jigme.wangchuk@example.com', '9A', 'Male'),
        ]

        for first_name, last_name, email, class_name, gender in students:
            Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                class_name=class_name,
                gender=gender,
            )

        # Populate Teachers
        teachers = [
            ('Karma', 'Wangdi', 'karma.wangdi@example.com', 'Mathematics'),
            ('Tshering', 'Yangzom', 'tshering.yangzom@example.com', 'Science'),
            ('Dawa', 'Tshering', 'dawa.tshering@example.com', 'English'),
        ]

        for first_name, last_name, email, subject in teachers:
            Teacher.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                subject=subject,
            )

        # Populate Attendance
        for teacher in Teacher.objects.all():
            for i in range(10):  # 10 random attendance records
                Attendance.objects.create(
                    teacher=teacher,
                    date=date.today() - timedelta(days=i),
                    status=random.choice(['Present', 'Absent']),
                )

        # Populate Results
        for student in Student.objects.all():
            for subject in ['Mathematics', 'Science', 'English']:
                Result.objects.create(
                    student=student,
                    subject=subject,
                    marks=random.randint(40, 100),
                )

        # Populate Events
        Event.objects.create(
            title='Annual Sports Day',
            description='A day full of sports activities and competitions.',
            start_time=datetime.now() + timedelta(days=5),
            end_time=datetime.now() + timedelta(days=5, hours=6),
        )

        # Populate Todos
        todos = ['Prepare for exam', 'Complete homework', 'Attend meeting']
        for task in todos:
            Todo.objects.create(
                task=task,
                completed=random.choice([True, False]),
            )

        # Populate Class Cleanliness
        for class_name in ['10A', '10B', '9A']:
            for i in range(5):  # 5 records per class
                ClassCleanliness.objects.create(
                    date=date.today() - timedelta(days=i),
                    class_name=class_name,
                    cleanliness_score=random.randint(1, 10),
                )

        # Populate Club Reports
        clubs = ['Science Club', 'Literary Club', 'Sports Club']
        for club_name in clubs:
            ClubReport.objects.create(
                date=date.today(),
                club_name=club_name,
                report=f'{club_name} had a successful event today.',
            )

        # Populate Log Book
        for i in range(10):  # 10 log book entries
            LogBook.objects.create(
                date=date.today() - timedelta(days=i),
                entry=f'Today was a productive day {i}.',
            )

        # Populate Reading Log
        for student in Student.objects.all():
            ReadingLog.objects.create(
                date=date.today(),
                student_name=f'{student.first_name} {student.last_name}',
                book_title=f'Book {random.randint(1, 10)}',
            )

        # Populate Staff Attendance
        for teacher in Teacher.objects.all():
            StaffAttendance.objects.create(
                date=date.today(),
                teacher_name=f'{teacher.first_name} {teacher.last_name}',
                present=random.choice([True, False]),
            )

        # Populate SUPW Reports
        SUPWReport.objects.create(
            date=date.today(),
            activity_name='Community Service',
            report='Students participated in community service activities.'
        )

        # Populate Teachers Substitution
        TeachersSubstitution.objects.create(
            date=date.today(),
            teacher_name='Karma Wangdi',
            substitute_teacher='Dawa Tshering',
            reason='Medical Leave',
        )

        # Populate Teachers Timetable
        TeachersTimetable.objects.create(
            date=date.today(),
            teacher_name='Tshering Yangzom',
            timetable='9:00 AM - 10:00 AM: Science, 10:15 AM - 11:15 AM: Physics'
        )

        # Populate TOD Reports
        TODReport.objects.create(
            date=date.today(),
            report_details='Teacher on duty report for today.'
        )

        # Populate Organization Chart
        OrganizationChart.objects.create(
            date=date.today(),
            chart='Organization chart details here.'
        )

        # Populate Professional Development
        ProfessionalDevelopment.objects.create(
            date=date.today(),
            activity_name='Workshop on Teaching Methods',
            details='Details about the workshop on teaching methods.'
        )

        # Populate PLC Reports
        PLCReport.objects.create(
            date=date.today(),
            report='PLC meeting report details here.'
        )

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))

    def clear_data(self):
        models = [Student, Teacher, Attendance, Result, Event, Todo, ClassCleanliness, ClubReport, LogBook, ReadingLog, StaffAttendance, SUPWReport, TeachersSubstitution, TeachersTimetable, TODReport, OrganizationChart, ProfessionalDevelopment, PLCReport]
        for model in models:
            model.objects.all().delete()
