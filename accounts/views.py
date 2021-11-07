from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, TemplateView, DetailView, UpdateView, ListView
from .models import CustomUser, Profile
from .forms import CustomUserForm
from jobs.models import Job


# Create your views here.
class UserRegisterView(SuccessMessageMixin, CreateView):
    form_class = CustomUserForm
    template_name = "accounts/register.html"
    success_url = "/"
    success_message = "Votre compte a été crée !"

    def form_valid(self, form):
        user = form.save(commit=False)
        user_type = form.cleaned_data['user_type']
        if user_type == "is_employee":
            user.is_employee = True
        elif user_type == "is_employer":
            user.is_employer = True
        user.save()

        return redirect(self.success_url)


class EmployeeProfileView(DetailView):
    template_name = "accounts/profile_employee.html"
    model = CustomUser

    def get_context_data(self, **kwargs):
        context = super(EmployeeProfileView, self).get_context_data(**kwargs)
        context["account"] = get_object_or_404(CustomUser, pk=self.kwargs['pk'])
        context["profile"] = get_object_or_404(Profile, user_id=self.kwargs['pk'])
        return context


class EmployerPostedJobsView(ListView):
    model = Job
    template_name = "accounts/job_employer_list.html"
    paginate_by = 3

    def get_queryset(self):
        return Job.objects.filter(employer=self.request.user).order_by("-id")