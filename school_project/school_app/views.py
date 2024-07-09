import json
from .forms import EventForm, TodoForm
from .models import Student, Teacher, Event, Todo, Attendance
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
import matplotlib
matplotlib.use('Agg')


def home_view(request):
    return render(request, 'school_app/home.html')


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
