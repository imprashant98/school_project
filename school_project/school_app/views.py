import json
from .forms import EventForm, TodoForm
from .models import Student, Teacher, Event, Todo, Attendance
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
import matplotlib
matplotlib.use('Agg')
from .models import ClassCleanliness, ClubReport, LogBook, ReadingLog, StaffAttendance
from .forms import ClassCleanlinessForm, ClubReportForm, LogBookForm, ReadingLogForm, StaffAttendanceForm, SUPWReportForm, TeachersSubstitutionForm, TeachersTimetableForm, TODReportForm, OrganizationChartForm, ProfessionalDevelopmentForm, PLCReportForm
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .forms import ClassCleanlinessForm, ClubReportForm, LogBookForm, ReadingLogForm, StaffAttendanceForm, SUPWReportForm, TeachersSubstitutionForm, TeachersTimetableForm, TODReportForm, OrganizationChartForm, ProfessionalDevelopmentForm, PLCReportForm
from .models import ClassCleanliness, ClubReport, LogBook, ReadingLog, StaffAttendance, SUPWReport, TeachersSubstitution, TeachersTimetable, TODReport, OrganizationChart, ProfessionalDevelopment, PLCReport




def about_view(request):
    return render(request, 'school_app/about.html')


def dashboard_view(request):
    events = Event.objects.all()
    todos = Todo.objects.all()

    # Calculate student data
    boys_count = Student.objects.filter(gender='Male').count()
    girls_count = Student.objects.filter(gender='Female').count()

    if boys_count == 0 and girls_count == 0:
        boys_count = 50  # Hardcoded dummy value
        girls_count = 50  # Hardcoded dummy value

    students_data = {
        'boys': boys_count,
        'girls': girls_count,
    }

    # Calculate teacher data
    teachers_count = Teacher.objects.count()

    if teachers_count == 0:
        teachers_count = 20  # Hardcoded dummy value

    teachers_data = {
        'total': teachers_count,
    }

    context = {
        'events': events,
        'todos': todos,
        'students_data': json.dumps(students_data),
        'teachers_data': json.dumps(teachers_data),
    }
    return render(request, 'school_app/dashboard.html', context)


def calendar_view(request):
    events = Event.objects.all()
    return render(request, 'school_app/calendar.html', {'events': events})


def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EventForm()
    return render(request, 'school_app/add_event.html', {'form': form})


def view_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'school_app/view_event.html', {'event': event})


def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'school_app/todo_list.html', {'todos': todos})


def add_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TodoForm()
    return render(request, 'school_app/add_todo.html', {'form': form})


def mark_completed(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('dashboard')


def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect('dashboard')


def pie_chart_view(request):
    labels = ['Math', 'Science', 'English', 'History']
    sizes = [15, 30, 45, 10]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    explode = (0.1, 0, 0, 0)

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    return HttpResponse(buffer, content_type='image/png')


def edit_attendance_view(request):
    teachers = Teacher.objects.all()
    attendance_records = Attendance.objects.all()
    context = {
        'teachers': teachers,
        'attendance_records': attendance_records,
    }
    return render(request, 'school_app/edit_attendance.html', context)


@csrf_exempt
def update_attendance(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'error'}, status=400)
    data = json.loads(request.body)
    for record in data:
        teacher_id = record.get('teacher_id')
        date = record.get('date')
        status = record.get('status')

        teacher = Teacher.objects.get(id=teacher_id)
        attendance, created = Attendance.objects.get_or_create(
            teacher=teacher, date=date)
        attendance.status = status
        attendance.save()

    return JsonResponse({'status': 'success'})

# ClassCleanliness Views
def class_cleanliness_view(request):
    if request.method == 'POST':
        form = ClassCleanlinessForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ClassCleanlinessForm()
    records = ClassCleanliness.objects.all()
    edit_form = ClassCleanlinessForm()
    return render(request, 'school_app/class_cleanliness.html', {'form': form, 'records': records, 'edit_form': edit_form})

def edit_class_cleanliness(request, pk):
    record = get_object_or_404(ClassCleanliness, pk=pk)
    if request.method == 'POST':
        form = ClassCleanlinessForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': True, 'record': {'date': record.date, 'class_name': record.class_name, 'cleanliness_score': record.cleanliness_score}})

def delete_class_cleanliness(request, pk):
    record = get_object_or_404(ClassCleanliness, pk=pk)
    if request.method == 'POST':
        record.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

# ClubReport Views
def club_report_view(request):
    if request.method == 'POST':
        form = ClubReportForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ClubReportForm()
    records = ClubReport.objects.all()
    edit_form = ClubReportForm()
    return render(request, 'school_app/club_report.html', {'form': form, 'records': records, 'edit_form': edit_form})

