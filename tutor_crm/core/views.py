from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Lesson, Homework
from .forms import StudentForm, LessonForm
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from .ai_services import AITutorService
import calendar
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def student_list(request):
    students = Student.objects.all()
    return render(request, "core/student_list.html", {"students": students})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    lessons = student.lessons.all().order_by("-date")
    return render(request, "core/student_detail.html", {"student": student, "lessons": lessons})

def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm()
    return render(request, "core/student_form.html", {"form": form})


def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("student_detail", pk=pk)
    else:
        form = StudentForm(instance=student)
    return render(request, "core/student_form.html", {"form": form})


def lesson_create(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.student = student
            lesson.save()
            return redirect("student_detail", pk=pk)
    else:
        form = LessonForm()
    return render(request, "core/lesson_form.html", {"form": form, "student": student})

def finance_summary(request):
    data = (
        Lesson.objects.filter(price__gt=0)
        .annotate(month=TruncMonth("date"))
        .values("month")
        .annotate(total=Sum("price"))
        .order_by("month")
    )

    total_sum = Lesson.objects.filter(price__gt=0).aggregate(Sum("price"))["price__sum"] or 0

    for item in data:
        item["month_str"] = item["month"].strftime("%B %Y")  # например, "Август 2025"

    return render(request, "core/finance_summary.html", {
        "total_sum": total_sum,
        "monthly_data": data
    })

def delete_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    student_pk = lesson.student.pk
    lesson.delete()
    return redirect('student_detail', pk=student_pk)

def ai_plan_lesson(request, student_id):
    """AI планирование урока"""
    student = get_object_or_404(Student, pk=student_id)
    ai_service = AITutorService()
    
    if request.method == "POST":
        topic = request.POST.get('topic', '')
        duration = int(request.POST.get('duration', 60))
        
        result = ai_service.plan_lesson(student, topic, duration)
        
        if result['success']:
            return render(request, "core/ai_lesson_plan.html", {
                "student": student,
                "plan": result['plan'],
                "topic": topic
            })
        else:
            return render(request, "core/ai_lesson_plan.html", {
                "student": student,
                "error": result['error']
            })
    
    return render(request, "core/ai_plan_form.html", {"student": student})

def ai_generate_homework(request, student_id):
    """AI генерация домашнего задания"""
    student = get_object_or_404(Student, pk=student_id)
    ai_service = AITutorService()
    
    if request.method == "POST":
        lesson_topic = request.POST.get('lesson_topic', '')
        difficulty = request.POST.get('difficulty', 'medium')
        
        result = ai_service.generate_homework(student, lesson_topic, difficulty)
        
        if result['success']:
            return render(request, "core/ai_homework.html", {
                "student": student,
                "homework": result['homework'],
                "lesson_topic": lesson_topic
            })
        else:
            return render(request, "core/ai_homework.html", {
                "student": student,
                "error": result['error']
            })
    
    return render(request, "core/ai_homework_form.html", {"student": student})

def ai_analyze_progress(request, student_id):
    """AI анализ прогресса ученика"""
    student = get_object_or_404(Student, pk=student_id)
    ai_service = AITutorService()
    
    result = ai_service.analyze_student_progress(student)
    
    if result['success']:
        return render(request, "core/ai_progress_analysis.html", {
            "student": student,
            "analysis": result['analysis']
        })
    else:
        return render(request, "core/ai_progress_analysis.html", {
            "student": student,
            "error": result['error']
        })

@csrf_exempt
def ai_save_lesson_plan(request, student_id):
    """Сохранение плана урока от AI"""
    if request.method == "POST":
        student = get_object_or_404(Student, pk=student_id)
        data = json.loads(request.body)
        
        # Создаем новое занятие на основе плана AI
        lesson = Lesson.objects.create(
            student=student,
            date=data.get('date'),
            topic=data.get('title'),
            comment=data.get('notes', ''),
            price=data.get('price', 0)
        )
        
        return JsonResponse({'success': True, 'lesson_id': lesson.id})
    
    return JsonResponse({'success': False, 'error': 'Invalid request'})

@csrf_exempt
def ai_save_homework(request, student_id):
    """Сохранение домашнего задания от AI"""
    if request.method == "POST":
        student = get_object_or_404(Student, pk=student_id)
        data = json.loads(request.body)
        
        # Создаем домашнее задание на основе AI
        homework = Homework.objects.create(
            student=student,
            lesson_id=data.get('lesson_id'),
            task=data.get('description', ''),
            is_done=False
        )
        
        return JsonResponse({'success': True, 'homework_id': homework.id})
    
    return JsonResponse({'success': False, 'error': 'Invalid request'})