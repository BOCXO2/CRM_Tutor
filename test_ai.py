#!/usr/bin/env python3
"""
Тестовый скрипт для проверки AI функциональности
"""

import os
import sys
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutor_crm.settings')
django.setup()

from tutor_crm.core.ai_services import AITutorService
from tutor_crm.core.models import Student

def test_ai_service():
    """Тестирование AI сервиса"""
    print("🤖 Тестирование AI сервиса для математики 6 класса")
    print("=" * 60)
    
    # Создаем тестового ученика
    student, created = Student.objects.get_or_create(
        name="Тестовый ученик",
        defaults={
            'school': "Тестовая школа",
            'grade': "6 класс",
            'goal': "Изучение математики"
        }
    )
    
    ai_service = AITutorService()
    
    # Тестируем планирование уроков для разных тем
    test_topics = [
        "десятичные дроби",
        "проценты", 
        "пропорции",
        "координатная плоскость",
        "положительные и отрицательные числа"
    ]
    
    print("\n📋 Тестирование планирования уроков:")
    print("-" * 40)
    
    for topic in test_topics:
        print(f"\n🎯 Тема: {topic}")
        prompt = f"Спланируй урок по теме {topic}"
        result = ai_service.plan_lesson(student, topic)
        
        if result and 'title' in result:
            print(f"✅ Найдена тема: {result['title']}")
            print(f"📚 Цели: {', '.join(result['objectives'][:2])}...")
            print(f"⏰ Структура: {len(result['structure'])} этапов")
        else:
            print(f"❌ Тема не найдена или ошибка")
    
    # Тестируем создание домашних заданий
    print("\n📝 Тестирование создания домашних заданий:")
    print("-" * 40)
    
    for topic in test_topics:
        print(f"\n🎯 Тема: {topic}")
        prompt = f"Создай домашнее задание по теме {topic}"
        result = ai_service.generate_homework(student, topic)
        
        if result and 'title' in result:
            print(f"✅ Создано ДЗ: {result['title']}")
            if 'tasks' in result:
                print(f"📋 Заданий: {len(result['tasks'])}")
                for task in result['tasks'][:2]:  # Показываем первые 2 задания
                    print(f"   • {task['task']}")
        else:
            print(f"❌ ДЗ не создано или ошибка")
    
    # Тестируем анализ прогресса
    print("\n📊 Тестирование анализа прогресса:")
    print("-" * 40)
    
    result = ai_service.analyze_student_progress(student)
    if result and 'progress_summary' in result:
        print(f"✅ Анализ создан: {result['progress_summary'][:100]}...")
    else:
        print("❌ Анализ не создан или ошибка")
    
    print("\n" + "=" * 60)
    print("✅ Тестирование завершено!")

if __name__ == "__main__":
    test_ai_service() 