def edit_club_report(request, pk):
    record = get_object_or_404(ClubReport, pk=pk)
    if request.method == 'POST':
        form = ClubReportForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': True, 'record': {'date': record.date, 'club_name': record.club_name, 'report': record.report}})

def delete_club_report(request, pk):
    record = get_object_or_404(ClubReport, pk=pk)
    if request.method == 'POST':
        record.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

# LogBook Views
def log_book_view(request):
    if request.method == 'POST':
        form = LogBookForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = LogBookForm()
    records = LogBook.objects.all()
    edit_form = LogBookForm()
    return render(request, 'school_app/log_book.html', {'form': form, 'records': records, 'edit_form': edit_form})

def edit_log_book(request, pk):
    record = get_object_or_404(LogBook, pk=pk)
    if request.method == 'POST':
        form = LogBookForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': True, 'record': {'date': record.date, 'entry': record.entry}})

def delete_log_book(request, pk):
    record = get_object_or_404(LogBook, pk=pk)
    if request.method == 'POST':
        record.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

# ReadingLog Views
def reading_log_view(request):
    if request.method == 'POST':
        form = ReadingLogForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ReadingLogForm()
    records = ReadingLog.objects.all()
    edit_form = ReadingLogForm()
    return render(request, 'school_app/reading_log.html', {'form': form, 'records': records, 'edit_form': edit_form})

def edit_reading_log(request, pk):
    record = get_object_or_404(ReadingLog, pk=pk)
    if request.method == 'POST':
        form = ReadingLogForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': True, 'record': {'date': record.date, 'student_name': record.student_name, 'book_title': record.book_title}})

def delete_reading_log(request, pk):
    record = get_object_or_404(ReadingLog, pk=pk)
    if request.method == 'POST':
        record.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

# StaffAttendance Views
def staff_attendance_view(request):
    if request.method == 'POST':
        form = StaffAttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = StaffAttendanceForm()
    records = StaffAttendance.objects.all()
    edit_form = StaffAttendanceForm()
    return render(request, 'school_app/staff_attendance.html', {'form': form, 'records': records, 'edit_form': edit_form})

def edit_staff_attendance(request, pk):
    record = get_object_or_404(StaffAttendance, pk=pk)
    if request.method == 'POST':
        form = StaffAttendanceForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': True, 'record': {'date': record.date, 'teacher_name': record.teacher_name, 'present': record.present}})

def delete_staff_attendance(request, pk):
    record = get_object_or_404(StaffAttendance, pk=pk)
    if request.method == 'POST':
        record.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

# SUPWReport Views
def supw_report_view(request):
    if request.method == 'POST':
        form = SUPWReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supw_report')
    else:
        form = SUPWReportForm()
    
    records = SUPWReport.objects.all()
    return render(request, 'school_app/supw_report.html', {'form': form, 'records': records})

def edit_supw_report(request, pk):
    report = get_object_or_404(SUPWReport, pk=pk)
    if request.method == 'POST':
        form = SUPWReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('supw_report')
    else:
        form = SUPWReportForm(instance=report)
    return render(request, 'school_app/edit_supw_report.html', {'form': form})

def delete_supw_report(request, pk):
    report = get_object_or_404(SUPWReport, pk=pk)
    if request.method == 'POST':
        report.delete()
        return redirect('supw_report')
    return render(request, 'school_app/delete_supw_report.html', {'report': report})

# TeachersSubstitution Views
def teachers_substitution_view(request):
    if request.method == 'POST':
        form = TeachersSubstitutionForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = TeachersSubstitutionForm()
    records = TeachersSubstitution.objects.all()
    edit_form = TeachersSubstitutionForm()
    return render(request, 'school_app/teachers_substitution.html', {'form': form, 'records': records, 'edit_form': edit_form})

def edit_teachers_substitution(request, pk):
    record = get_object_or_404(TeachersSubstitution, pk=pk)
    if request.method == 'POST':
        form = TeachersSubstitutionForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': True, 'record': {'date': record.date, 'teacher_name': record.teacher_name, 'substitution_details': record.substitution_details}})

def delete_teachers_substitution(request, pk):
    record = get_object_or_404(TeachersSubstitution, pk=pk)
    if request.method == 'POST':
        record.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

# TeachersTimetable Views
def teachers_timetable_view(request):
    if request.method == 'POST':
        form = TeachersTimetableForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = TeachersTimetableForm()
    records = TeachersTimetable.objects.all()
    edit_form = TeachersTimetableForm()
    return render(request, 'school_app/teachers_timetable.html', {'form': form, 'records': records, 'edit_form': edit_form})

def edit_teachers_timetable(request, pk):
    record = get_object_or_404(TeachersTimetable, pk=pk)
    if request.method == 'POST':
        form = TeachersTimetableForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': True, 'record': {'date': record.date, 'teacher_name': record.teacher_name, 'timetable_details': record.timetable_details}})

