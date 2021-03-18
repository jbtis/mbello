from django.shortcuts import render
from me.models import Introduction


def about_me(request):
    introduction = Introduction.objects.all()
    context = {
        'introduction': introduction,
    }
    return render(request, 'about_me.html', context)
