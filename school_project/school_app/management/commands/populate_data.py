from django.core.management.base import BaseCommand
from school_app.models import Student, Teacher, Event, Todo


class Command(BaseCommand):
    help = 'Populate initial data into the database'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Student.objects.all().delete()
        Teacher.objects.all().delete()
        Event.objects.all().delete()
        Todo.objects.all().delete()

        # Create sample teachers
        teachers = [
            {'first_name': 'John', 'last_name': 'Doe',
                'email': 'john.doe@example.com', 'subject': 'Math'},
            {'first_name': 'Jane', 'last_name': 'Smith',
                'email': 'jane.smith@example.com', 'subject': 'Science'}
        ]
        for teacher in teachers:
            Teacher.objects.create(**teacher)

        # Create sample students
        students = [
            {'first_name': 'Alice', 'last_name': 'Johnson',
                'email': 'alice.johnson@example.com', 'class_name': '5A', 'gender': 'Female'},
            {'first_name': 'Bob', 'last_name': 'Brown',
                'email': 'bob.brown@example.com', 'class_name': '5A', 'gender': 'Male'},
            {'first_name': 'Charlie', 'last_name': 'Davis',
                'email': 'charlie.davis@example.com', 'class_name': '5B', 'gender': 'Male'},
            {'first_name': 'Diana', 'last_name': 'Evans',
                'email': 'diana.evans@example.com', 'class_name': '5B', 'gender': 'Female'}
        ]
        for student in students:
            Student.objects.create(**student)

        # Create sample events
        events = [
            {'title': 'School Annual Day', 'description': 'Annual day celebration.',
                'start_time': '2024-09-25 10:00:00', 'end_time': '2024-09-25 14:00:00'},
            {'title': 'Science Fair', 'description': 'Annual science fair.',
                'start_time': '2024-10-15 09:00:00', 'end_time': '2024-10-15 12:00:00'}
        ]
        for event in events:
            Event.objects.create(**event)

        # Create sample todos
        todos = [
            {'task': 'Prepare for annual day', 'completed': False},
            {'task': 'Science fair presentation', 'completed': True}
        ]
        for todo in todos:
            Todo.objects.create(**todo)

        self.stdout.write(self.style.SUCCESS(
            'Successfully populated the database with initial data.'))
