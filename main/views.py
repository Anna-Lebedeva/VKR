from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from main.forms import LoginForm


def index(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html")


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'main/index.html', {'form': form})
