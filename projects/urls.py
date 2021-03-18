from django.urls import path
from . import views

# Generates urlpatterns for current app. Note this is tightly coupled with views file
# Since we are calling functions from there
urlpatterns = [

    # Hook up root of project to project_index from views file
    path("", views.project_index, name="project_index"),

    # Hook up the number since every project has a different page
    # Dynamic url name generation, depending on how many projects
    path("<int:pk>/", views.project_detail, name="project_detail"),
]