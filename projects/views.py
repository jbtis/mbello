from django.shortcuts import render
from projects.models import Project


def project_index(request):

    # Query to retrieve a Queryset of all project objects from the database
    # In previous example, {} was an empty dictionary!
    projects = Project.objects.all()
    context = {
        'projects': projects
    }

    # Objects from database passed as values in context dictionary
    return render(request, 'project_index.html', context)


def project_detail(request, pk):

    # Retrieve primary key of objects TODO: used for url indexing?
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

