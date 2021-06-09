# from django.contrib import admin
from django.urls import path#, include
from . import views

# urlpatterns = [
#     path('', views.home, name="app_tut-home"),
#     path('about/', views.about, name="app_tut-about"),
# ]



# from . import contact
from . import pybase
from . import anime
from . import test
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    path('', views.home, name="app_tut-home"),
    path('about/', views.about, name="app_tut-about"),
    # path('python_base/', views.python_base, name="app_tut-python_base"),
    path('pybase/', pybase.inputval, name='pybase'),
    path('anime/', anime.inputval, name='anime'),
    path('anime-load/', anime.load, name='anime-load'),
    path('test/', test.inputval, name='test'),
    # url(r'^admin/', admin.site.urls),
    # url(r'^$', views.button),
    # url(r'^output', views.output,name="script"),
    # url(r'^external', views.external),
]

# from . import webapp
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^$', webapp.button),
#     url(r'^output', webapp.output,name="script"),
# ]
