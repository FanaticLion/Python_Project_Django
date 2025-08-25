# Skystore - Интернет-магазин цифровых товаров

![Django](https://img.shields.io/badge/Django-4.2-green.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-blue.svg)
![Python](https://img.shields.io/badge/Python-3.13-yellow.svg)

## 📋 О проекте

Skystore - это современный интернет-магазин для продажи цифровых товаров: плагинов, шаблонов кода, скриптов и утилит. Проект разработан на Django с использованием Bootstrap для стилизации.

## ✨ Возможности

- 🏠 **Главная страница** с каталогом товаров
- 📞 **Страница контактов** с формой обратной связи
- 🎨 **Адаптивный дизайн** на Bootstrap 5
- 📱 **Мобильная версия** 
- 📧 **Форма обратной связи** с валидацией
- ⚡ **Административная панель** Django

## 🛠 Технологии

- **Backend**: Django 4.2
- **Frontend**: Bootstrap 5.3, HTML5, CSS3
- **Database**: SQLite3 (для разработки)
- **Language**: Python 3.13
- **Package management**: Poetry

## 📁 Структура проекта
PythonProject11/
├── catalog/ # Основное приложение
│ ├── migrations/ # Миграции базы данных
│ ├── templates/ # HTML шаблоны
│ │ └── catalog/
│ │ ├── home.html # Главная страница
│ │ └── contacts.html # Страница контактов
│ ├── init.py
│ ├── admin.py # Административная панель
│ ├── apps.py # Конфигурация приложения
│ ├── forms.py # Формы (обратная связь)
│ ├── models.py # Модели данных
│ ├── tests.py # Тесты
│ ├── urls.py # Маршруты приложения
│ └── views.py # Контроллеры
├── config/ # Настройки проекта
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py # Основные настройки
│ ├── urls.py # Главные маршруты
│ └── wsgi.py
├── static/ # Статические файлы
│ └── bootstrap-5.3.7/ # Bootstrap framework
├── venv/ # Виртуальное окружение
├── .gitignore # Git ignore правила
├── db.sqlite3 # База данных (dev)
├── manage.py # Django management
├── poetry.lock Poetry lock file
├── pyproject.toml Poetry dependencies
└── README.md # Этот файл

text

## 🚀 Установка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/ваш-username/PythonProject11.git
cd PythonProject11
2. Установка зависимостей
bash
# Установка Poetry (если не установлен)
pip install poetry

# Установка зависимостей проекта
poetry install

# Активация виртуального окружения
poetry shell
3. Настройка базы данных
bash
# Применение миграций
python manage.py migrate

# Создание суперпользователя (опционально)
python manage.py createsuperuser
4. Запуск сервера
bash
# Запуск development сервера
python manage.py runserver

# Приложение будет доступно по адресу:
# http://localhost:8000/
📊 Маршруты (URLs)
/ - Главная страница

/contacts/ - Страница контактов с формой обратной связи

/admin/ - Административная панель Django

👥 Разработка
Git ветвление
Проект использует упрощенную GitFlow стратегию:

main - Стабильная версия (production)

develop - Ветка разработки

Добавление нового функционала
bash
# Переход в ветку разработки
git checkout develop

# Создание feature ветки
git checkout -b feature/название-фичи

# После разработки...
git add .
git commit -m "feat: описание фичи"

# Мерж в develop
git checkout develop
git merge --no-ff feature/название-фичи
###📝 Форма обратной связи
Страница контактов включает форму с валидацией:

Поле имени (обязательное)

Поле телефона (обязательное)

Текстовое поле сообщения

Валидация на стороне сервера

Уведомления об успешной отправке

###🎨 Стилизация
Bootstrap 5.3 - современный CSS framework

Адаптивный дизайн - поддержка мобильных устройств

Компоненты Bootstrap - кнопки, формы, карточки

Custom стили - кастомные настройки

###📦 Зависимости
Основные зависимости (см. pyproject.toml):

Django == 4.2.*

Bootstrap 5.3.7 (статически)

Другие зависимости Django

###🔧 Настройки
Основные настройки в config/settings.py:

Debug режим

Настройки базы данных

Static files configuration

Installed apps

Template settings

###🤝 Contributing
Форкните репозиторий

Создайте feature ветку (git checkout -b feature/AmazingFeature)

Закоммитьте изменения (git commit -m 'Add AmazingFeature')

Запушьте ветку (git push origin feature/AmazingFeature)

Откройте Pull Request
