from django.shortcuts import render
from contact.models import Contacts


def contact(request):
    contacts = Contacts.objects.all()
    context = {
        'contacts': contacts,
    }
    return render(request, 'contact.html', context)
