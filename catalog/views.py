from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import ContactForm

def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Обработка данных
            name = form.cleaned_data['name']
            messages.success(request, f'Спасибо, {name}! Ваше сообщение отправлено.')
            return HttpResponseRedirect('/contacts/')
    else:
        form = ContactForm()

    return render(request, 'catalog/contacts.html', {'form': form})