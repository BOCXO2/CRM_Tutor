from django import forms
from .models import Student, Lesson, Homework

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ["date", "topic", "comment", "price"]