from django.shortcuts import render
from django.contrib.auth.models import AnonymousUser, User, auth

# Create your views here.
def index(request):
    context = {
        
    }
    return render(request, 'index.html', context)

