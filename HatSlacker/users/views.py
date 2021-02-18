from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

from users.models import User


def hem(request):
    searchterm = request.GET.get('search')

    if searchterm:
        users = User.objects.all().filter(first_name=searchterm)
    else:
        users = User.objects.all()

    context = {
        'users': users,
        'searchterm': searchterm
    }
    return render(request, 'users/dashboard.html', context)


def felbrodyr(request):
    return render(request, 'users/felbrodyr.html')


def minskalager(request):
    return render(request, 'users/minskalager.html')


def nyanvandare(request):
    return render(request, 'users/nyanvandare.html')


