from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Job

# Create your views here.


class HomeView(ListView):
    model = Job
    context_object_name = "jobs"
    template_name = "jobs/index.html"