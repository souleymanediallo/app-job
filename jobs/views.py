from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Job, Category

from .forms import JobFormCreate

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


class JobCreateView(SuccessMessageMixin, CreateView):
    model = Job
    form_class = JobFormCreate
    template_name = "jobs/job_form.html"
    context_object_name = "forms"
    success_url = "/"
    success_message = "Votre annonce a été ajouté !"

    def form_valid(self, form):
        job = form.save(commit=False)
        job.employer = self.request.user
        job.save()
        return super(JobCreateView, self).form_valid(form)


class JobDetailView(DetailView):
    model = Job
    template_name = "jobs/job_detail.html"
    context_object_name = "job"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
