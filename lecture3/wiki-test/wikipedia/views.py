from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
   #return HttpResponse("Hello")
    return render(request, "wikipedia/index.html")
def entryPage(request, TITLE):
    #return HttpResponse(f"Hello, {TITLE.capitalize()}!")
    return render(request, "wikipedia/entryPage.html", {"TITLE": TITLE.capitalize()})

