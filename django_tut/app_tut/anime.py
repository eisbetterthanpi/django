# https://djangobook.com/mdj2-django-forms/
from django import forms

class AnimeForm(forms.Form):
    # inputval = forms.CharField(max_length=100, label='input val', required=False)
    # btn = forms.CharField(widget=forms.HiddenInput(), required=False)
    btn = forms.CharField()

'''
cd django_tut
python manage.py runserver
'''

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .headless_anime_colab_api import *
import json

# driver = setup_anime_colab()
# img1, img2 = run_anime_colab(driver, high="a")


import time

def inputval(request):
    submitted = False
    if request.method == 'POST':
        form = AnimeForm(request.POST)
        if form.is_valid():
            cd = form.clean()
            # high = form.cleaned_data.get("btn")
            print(request.POST, request.POST["btn"])
            high=cd['btn']
            print(high)

            print("start load")
            img1, img2 = run_anime_colab(inputval.driver, high) #driver drivers[0]
            # time.sleep(1)
            print("finish load")
            # img1="F:/html code/poem n 1.png"
            # img2="F:/html code/poem n 2.png"

            # return render(request, 'app_tut/anime.html', {'val': high, 'form': form, 'submitted': submitted})
            return render(request, 'app_tut/anime.html', {'img1': img1, 'img2': img2, 'form': form, 'submitted': submitted})

    else:
        form = AnimeForm() #new form
    # print("setup") #old setup
    submitted = True
    return render(request, 'app_tut/anime.html', {'form': form, 'submitted': submitted})
    # return render(request, 'app_tut/anime.html', {'img1': img1, 'img2': img2, 'form': form, 'submitted': submitted})


from django.http import JsonResponse
def load(request): #initial setup loading
    print("load setup")
    inputval.driver = setup_anime_colab()
    # time.sleep(1)
    print("load done")
    submitted = True
    return JsonResponse({'image': 'image url here'})
    # return render(request, 'app_tut/anime.html', {'form': form, 'submitted': submitted})
    # return render(request, 'app_tut/anime.html', {'img1': img1, 'img2': img2, 'form': form, 'submitted': submitted})

def no_update(request):
    print("no update",request.POST)
    img=run_zs(inputval.driver)
    # img="F:/html code/poem n 1.png"
    return JsonResponse({'img': img})
