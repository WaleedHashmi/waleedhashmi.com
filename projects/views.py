from django.shortcuts import render
from django.http import HttpResponse

from .models import Project,Tag,Home

# Create your views here.

def index (request):
    Tags = Tag.objects.all()
    Projects = Project.objects.all()
    return render (request, 'projects/works.html', {'Projects':Projects, 'Tags':Tags})

def home (request):
    Tags = Tag.objects.all()
    Projects = Project.objects.all()
    return render (request, 'index.html', {'Projects':Projects, 'Tags':Tags})

def item (request,id):
    return HttpResponse (id)

