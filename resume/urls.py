from django.urls import path
from resume import views

urlpatterns = [
    path("", views.web_resume, name="web_resume"),
]

