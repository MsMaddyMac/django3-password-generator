from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
  return render(request, 'generator/home.html')

def about(request):
  return render(request, 'generator/about.html')

def password(request):
  
  characters = list('abcdefghijklmnopqrstuvwxyz')
  
  if request.GET.get('uppercase'):
    characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    # If 'uppercase' is checked it will come in the request.GET.get() and the characters.extend() will run to use uppercase letters in list() above
  
  if request.GET.get('special'):
    characters.extend(list('!@#$%^&*()'))
    # If 'special' is checked it will come in the request.GET.get() and the characters.extend() will run to use the special characters in list() above
    
  if request.GET.get('numbers'):
    characters.extend(list('1234567890'))
    # If 'numbers' is checked it will come in the request.GET.get() and the characters.extend() will run to use numbers in list() above
  
  length = int(request.GET.get('length', 12))
  # everything using the name attribute in the form in home.html can be referenced and used here. For instance we gave the select number drop down menu a name='length' which we are now referencing above. Everything returned in request.GET.get() is a string and we need the length to be an int. We then change it to an int by wrapping passing the request inside int(). The number after 'length', is a default value. So if no length is selected 12 will be the default length used. 
  
  thepassword = ''
  
  for x in range(length):
    thepassword += random.choice(characters)
  
  
  return render(request, 'generator/password.html', {'password': thepassword})

# def home(request):
#   return render(request, 'generator/home.html', {'password': 'hingirgnien'})

# you can pass things to be displayed in the home.html in this case it will display the value of the dictionary password key above