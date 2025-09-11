from django.shortcuts import render

def index(request):
    return render(request,'front/index.html')

def quiz (request):
    return render(request, 'front/quiz.html')