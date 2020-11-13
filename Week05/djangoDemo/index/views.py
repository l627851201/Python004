from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello Django Demo!")

def year(request, year):
    return HttpResponse(year)
    return redirect("/2099.html")

def year_diy(request, year):
    return HttpResponse(year)

def name(request, **kwargs):
    return HttpResponse(kwargs['name'])

# templates，不明白
def myyear(request, year):
    return render(request, 'yearview.html')
