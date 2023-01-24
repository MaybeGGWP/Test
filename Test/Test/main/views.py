from django.shortcuts import render
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница', 'tasks': tasks})


def info(request):
    return render(request,  'main/info.html')


def create(request):
    return render(request, 'main/create.html')
