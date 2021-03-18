from django.urls import path
from . import views

# Generates urlpatterns for current app. Note this is tightly coupled with views file
# Since we are calling functions from there
urlpatterns = [

    # Hook up root of project to project_index from views file
    path('', views.about_me, name='about_me'),

]