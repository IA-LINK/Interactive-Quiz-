from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,'welcome.html') #we have to use render funtion to request the webpages from templates