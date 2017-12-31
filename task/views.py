from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import UserForm

def home(request):
	if not request.user.is_authenticated():
		return render(request, 'task/login.html')
	else:
		return render(request, "task/home.html")

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'task/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'task/home.html')
            else:
                return render(request, 'task/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'task/login.html', {'error_message': 'Invalid login'})
    return render(request, 'task/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'task/home.html')
    context = {
        "form": form,
    }
    return render(request, 'task/register.html', context)