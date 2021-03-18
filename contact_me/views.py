from django.shortcuts import render
from contact_me.models import ContactMe


# Create your views here.
def contact_me(request):
    items = ContactMe.objects.all()
    context = {
        'items':items,
    }
    return render(request, 'contact_me.html', context)
