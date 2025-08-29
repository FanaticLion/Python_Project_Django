from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import ContactForm
from .models import Product, Contact  # Добавлен импорт моделей


def home(request):
    # Получаем последние 5 продуктов
    latest_products = Product.objects.order_by('-created_at')[:5]

    # Выводим в консоль (для дополнительного задания)
    print("=" * 50)
    print("ПОСЛЕДНИЕ 5 ПРОДУКТОВ:")
    print("=" * 50)
    for product in latest_products:
        print(f"🏷️  {product.name}")
        print(f"   💰 Цена: {product.price} руб.")
        print(f"   📦 Категория: {product.category.name}")
        print(f"   📅 Создан: {product.created_at}")
        print("-" * 30)

    # Передаем в шаблон
    context = {
        'latest_products': latest_products,
        'title': 'Главная страница - Магазин'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    # Получаем все контакты из базы для отображения
    contacts_list = Contact.objects.all().order_by('-created_at')

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Сохраняем данные в базу
            contact = form.save()
            messages.success(
                request,
                f'✅ Спасибо, {contact.name}! Ваше сообщение отправлено. Мы ответим на {contact.email}'
            )
            return HttpResponseRedirect('/contacts/')
    else:
        form = ContactForm()

    context = {
        'form': form,
        'contacts': contacts_list,  # Передаем контакты в шаблон
        'title': 'Контакты - Магазин'
    }
    return render(request, 'catalog/contacts.html', context)