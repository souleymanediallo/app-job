from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name="register"),
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('profile-employee/<int:pk>/', views.EmployeeProfileView.as_view(), name="profile-employee"),
    path('profile-job-list/', views.EmployerPostedJobsView.as_view(), name="profile-job-list"),
]
