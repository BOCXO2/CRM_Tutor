from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('student/new/', views.student_create, name='student_create'),
    path('student/<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('student/<int:pk>/lesson/new/', views.lesson_create, name='lesson_create'),
    path('lesson/<int:lesson_id>/delete/', views.delete_lesson, name='delete_lesson'),
    path('finance/', views.finance_summary, name='finance_summary'),
    
    # AI функциональность
    path('student/<int:student_id>/ai/plan/', views.ai_plan_lesson, name='ai_plan_lesson'),
    path('student/<int:student_id>/ai/homework/', views.ai_generate_homework, name='ai_generate_homework'),
    path('student/<int:student_id>/ai/analyze/', views.ai_analyze_progress, name='ai_analyze_progress'),
    path('student/<int:student_id>/ai/save-plan/', views.ai_save_lesson_plan, name='ai_save_lesson_plan'),
    path('student/<int:student_id>/ai/save-homework/', views.ai_save_homework, name='ai_save_homework'),
]
