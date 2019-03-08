from django.shortcuts import render

# Create your views here.
def woda(request):
    return render(request, 'woda_czy_las/woda.html')

def las(request):
    return render(request, 'woda_czy_las/las.html')

def home(request):
    return render(request, 'woda_czy_las/home.html')