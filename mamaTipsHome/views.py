from django.shortcuts import render

# Create your views here

def home(request):

    c = {'r': 10, 'ty': 'This is cool'}
    return render(request,'mamatipshome/home.html', c)