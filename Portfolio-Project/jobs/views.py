from django.shortcuts import render, get_object_or_404
from .models import Job
from .models import Project
from .models import Skill
from .models import Certificates
import os
from django.http import HttpResponse
from django.conf import settings
# Create your views here.
def homepage(request):
    skills = Skill.objects
    return render(request,"jobs/home.html",{'skills':skills})

def detail(request,job_id):
    job_detail = get_object_or_404(Job,pk = job_id)

    return render(request,'jobs/detail.html',{'job_detail':job_detail})

def projects(request):
    projects = Project.objects

    return render(request,"jobs/projects.html",{'projects':projects,'home_link':'home'})


def certificates(request):
    certificates = Certificates.objects
    return render(request,"jobs/certificates.html",{'certificates':certificates,'home_link':'home'})

def skills(request):
    skills = Skill.objects
    return render(request,"jobs/skills.html",{"skills":skills})



def my_cv(request):
    return render(request,"jobs/my_cv.html")