from django.core.management.base import BaseCommand
from school_app.models import Student, Teacher, Event, Todo


class Command(BaseCommand):
    help = 'Clears all data from the database'

    def handle(self, *args, **kwargs):
        Student.objects.all().delete()
        Teacher.objects.all().delete()
        Event.objects.all().delete()
        Todo.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(
            'Successfully cleared the database.'))
