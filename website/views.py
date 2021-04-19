from django.shortcuts import render
from random import randint


def home(request):
    return render(request, 'home.html', {})


def add(request):
    num1 = randint(0, 10)
    num2 = randint(0, 10)
    if request.method == 'POST':
        answer = request.POST['answer']
        return render(request, 'add.html', {'answer': answer})
    return render(request, 'add.html', {
        'num1': num1,
        'num2': num2
    })


def subtract(request):
    return render(request, 'subtract.html', {})


def multiply(request):
    return render(request, 'multiply.html', {})


def divide(request):
    return render(request, 'divide.html', {})
