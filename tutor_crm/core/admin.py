from django.contrib import admin
from .models import Student, Lesson, Homework


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "school", "grade")
    search_fields = ("name", "phone", "email", "school")
    list_filter = ("grade",)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("student", "date", "topic", "price")
    search_fields = ("student__name", "topic")
    date_hierarchy = "date"


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ("student", "lesson", "task", "is_done", "grade")
    search_fields = ("student__name", "task")

