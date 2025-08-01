<<<<<<< HEAD
# 🤖 CRM для репетитора с AI

Система управления учениками для репетиторов с интеграцией искусственного интеллекта.

## ✨ Возможности

### Основные функции
- 📚 Управление учениками и занятиями
- 💰 Финансовая отчетность
- 📝 Домашние задания
- 📊 Аналитика прогресса

### AI функциональность
- 🤖 Планирование уроков с помощью AI
- 📝 Генерация домашних заданий
- 📊 Анализ прогресса учеников
- 💡 Персонализированные рекомендации

## 🚀 Установка

1. **Клонируйте репозиторий:**
```bash
git clone <repository-url>
cd tutor_crm
```

2. **Создайте виртуальное окружение:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows
```

3. **Установите зависимости:**
```bash
pip install -r requirements.txt
```

4. **Настройте переменные окружения:**
Создайте файл `.env` в корне проекта:
```env
OPENAI_API_KEY=your_openai_api_key_here
DEBUG=True
SECRET_KEY=your_secret_key_here
```

5. **Выполните миграции:**
```bash
python manage.py migrate
```

6. **Создайте суперпользователя:**
```bash
python manage.py createsuperuser
```

7. **Запустите сервер:**
```bash
python manage.py runserver
```

## 🔧 Настройка AI

### Получение API ключа OpenAI
1. Зарегистрируйтесь на [OpenAI](https://openai.com/)
2. Перейдите в раздел API Keys
3. Создайте новый API ключ
4. Добавьте ключ в файл `.env`

### Использование AI функций
1. **Планирование урока:**
   - Перейдите к ученику
   - Нажмите "📋 Планировать урок"
   - Укажите тему и длительность
   - AI создаст детальный план урока

2. **Генерация домашних заданий:**
   - Нажмите "📝 Создать ДЗ"
   - Укажите тему урока и сложность
   - AI сгенерирует задания с подсказками

3. **Анализ прогресса:**
   - Нажмите "📊 Анализ прогресса"
   - AI проанализирует успеваемость и даст рекомендации

## 📁 Структура проекта

```
tutor_crm/
├── core/
│   ├── models.py          # Модели данных
│   ├── views.py           # Представления
│   ├── ai_services.py     # AI сервисы
│   ├── templates/         # HTML шаблоны
│   └── urls.py           # URL маршруты
├── tutor_crm/
│   ├── settings.py        # Настройки Django
│   └── urls.py           # Главные URL
└── requirements.txt       # Зависимости
```

## 🎯 Примеры использования

### Планирование урока
AI учтет:
- Цель занятий ученика
- Последние пройденные темы
- Уровень сложности
- Временные рамки

### Генерация заданий
AI создаст:
- Задания разной сложности
- Подсказки и объяснения
- Оценку времени выполнения
- Персонализированные задачи

### Анализ прогресса
AI проанализирует:
- Сильные и слабые стороны
- Рекомендации по улучшению
- Следующие темы для изучения
- Советы по мотивации

## 🔒 Безопасность

- API ключи хранятся в переменных окружения
- Все запросы к AI логируются
- Данные учеников защищены

## 🚧 Разработка

### Добавление новых AI функций
1. Создайте метод в `ai_services.py`
2. Добавьте представление в `views.py`
3. Создайте шаблон в `templates/`
4. Добавьте URL маршрут

### Тестирование
```bash
python manage.py test
```

## 📞 Поддержка

При возникновении проблем:
1. Проверьте настройки API ключа
2. Убедитесь в корректности данных ученика
3. Проверьте логи Django

## 📄 Лицензия

MIT License 
=======
# Учёт занятий репетитора

Простой веб-приложение на Python (Tkinter) для учёта учеников, их занятий, оплаты и доходов.

## 🚀 Возможности

- ✅ Добавление учеников с указанием ФИО, предмета, стоимости занятия.
- 📅 Учет занятий по дате с автоматическим добавлением стоимости.
- 💰 Автоматический расчет общей прибыли и помесячной статистики.
- 📊 Отображение финансов по каждому месяцу.
- ❌ Возможность удаления занятий.
- 🔍 Удобный и минималистичный интерфейс на Tkinter.

## 📸 Интерфейс

## 🛠 Установка и запуск

1. Убедитесь, что у вас установлен Python 3.10+.

2. Клонируйте репозиторий:

```bash
git clone https://github.com/ваш-профиль/ваш-проект.git
cd ваш-проект
```

3. Запустите приложение:

```bash
python main.py
```

## 📁 Структура проекта

```text
├── main.py               # Основной запуск
├── app/                  # Логика приложения
│   ├── models.py         # Модели данных (ученики, занятия)
│   ├── views.py          # Графический интерфейс
│   ├── finance.py        # Финансовая логика
│   └── utils.py          # Утилиты
└── data/
    └── database.pkl      # Локальное хранилище данных (автосохраняется)
```

## 📦 Используемые технологии

- Python 3.10+
- Tkinter
- Pickle (для хранения данных)

## 🔒 Сохранение данных

Все данные автоматически сохраняются в файл `database.pkl`. При повторном запуске они загружаются автоматически.

## 📌 Пример использования

1. Запустите `main.py`
2. Добавьте ученика.
3. Добавьте занятие — система сразу посчитает оплату.
4. Перейдите во вкладку **Финансы**, чтобы увидеть статистику.
5. При необходимости удалите занятие из списка.

## 🧑‍💻 Автор

- 👤 Stas Opishko — [GitHub](https://github.com/bocxo2)

## 📄 Лицензия

Этот проект находится под лицензией MIT. Свободен для использования и модификации.

>>>>>>> 9055346e170aa3f647af63faece32033d84e3a78
