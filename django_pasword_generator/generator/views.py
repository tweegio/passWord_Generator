
from django.shortcuts import render
from django.http import HttpResponse 
import random

# Create your views here.

def styles(request):
    
    return render(request,'generator/styles.css')

def about(request):
    
    return render (request,'generator/about.html')

def home(request):
    
    return render(request,'generator/Home.html')

def password(request):
    

    
    generated_password = ""
    
    characters = list('abcdefghijklmnñopqrstuvwxyz')

    length= int(request.GET.get('length'))
    
    if request.GET.get('uppercase'):
        
        characters.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')) 
        
    if request.GET.get('special'):
        
        characters.extend(list('-_+*@$%&()')) 
        
             
    if request.GET.get('numbers'):
        
        characters.extend(list('0123456789'))
    
    
    for x in range(length):
        generated_password += random.choice(characters)
        
    
    return render(request,'generator/password.html', {'password': generated_password})