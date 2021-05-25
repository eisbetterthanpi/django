from django.shortcuts import render
# from django.http import HttpResponse

def home(request):
    # return HttpResponse('<h1>app_tut Home</h1>')
    return render(request,'app_tut/home.html')


def about(request):
    return render(request,'app_tut/about.html')
