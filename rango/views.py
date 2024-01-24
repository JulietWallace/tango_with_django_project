from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse


#This 
def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)
    #return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About</a>")

def about(request):
    #return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/about.html', context=context_dict)

#def media(request):
    #return HttpResponse("Your media will appear here. <a href='/rango/'>Index</a>")
