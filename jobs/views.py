from django.shortcuts import render, get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Job, Category
from django.db.models import Q

from .forms import JobFormCreate, JobFormUpdate

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


class JobListView(ListView):
    model = Job
    template_name = "jobs/job_list.html"
    context_object_name = "jobs"
    paginate_by = 3

    def get_context_data(self, **kwargs):
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


class CategoryViewDetail(ListView):
    model = Job
    template_name = "jobs/category_detail.html"
    context_object_name = "jobs"
    paginate_by = 2
    
    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs["pk"])
        return Job.objects.filter(category=self.category)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        self.category = get_object_or_404(Category, pk=self.kwargs["pk"])
        context["categories"] = Category.objects.all()
        context["category"] = self.category
        return context


class SearchListView(ListView):
    model = Job
    context_object_name = "job"
    template_name = "jobs/search.html"

    def get_queryset(self):
        q1 = self.request.GET.get("job_title")
        q2 = self.request.GET.get("Job_type")
        q3 = self.request.GET.get("job_location")
        if q1 or q2 or q3:
            return Job.objects.filter(
                Q(title__icontains=q1) | Q(description__icontains=q1),
                job_type=q2, location__icontains=q3
            ).order_by('-id')
        return Job.objects.all().order_by('-id')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["categories"] = Category.objects.all()
        return context


class JobUpdateView(SuccessMessageMixin, UpdateView):
    model = Job
    form_class = JobFormUpdate
    context_object_name = "forms"
    success_url = "/"
    success_message = "Votre annonce a été modifié !"
