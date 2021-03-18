from django.urls import path
from . import views


urlpatterns = [
    # Hook up root of project to project_index from views file
    path('', views.in_progress, name='in_progress'),

    path('<int:pk>/', views.in_progress_detail, name='in_progress_detail')

]