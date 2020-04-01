from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html') 

def baja(request):
    return render(request,'baja.html')