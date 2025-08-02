#!/usr/bin/env python3
"""
Скрипт для тестирования AI функциональности
"""

import os
import sys
import django
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Настраиваем Django
sys.path.append(os.path.join(os.path.dirname(__file__), 'tutor_crm'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutor_crm.settings')
django.setup()

from tutor_crm.core.models import Student
from tutor_crm.core.ai_services import AITutorService

def test_ai_functionality():
    """Тестирует AI функциональность"""
    print("🤖 Тестирование AI функциональности")
    print("=" * 50)
    
    # Проверяем API ключ
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ OPENAI_API_KEY не найден в переменных окружения")
        print("Создайте файл .env с вашим API ключом:")
        print("OPENAI_API_KEY=your_key_here")
        return False
    
    print("✅ API ключ найден")
    
    # Создаем тестового ученика
    student, created = Student.objects.get_or_create(
        name="Тестовый ученик",
        defaults={
            'phone': '+7 999 123-45-67',
            'email': 'test@example.com',
            'school': 'Тестовая школа',
            'grade': '9 класс',
            'goal': 'Подготовка к ОГЭ по математике',
            'notes': 'Хорошо усваивает материал, нужна практика'
        }
    )
    
    if created:
        print(f"✅ Создан тестовый ученик: {student.name}")
    else:
        print(f"✅ Используется существующий ученик: {student.name}")
    
    # Тестируем AI сервис
    ai_service = AITutorService()
    
    print("\n📋 Тестирование планирования урока...")
    result = ai_service.plan_lesson(student, "Квадратные уравнения", 60)
    
    if result['success']:
        print("✅ Планирование урока работает")
        plan = result['plan']
        print(f"   Название: {plan.get('title', 'N/A')}")
        print(f"   Цели: {len(plan.get('objectives', []))}")
        print(f"   Структура: {len(plan.get('structure', []))} этапов")
    else:
        print(f"❌ Ошибка планирования: {result['error']}")
    
    print("\n📝 Тестирование генерации домашнего задания...")
    result = ai_service.generate_homework(student, "Квадратные уравнения", "medium")
    
    if result['success']:
        print("✅ Генерация ДЗ работает")
        homework = result['homework']
        print(f"   Название: {homework.get('title', 'N/A')}")
        print(f"   Заданий: {len(homework.get('tasks', []))}")
        print(f"   Время: {homework.get('estimated_time', 'N/A')}")
    else:
        print(f"❌ Ошибка генерации ДЗ: {result['error']}")
    
    print("\n📊 Тестирование анализа прогресса...")
    result = ai_service.analyze_student_progress(student)
    
    if result['success']:
        print("✅ Анализ прогресса работает")
        analysis = result['analysis']
        print(f"   Сильные стороны: {len(analysis.get('strengths', []))}")
        print(f"   Рекомендации: {len(analysis.get('recommendations', []))}")
    else:
        print(f"❌ Ошибка анализа: {result['error']}")
    
    print("\n" + "=" * 50)
    print("🎉 Тестирование завершено!")
    
    return True

if __name__ == "__main__":
    test_ai_functionality() 