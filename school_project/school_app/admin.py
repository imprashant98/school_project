from django.contrib import admin
from .models import Student, Teacher, Result, Event, Todo

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Result)
admin.site.register(Event)
admin.site.register(Todo)
