from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, EventForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, EventForm
from .models import Event, Category


def index(request):
    events = Event.objects.all().order_by('-date')
    categories = Category.objects.all()
    regions = Event.objects.exclude(region='').values_list('region', flat=True).distinct()

    # Фильтрация
    q = request.GET.get('q', '').strip()
    if q:
        events = events.filter(title__icontains=q) | events.filter(description__icontains=q)

    cat_ids = request.GET.getlist('categories')
    if cat_ids:
        events = events.filter(categories__id__in=cat_ids).distinct()

    region_list = request.GET.getlist('regions')
    if region_list:
        events = events.filter(region__in=region_list)

    return render(request, 'history/index.html', {
        'events': events,
        'categories': categories,
        'regions': regions,
        'user': request.user,
        'selected_categories': cat_ids,
        'selected_regions': region_list,
    })

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'history/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'history/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')

@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            messages.success(request, 'Событие добавлено!')
            return redirect('index')
    else:
        form = EventForm()
    return render(request, 'history/add_event.html', {'form': form})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'history/event_detail.html', {'event': event})

