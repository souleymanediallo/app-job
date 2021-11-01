from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("new/", views.JobCreateView.as_view(), name="job-create"),
    path("job-detail/<slug>/<int:pk>/", views.JobDetailView.as_view(), name="job-detail"),
]