from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.

def index(request):

    # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    # Skills
    categories = Category.objects.all()

    # Portfolio
    portfolios = Portfolio.objects.all()

    # Contact
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')

        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.save()



    context = {
        'home' : home,
        'about' : about,
        'profiles' : profiles,
        'categories' : categories,
        'portfolios' : portfolios,
    }


    return render(request, 'index.html', context)
