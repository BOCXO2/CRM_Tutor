from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_list, name="student_list"),
    path("student/<int:pk>/", views.student_detail, name="student_detail"),
    path("student/add/", views.student_create, name="student_add"),
    path("student/<int:pk>/edit/", views.student_edit, name="student_edit"),
    path("student/<int:pk>/lesson/add/", views.lesson_create, name="lesson_add"),
    path("finance/", views.finance_summary, name="finance_summary"),
    path('delete_lesson/<int:lesson_id>/', views.delete_lesson, name='delete_lesson'),
]
