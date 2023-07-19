from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse('This is my Homepage')

def contact(request):
    return HttpResponse('This is my contact page')

def service(request):
    return HttpResponse('This is my service page')

def about(request):
    return HttpResponse('This is my about page')