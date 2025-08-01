from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField("Имя ученика", max_length=100)
    phone = models.CharField("Телефон", max_length=20, blank=True)
    email = models.EmailField("Email", blank=True)
    school = models.CharField("Школа", max_length=100, blank=True)
    grade = models.CharField("Класс", max_length=20, blank=True)
    goal = models.TextField("Цель занятий", blank=True)
    notes = models.TextField("Доп. заметки", blank=True)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='lessons')
    date = models.DateField("Дата занятия")
    topic = models.CharField("Тема занятия", max_length=200)
    comment = models.TextField("Комментарий", blank=True)
    price = models.DecimalField("Сумма оплаты", max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.topic}"

class Homework(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='homeworks')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='homeworks')
    task = models.TextField("Задание")
    is_done = models.BooleanField("Выполнено", default=False)
    grade = models.CharField("Оценка", max_length=10, blank=True)

    def __str__(self):
        return f"ДЗ для {self.student.name} ({'✔' if self.is_done else '✘'})"
    
