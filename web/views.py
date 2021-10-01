from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'index.html',{'name':'Rashedul','salary':'$235346','job':'Web Developer'})