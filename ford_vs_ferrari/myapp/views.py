from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

def resumo(request):
    return render(request, 'myapp/resumo.html')

def onde_encontrar(request):
    return render(request, 'myapp/onde_encontrar.html')