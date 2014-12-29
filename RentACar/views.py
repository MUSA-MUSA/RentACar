from django.shortcuts import render, render_to_response,RequestContext
from django.template import RequestContext
from cars.models import Car
import searchengine
from cars.forms import QuestinForm
#Create your views here.
def home1(request):
    templates="home1.html"
    return render(request, templates )
def result(request):
    d=dict()
    search_text=request.GET.get('q','')
    print search_text
    res=searchengine.return_results(search_text)
    d["results"]=res
    return render_to_response("result.html",d,context_instance=RequestContext(request))
def about(request):
    templates="about.html"
    return render(request, templates )

def navbar(request):
    template='navbar.html'
    return render(request, template)

def register(request):
    remplate='register.html'
    return render(request, remplate)
def rent(request):
    template='rent.html'
    return render(request, template)
def add_Question(request):
    form=QuestinForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(comit=False)
        save_it.save()

    return  render_to_response("about",
                               locals(),
                               context_instance=RequestContext(request))




