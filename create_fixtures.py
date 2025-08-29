import json
from django.core import serializers
import os
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from catalog.models import Category, Product


def create_fixtures():
    # Создаем папку fixtures если ее нет
    fixtures_dir = 'catalog/fixtures'
    if not os.path.exists(fixtures_dir):
        os.makedirs(fixtures_dir)
        print(f"✅ Создана папка: {fixtures_dir}")

    # Для категорий
    categories = Category.objects.all()
    category_data = serializers.serialize('json', categories, indent=2, ensure_ascii=False)
    with open(f'{fixtures_dir}/category_data.json', 'w', encoding='utf-8') as f:
        f.write(category_data)
    print(f"✅ Создан файл: {fixtures_dir}/category_data.json")
    print(f"   📦 Категорий: {categories.count()} шт.")

    # Для продуктов
    products = Product.objects.all()
    product_data = serializers.serialize('json', products, indent=2, ensure_ascii=False)
    with open(f'{fixtures_dir}/product_data.json', 'w', encoding='utf-8') as f:
        f.write(product_data)
    print(f"✅ Создан файл: {fixtures_dir}/product_data.json")
    print(f"   📦 Продуктов: {products.count()} шт.")

    print("🎉 Все фикстуры успешно созданы!")


if __name__ == '__main__':
    create_fixtures()