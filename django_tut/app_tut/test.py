# https://djangobook.com/mdj2-django-forms/
from django import forms

class Fooform(forms.Form):
    btn = forms.CharField()

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .temp import *
import time

def inputval(request):
    if request.method == 'POST':
        form = Fooform(request.POST)
        if form.is_valid():
            print(request.POST, request.POST["btn"])

            val = form.cleaned_data.get("btn")
            print(val)
            time.sleep(2)
    else:
        form = Fooform()
    return render(request, 'app_tut/test.html', locals())
