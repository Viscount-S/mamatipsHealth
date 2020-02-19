from django.shortcuts import render

# Create your views here

def home(request):

    c = {'r': 10, 'ty': 'This is cool'}
    return render(request,'mamatipshome/fromGit.html', c)

def spoilt(request):

    return render(request,'mamatipshome/broken.html', context = None)