def delete_teachers_timetable(request, pk):
    record = get_object_or_404(TeachersTimetable, pk=pk)
    if request.method == 'POST':
        record.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

# TODReport Views
def tod_report_view(request):
    if request.method == 'POST':
        form = TODReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tod_report')
    else:
        form = TODReportForm()
    
    records = TODReport.objects.all()
    return render(request, 'school_app/tod_report.html', {'form': form, 'records': records})

def edit_tod_report(request, pk):
    report = get_object_or_404(TODReport, pk=pk)
    if request.method == 'POST':
        form = TODReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('tod_report')
    else:
        form = TODReportForm(instance=report)
    return render(request, 'school_app/edit_tod_report.html', {'form': form})

def delete_tod_report(request, pk):
    report = get_object_or_404(TODReport, pk=pk)
    if request.method == 'POST':
        report.delete()
        return redirect('tod_report')
    return render(request, 'school_app/delete_tod_report.html', {'report': report})

# OrganizationChart Views
def organization_chart_view(request):
    if request.method == 'POST':
        form = OrganizationChartForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = OrganizationChartForm()
    records = OrganizationChart.objects.all()
    edit_form = OrganizationChartForm()
    return render(request, 'school_app/organization_chart.html', {'form': form, 'records': records, 'edit_form': edit_form})

def edit_organization_chart(request, pk):
    record = get_object_or_404(OrganizationChart, pk=pk)
    if request.method == 'POST':
        form = OrganizationChartForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': True, 'record': {'date': record.date, 'organization_name': record.organization_name, 'chart_details': record.chart_details}})

def delete_organization_chart(request, pk):
    record = get_object_or_404(OrganizationChart, pk=pk)
    if request.method == 'POST':
        record.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

# ProfessionalDevelopment Views
def professional_development_view(request):
    if request.method == 'POST':
        form = ProfessionalDevelopmentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ProfessionalDevelopmentForm()
    records = ProfessionalDevelopment.objects.all()
    edit_form = ProfessionalDevelopmentForm()
    return render(request, 'school_app/professional_development.html', {'form': form, 'records': records, 'edit_form': edit_form})

def edit_professional_development(request, pk):
    record = get_object_or_404(ProfessionalDevelopment, pk=pk)
    if request.method == 'POST':
        form = ProfessionalDevelopmentForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': True, 'record': {'date': record.date, 'teacher_name': record.teacher_name, 'development_details': record.development_details}})

def delete_professional_development(request, pk):
    record = get_object_or_404(ProfessionalDevelopment, pk=pk)
    if request.method == 'POST':
        record.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

# PLCReport Views
def plc_report_view(request):
    if request.method == 'POST':
        form = PLCReportForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = PLCReportForm()
    records = PLCReport.objects.all()
    edit_form = PLCReportForm()
    return render(request, 'school_app/plc_report.html', {'form': form, 'records': records, 'edit_form': edit_form})

def edit_plc_report(request, pk):
    record = get_object_or_404(PLCReport, pk=pk)
    if request.method == 'POST':
        form = PLCReportForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': True, 'record': {'date': record.date, 'plc_name': record.plc_name, 'report': record.report}})

def delete_plc_report(request, pk):
    record = get_object_or_404(PLCReport, pk=pk)
    if request.method == 'POST':
        record.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def home_view(request):
    dashboard_items = [
        {"title": "Class Cleanliness", "url_name": "class_cleanliness", "img_path": "Images/dashboard/class-cleanliness.png"},
        {"title": "Club Report", "url_name": "club_report", "img_path": "Images/dashboard/club-report.png"},
        {"title": "Log Book", "url_name": "log_book", "img_path": "Images/dashboard/log-book.png"},
        {"title": "Reading Log", "url_name": "reading_log", "img_path": "Images/dashboard/reading-log.png"},
        {"title": "Staff Attendance", "url_name": "staff_attendance", "img_path": "Images/dashboard/staff-attendance.png"},
        {"title": "SUPW Report", "url_name": "supw_report", "img_path": "Images/dashboard/supw-report.png"},
        {"title": "Teachers Substitution", "url_name": "teachers_substitution", "img_path": "Images/dashboard/teachers-substitution.png"},
        {"title": "Teacher's Timetable", "url_name": "teachers_timetable", "img_path": "Images/dashboard/teachers-timetable.png"},
        {"title": "TOD Report", "url_name": "tod_report", "img_path": "Images/dashboard/tod-report.png"},
        {"title": "Organization Chart", "url_name": "organization_chart", "img_path": "Images/dashboard/organogram.png"},
        {"title": "Professional Development", "url_name": "professional_development", "img_path": "Images/dashboard/pd.png"},
        {"title": "PLC Report", "url_name": "plc_report", "img_path": "Images/dashboard/plc-report.png"},
    ]
    return render(request, 'school_app/home.html', {'dashboard_items': dashboard_items})
