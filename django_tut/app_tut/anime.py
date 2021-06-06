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
            # val=cd['btn']

            print(request.POST, request.POST["btn"])
            # if 'left' in request.POST:
            # if request.POST["btn"] == 'left':
            if 'btn_l' in request.POST:
                # print("submit left")
                high="left"
            elif 'btn_r' in request.POST:
                high="right"
            else:
                val=cd['btn']
                high=val
                # print("val",val)

            print(high)

            print("start load")
            img1, img2 = run_anime_colab(inputval.driver, high) #driver drivers[0]
            # time.sleep(3)
            print("finish load")
            # img1="F:/html code/poem n 1.png"
            # img2="F:/html code/poem n 2.png"

            # return render(request, 'app_tut/anime.html', {'val': high, 'form': form, 'submitted': submitted})
            return render(request, 'app_tut/anime.html', {'img1': img1, 'img2': img2, 'form': form, 'submitted': submitted})

    else:
        form = AnimeForm() #new form
    print("setup")
    inputval.driver = setup_anime_colab()
    print("done")
    submitted = True
    return render(request, 'app_tut/anime.html', {'form': form, 'submitted': submitted})
    # return render(request, 'app_tut/anime.html', {'img1': img1, 'img2': img2, 'form': form, 'submitted': submitted})
