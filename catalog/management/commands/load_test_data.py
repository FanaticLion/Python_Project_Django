from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Загрузка тестовых данных для продуктов и категорий'

    def handle(self, *args, **options):
        # Удаляем существующие данные
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write('Удалены старые данные...')

        # Создаем категории
        categories_data = [
            {"name": "Электроника", "description": "Электронные устройства и гаджеты"},
            {"name": "Одежда", "description": "Одежда и аксессуары"},
            {"name": "Книги", "description": "Художественная и учебная литература"},
            {"name": "Спорт", "description": "Спортивные товары и инвентарь"},
            {"name": "Мебель", "description": "Мебель для дома и офиса"},
        ]

        for cat_data in categories_data:
            Category.objects.create(**cat_data)

        self.stdout.write('Созданы категории...')

        # Получаем созданные категории
        electronics = Category.objects.get(name="Электроника")
        clothing = Category.objects.get(name="Одежда")
        books = Category.objects.get(name="Книги")
        sports = Category.objects.get(name="Спорт")
        furniture = Category.objects.get(name="Мебель")

        # Создаем продукты
        products_data = [
            # Электроника
            {"name": "Смартфон iPhone 15", "price": 89999.99, "category": electronics,
             "description": "Последняя модель iPhone с улучшенной камерой"},
            {"name": "Ноутбук Dell XPS", "price": 129999.99, "category": electronics,
             "description": "Мощный игровой ноутбук с SSD диском"},
            {"name": "Наушники Sony", "price": 15999.99, "category": electronics,
             "description": "Беспроводные наушники с шумоподавлением"},

            # Одежда
            {"name": "Футболка хлопковая", "price": 1999.99, "category": clothing,
             "description": "Мужская хлопковая футболка черного цвета"},
            {"name": "Джинсы классические", "price": 4999.99, "category": clothing,
             "description": "Синие джинсы прямого кроя"},
            {"name": "Куртка зимняя", "price": 8999.99, "category": clothing,
             "description": "Теплая зимняя куртка с мехом"},

            # Книги
            {"name": "Программирование на Python", "price": 1499.99, "category": books,
             "description": "Учебник по программированию для начинающих"},
            {"name": "Игра престолов", "price": 999.99, "category": books,
             "description": "Фэнтези роман Джорджа Мартина"},

            # Спорт
            {"name": "Футбольный мяч", "price": 2999.99, "category": sports,
             "description": "Профессиональный футбольный мяч"},
            {"name": "Гантели 5кг", "price": 1999.99, "category": sports,
             "description": "Набор гантелей для тренировок"},

            # Мебель
            {"name": "Офисное кресло", "price": 8999.99, "category": furniture,
             "description": "Эргономичное офисное кресло"},
        ]

        for product_data in products_data:
            Product.objects.create(**product_data)

        self.stdout.write(
            self.style.SUCCESS('✅ Успешно загружено!')
        )
        self.stdout.write(
            self.style.SUCCESS(f'📦 Категории: {Category.objects.count()} шт.')
        )
        self.stdout.write(
            self.style.SUCCESS(f'📦 Продукты: {Product.objects.count()} шт.')
        )