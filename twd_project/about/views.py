from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    context_dict = {'myname':'LORIS'}
    return render(request, 'rango/about.html',context_dict)
