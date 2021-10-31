from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from .models import CustomUser
from .forms import CustomUserForm


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

