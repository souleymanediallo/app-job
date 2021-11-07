from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("job-list/", views.JobListView.as_view(), name="job-list"),
    path("new/", views.JobCreateView.as_view(), name="job-create"),
    path("job-detail/<slug>/<int:pk>/", views.JobDetailView.as_view(), name="job-detail"),
    path("category/<slug>/<int:pk>/", views.CategoryViewDetail.as_view(), name="category-detail"),
    path("search/", views.SearchListView.as_view(), name="search"),
]