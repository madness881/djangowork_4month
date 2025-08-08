from django.shortcuts import render, HttpResponse

# Create your views here.

def test_view(request):
    return HttpResponse('Добро пожаловать! ')

def html_test(request):
    return render(request,"base.html")