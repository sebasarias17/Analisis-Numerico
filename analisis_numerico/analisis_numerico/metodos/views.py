from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def cap1(request):
    return render(request, 'cap1.html')

def cap2(request):
    return render(request, 'cap2.html')

def cap3(request):
    return render(request, 'cap3.html')

