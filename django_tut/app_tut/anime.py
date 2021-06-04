# https://djangobook.com/mdj2-django-forms/
from django import forms

class AnimeForm(forms.Form):
    # inputval = forms.CharField(max_length=100, label='input val', required=False)
    # <input type="image" name="Name of image button" src="Path of the Image file? border="Specfiy Image Border " alt="text">

    choices=[("left",1),("right",2)]
    # choices=[(1,"left"),(2,"right")]
    # btn = forms.CharField(widget=forms.RadioSelect(choices=choices))
    # btn = forms.CharField(widget=forms.HiddenInput())
    btn = forms.CharField(widget=forms.HiddenInput(), required=False)

'''
cd django_tut
python manage.py runserver
'''

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .headless_anime_colab_api import *


# drivers=[]
# driver = setup_anime_colab()
# img1, img2 = run_anime_colab(driver, high="a")


def inputval(request):
    submitted = False
    if request.method == 'POST':
        form = AnimeForm(request.POST)
        if form.is_valid():
            # cd = form.cleaned_data
            cd = form.clean()
            # high = form.cleaned_data.get("btn")
            # val=cd['btn']
            # print("val",val)

            # print(request.POST, request.POST["btn"])
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
            # img1, img2 = run_anime_colab(driver, high)
            # img1, img2 = run_anime_colab(drivers[0], high)
            img1, img2 = run_anime_colab(inputval.driver, high)

            # return render(request, 'app_tut/anime.html', {'val': high, 'form': form, 'submitted': submitted})
            return render(request, 'app_tut/anime.html', {'img1': img1, 'img2': img2, 'form': form, 'submitted': submitted})

    else:
        form = AnimeForm()
        if 'submitted' in request.GET:
            print("sfg")
            submitted = True
    print("setup")
    inputval.driver = setup_anime_colab()
    # drivers[0] = setup_anime_colab()
    return render(request, 'app_tut/anime.html', {'form': form, 'submitted': submitted})
    # return render(request, 'app_tut/anime.html', {'img1': img1, 'img2': img2, 'form': form, 'submitted': submitted})
