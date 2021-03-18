from django.shortcuts import render
from in_progress.models import ProjectsInProgress


def in_progress(request):
    projects_in_progress = ProjectsInProgress.objects.all()
    context = {
        'projects_in_progress': projects_in_progress,
    }
    return render(request, 'in_progress.html', context)


def in_progress_detail(request, pk):
    project_in_progress = ProjectsInProgress.objects.get(pk=pk)
    context = {
        'project': project_in_progress,
    }
    return render(request, 'in_progress_detail.html', context)
