from django.urls import path
from django.views.generic import TemplateView
from .views import ProjectDetailView

app_name = 'projects'

urlpatterns = [
    path('', TemplateView.as_view(template_name='projects/home.html'), name='home'),
    path('projects/<int:project_id>/', ProjectDetailView.as_view(), name='project-detail'),
]
