"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Register url patterns from project.urls
    # Accessed when prefixed by projects
    path('projects/', include('projects.urls')),
    path('blog/', include('blog.urls')),
    path('', include('me.urls')),
    path('resume/', include('resume.urls')),
    path('contact/', include('contact.urls')),
    path('in_progress', include('in_progress.urls')),
    path('contact_me/', include('contact_me.urls')),
]
