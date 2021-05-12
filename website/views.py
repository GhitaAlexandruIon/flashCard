from django.shortcuts import render
from random import randint


def home(request):
    return render(request, 'home.html', {})


def add(request):
    num1 = randint(0, 10)
    num2 = randint(0, 10)
    if request.method == 'POST':
        answer = request.POST['answer']
        old_num1 = request.POST['old_num1']
        old_num2 = request.POST['old_num2']
        correct_answer = int(old_num1) + int(old_num2)
        if int(answer) == correct_answer:
            my_answer = 'Correct ' + old_num1 + '+' + old_num2 + '=' + answer
            color = 'success'
        else:
            my_answer = 'Incorrect ' + old_num1 + '+' + old_num2 + ' is not ' + answer + ' it is ' + str(correct_answer)
            color = 'danger'
        return render(request, 'add.html', {'answer': answer,
                                            'my_answer': my_answer,
                                            'num1': num1,
                                            'num2': num2,
                                            'color': color})
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
