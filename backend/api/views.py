from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def api_home(rquest,*args,**kwargs):
    return( JsonResponse({'message': "Hey there whats up"}))