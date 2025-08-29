from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import ContactForm , ProductForm
from .models import Product, Contact  # Добавлен импорт моделей
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    # Получаем ВСЕ продукты вместо только последних 5
    all_products = Product.objects.order_by('-created_at')

    # Настраиваем пагинацию - 6 товаров на страницу
    paginator = Paginator(all_products, 6)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # Если page не число, показываем первую страницу
        products = paginator.page(1)
    except EmptyPage:
        # Если page вне диапазона, показываем последнюю страницу
        products = paginator.page(paginator.num_pages)

    # Вывод в консоль для отладки
    print("=" * 50)
    print(f"СТРАНИЦА: {products.number} из {paginator.num_pages}")
    print("=" * 50)
    for product in products:
        print(f"🏷️  {product.name} - {product.price} руб.")

    context = {
        'products': products,  # Передаем page object вместо queryset
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


# catalog/views.py
def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'Товар "{product.name}" успешно добавлен!')
            return redirect('catalog:product_detail', pk=product.id)
    else:
        form = ProductForm()

    context = {
        'form': form,
        'title': 'Добавить товар - Магазин'
    }
    return render(request, 'catalog/add_product.html', context)