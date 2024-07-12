from django import forms
from .models import Event, Todo, ClassCleanliness, ClubReport, LogBook, ReadingLog, StaffAttendance, SUPWReport, TeachersSubstitution, TeachersTimetable, TODReport, OrganizationChart, ProfessionalDevelopment, PLCReport

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_time', 'end_time']

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task', 'completed']

class ClassCleanlinessForm(forms.ModelForm):
    class Meta:
        model = ClassCleanliness
        fields = ['date', 'class_name', 'cleanliness_score']

class ClubReportForm(forms.ModelForm):
    class Meta:
        model = ClubReport
        fields = ['date', 'club_name', 'report']

class LogBookForm(forms.ModelForm):
    class Meta:
        model = LogBook
        fields = ['date', 'entry']

class ReadingLogForm(forms.ModelForm):
    class Meta:
        model = ReadingLog
        fields = ['date', 'student_name', 'book_title']

class StaffAttendanceForm(forms.ModelForm):
    class Meta:
        model = StaffAttendance
        fields = ['date', 'teacher_name', 'present']

class SUPWReportForm(forms.ModelForm):
    class Meta:
        model = SUPWReport
        fields = ['date', 'activity_name', 'report']

class TeachersSubstitutionForm(forms.ModelForm):
    class Meta:
        model = TeachersSubstitution
        fields = ['date', 'teacher_name', 'substitute_teacher', 'reason']

class TeachersTimetableForm(forms.ModelForm):
    class Meta:
        model = TeachersTimetable
        fields = ['date', 'teacher_name', 'timetable']

class TODReportForm(forms.ModelForm):
    class Meta:
        model = TODReport
        fields = ['date', 'report_details']

class OrganizationChartForm(forms.ModelForm):
    class Meta:
        model = OrganizationChart
        fields = ['date', 'chart']

class ProfessionalDevelopmentForm(forms.ModelForm):
    class Meta:
        model = ProfessionalDevelopment
        fields = ['date', 'activity_name', 'details']

class PLCReportForm(forms.ModelForm):
    class Meta:
        model = PLCReport
        fields = ['date', 'report']
