#A view in a django project is something the user may want to see


from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import markdown2
from . import util
from urllib.parse import urlparse
from urllib.parse import parse_qs
from django import forms
import random


class NewPageForm(forms.Form):
    pageName = forms.CharField(label="Enter Page Name",min_length=2,widget=forms.TextInput(attrs={'class':'form-control'}))
    pageMarkdown = forms.CharField(label="Enter the Page's Markdown Code",widget=forms.Textarea(attrs={'class':'form-control'}))
    def clean(self):
        cd = self.cleaned_data
        for e in util.list_entries():
            if cd.get('pageName').lower() == e.lower():
                raise forms.ValidationError('Page Name Already Exists, Try entering a different page name')
        return cd

class EditPageForm(forms.Form):
    pageMarkdown = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label="Edit Markdown for the page below:")
    


#the request argument represents the http request that the user makes while browsing the site
#so in this example when loading up the website for the first time the user will try to access the home page
#this will create a request and we will process this request in the function "index" below.
#To specify which functions to run when specific urls are accessed, we use urls.py
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):

    try:
        return render(request, "encyclopedia/entry.html", {
        "markdownEntry" : markdown2.markdown(util.get_entry(entry)),"request":entry
        })
    except:
        return render(request, "encyclopedia/error.html",{"request":entry
        })

        
def search(request):
    entry = request.GET.get('q','') 
    for e in util.list_entries():
        if entry == e.lower():
            return HttpResponseRedirect("/wiki/"+entry)

    
    entry = request.GET.get('q','') 
    newlist = []
    for e in util.list_entries():
        if entry in e.lower():
            newlist.append(e)
    return render(request, "encyclopedia/search.html",{"request":entry, "entries": newlist
        })
    
            
def new(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():

            util.save_entry(form.cleaned_data["pageName"], form.cleaned_data["pageMarkdown"])
            return HttpResponseRedirect("/wiki/"+form.cleaned_data["pageName"])
        
        else:
            if util.get_entry(form.cleaned_data["pageName"]):
                 #form.errors.get('duplicate')
                 return render(request, "encyclopedia/new.html"
                   , {"form": form})
                 #return render(request, "encyclopedia/error2.html",{"request":form.cleaned_data["pageName"]})

   
    return render(request, "encyclopedia/new.html"
                   , {"form": NewPageForm()})

def rndm(request):
    entries = util.list_entries()
    entry = random.choice(entries)
    return HttpResponseRedirect("/wiki/"+entry)

def edit(request, entry):
    if request.method == "POST":
        form = EditPageForm(request.POST)
        if form.is_valid():
            util.save_entry(entry, form.cleaned_data["pageMarkdown"])
            return HttpResponseRedirect("/wiki/"+entry)
        
        else:
            return render(request, "encyclopedia/error2.html",{"request":form.cleaned_data["pageName"]})
    f = EditPageForm(initial={'pageName':entry, 'pageMarkdown':util.get_entry(entry)})
     
    return render(request, "encyclopedia/edit.html"
                   , {"form": f})
