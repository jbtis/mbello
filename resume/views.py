from django.shortcuts import render


def web_resume(request):
    # Don't really need to send a context, resume can be hardcoded and changed in html
    return render(request, 'web_resume.html', {})
    


