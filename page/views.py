from django.shortcuts import render
from .models import *
from .forms import *


# Create your views here.
def home(request):
    data=list.objects.all()
    data1=delights.objects.all()
    data2=popsicles.objects.all()
    data3=cheese.objects.all()
    return render(request,'home.html',{'data':data,'data1':data1,'data2':data2,'data3':data3})


# ice cream library         
def waffle(request):
    products = Product.objects.filter(cid=1)
    return render(request,'project.html',{'products':products})
def creambars(request):
    products2 = Product.objects.filter(cid=2)
    return render(request,'icecreambar.html',{'products2':products2})
def minibites(request):
    products3 = Product.objects.filter(cid=3)
    return render(request,'minibites.html',{'products3':products3})
def lowcal(request):
    products4 = Product.objects.filter(cid=4)
    return render(request,'lowcal.html',{'products4':products4})



def details(request,id):
    product = Product.objects.get(pid=id)
    return render(request,'detailedpage.html',{'product':product})
def aboutus(request):
    return render(request,'aboutus.html')


def bars(request):
    return render(request,'bars.html')
def pop(request):
    return render(request,'pop.html')
def bites(request):
    return render(request,'bites.html')
def desserts(request):
    return render(request,'desserts.html')
def cakes(request):
    return render(request,'cakes.html')