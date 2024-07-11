from django.shortcuts import render
from django.http import HttpResponse
from .models import Skill
from django.views.generic.list import ListView


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the index.")


def app(request):
    all_skills = Skill.objects.all()
    output = ", ".join(s.name for s in all_skills)
    return HttpResponse(output)
