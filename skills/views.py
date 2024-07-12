from django.shortcuts import render
from django.http import HttpResponse
from .models import Skill
from django.views import generic
from django.db.models import F

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the index.")


class appView(generic.ListView):
    model = Skill
    context_object_name = "all_skills"
    template_name = "skills/app.html"
