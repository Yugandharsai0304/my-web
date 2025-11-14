from django.urls import path
from .views import *

app_name='page'

urlpatterns=[
    path('',home,name='home'),

    path('waffle/',waffle,name='waffle'),
    path('creambars/',creambars,name='creambars'),
    path('minibites/',minibites,name='minibites'),
    path('lowcal/',lowcal,name='lowcal'),
    path('details/<int:id>/',details,name='details'),
    path('aboutus/',aboutus,name='aboutus'),


    
    path('bars/',bars,name='bars'),
    path('pop/',pop,name='pop'),
    path('bites/',bites,name='bites'),
    path('desserts/',desserts,name='desserts'),
    path('cakes/',cakes,name='cakes'),
]