from django.urls import path
from . import views


urlpatterns = [
    # Hook up root of project to project_index from views file
    path('', views.contact_me, name='contact_me'),
]