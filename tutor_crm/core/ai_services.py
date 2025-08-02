import openai
import os
from django.conf import settings
from .models import Student, Lesson, Homework
import json

class AITutorService:
    def __init__(self):
        # Используем переменную окружения для API ключа
        self.api_key = os.getenv('OPENAI_API_KEY')
        # Временная настройка для тестирования (удалите эту строку в продакшене!)
        # self.api_key = "sk-your-api-key-here"
        if self.api_key:
            openai.api_key = self.api_key
    
    def plan_lesson(self, student, topic=None, duration=60):
        """Планирует урок с помощью AI"""
        if not self.api_key:
            return {
                'success': False,
                'error': 'API ключ не настроен'
            }
        
        try:
            # Собираем информацию об ученике
            student_info = f"""
            Ученик: {student.name}
            Класс: {student.grade}
            Школа: {student.school}
            Цель занятий: {student.goal}
            Заметки: {student.notes}
            """
            
            # Получаем историю занятий
            recent_lessons = student.lessons.all().order_by('-date')[:5]
            lesson_history = ""
            for lesson in recent_lessons:
                lesson_history += f"- {lesson.date}: {lesson.topic}\n"
            
            prompt = f"""
            Ты опытный репетитор. Спланируй урок для ученика.
            
            {student_info}
            
            Последние занятия:
            {lesson_history}
            
            Тема урока: {topic or 'Продолжение предыдущей темы'}
            Длительность: {duration} минут
            
            Создай план урока в формате JSON:
            {{
                "title": "Название урока",
                "objectives": ["Цель 1", "Цель 2"],
                "structure": [
                    {{
                        "time": "0-10 мин",
                        "activity": "Описание активности",
                        "description": "Подробное описание"
                    }}
                ],
                "materials": ["Материал 1", "Материал 2"],
                "homework": "Домашнее задание",
                "notes": "Дополнительные заметки"
            }}
            """
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Ты опытный репетитор, который создает качественные планы уроков."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1000,
                temperature=0.7
            )
            
            lesson_plan = json.loads(response.choices[0].message.content)
            return {
                'success': True,
                'plan': lesson_plan
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def generate_homework(self, student, lesson_topic, difficulty="medium"):
        """Генерирует домашнее задание с помощью AI"""
        if not self.api_key:
            return {
                'success': False,
                'error': 'API ключ не настроен'
            }
        
        try:
            prompt = f"""
            Создай домашнее задание для ученика.
            
            Ученик: {student.name}
            Класс: {student.grade}
            Тема урока: {lesson_topic}
            Сложность: {difficulty}
            
            Создай задание в формате JSON:
            {{
                "title": "Название задания",
                "description": "Описание задания",
                "tasks": [
                    {{
                        "number": 1,
                        "task": "Описание задачи",
                        "hint": "Подсказка (опционально)"
                    }}
                ],
                "estimated_time": "Примерное время выполнения",
                "difficulty": "Сложность"
            }}
            """
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Ты опытный учитель, создающий качественные домашние задания."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=800,
                temperature=0.7
            )
            
            homework = json.loads(response.choices[0].message.content)
            return {
                'success': True,
                'homework': homework
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def analyze_student_progress(self, student):
        """Анализирует прогресс ученика с помощью AI"""
        if not self.api_key:
            return {
                'success': False,
                'error': 'API ключ не настроен'
            }
        
        try:
            # Получаем все занятия ученика
            lessons = student.lessons.all().order_by('date')
            homework = student.homeworks.all()
            
            lessons_summary = ""
            for lesson in lessons:
                lessons_summary += f"- {lesson.date}: {lesson.topic}\n"
            
            homework_summary = ""
            completed = 0
            for hw in homework:
                status = "✅" if hw.is_done else "❌"
                homework_summary += f"- {status} {hw.task[:50]}...\n"
                if hw.is_done:
                    completed += 1
            
            prompt = f"""
            Проанализируй прогресс ученика и дай рекомендации.
            
            Ученик: {student.name}
            Класс: {student.grade}
            Цель: {student.goal}
            
            История занятий:
            {lessons_summary}
            
            Домашние задания:
            {homework_summary}
            Выполнено: {completed}/{len(homework)} заданий
            
            Дай анализ в формате JSON:
            {{
                "progress_summary": "Общая оценка прогресса",
                "strengths": ["Сильные стороны"],
                "weaknesses": ["Области для улучшения"],
                "recommendations": ["Рекомендации"],
                "next_topics": ["Следующие темы для изучения"],
                "motivation_tips": ["Советы по мотивации"]
            }}
            """
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Ты опытный педагог-психолог, анализирующий прогресс учеников."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=600,
                temperature=0.7
            )
            
            analysis = json.loads(response.choices[0].message.content)
            return {
                'success': True,
                'analysis': analysis
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            } 