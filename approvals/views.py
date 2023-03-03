# approvals/views.py

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import logout

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
    else:
        # If the request is not a POST request, just render the logout template
        return render(request, 'auth/logout.html')

def index(request):
    return render(request, 'index.html')

@login_required
def manage_notices(request):
    return render(request, 'manage_notices.html')

@user_passes_test(lambda u: u.is_superuser)
def manage_users_groups(request):
    return render(request, 'manage_users_groups.html')

def create(request):
    # TODO: Implement create view
    pass