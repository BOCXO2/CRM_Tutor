from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Lesson, Homework
from .forms import StudentForm, LessonForm
from django.db.models import Sum
from django.db.models.functions import TruncMonth
import calendar
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