from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('hello/',hello1,name='hello'),
    path('',NewHomepage,name='NewHomepage'),
    path('travelpackage/',travelpackage,name='travelpackage'),
    path('print/',print_to_console,name='print_to_console'),
    path('p/',print1,name='print1'),
    path('randomcall/',randomcall , name='randomcall'),
    path('randomlogic/', randomlogic, name='randomlogic'),
    path('getdate1/',getdate1,name='getdate1'),
    path('get_date/',get_date,name='get_date'),
    path('register/',register,name='register'),
    path('Registerpage/',Registerpage,name='Registerpage'),
    path('pie_chart/',pie_chart,name='pie_chart'),
    path('carcards/', carcards, name='carcards'),
    path('weatherpagecall/', weatherpagecall, name='weatherpagecall'),
    path('weatherlogic/', weatherlogic, name='weatherlogic'),
    path('Feedbackcall/', Feedbackcall, name='Feedbackcall'),
    path('Feedbackform/', Feedbackform, name='Feedbackform'),
    path('login/', login, name='login'),
    path('login1/', login1, name='login1'),
    path('signup/', signup, name='signup'),
    path('signup1/', signup1, name='signup1'),
    path('logout/', logout, name='logout'),






]