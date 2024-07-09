from django.urls import path
from .views import home_view, about_view, dashboard_view, calendar_view, add_event, view_event, todo_list, add_todo, mark_completed, delete_todo, pie_chart_view, edit_attendance_view, update_attendance

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('calendar/', calendar_view, name='calendar'),
    path('add_event/', add_event, name='add_event'),
    path('view_event/<int:event_id>/', view_event, name='view_event'),
    path('todos/', todo_list, name='todo_list'),
    path('add_todo/', add_todo, name='add_todo'),
    path('mark_completed/<int:todo_id>/',
         mark_completed, name='mark_completed'),
    path('delete_todo/<int:todo_id>/', delete_todo, name='delete_todo'),
    path('pie_chart/', pie_chart_view, name='pie_chart'),
    path('edit_attendance/', edit_attendance_view, name='edit_attendance'),
    path('update_attendance/', update_attendance, name='update_attendance'),
]
