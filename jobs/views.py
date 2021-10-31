from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Job, Category

# Create your views here.


class HomeView(ListView):
    model = Job
    context_object_name = "jobs"
    template_name = "jobs/index.html"
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context