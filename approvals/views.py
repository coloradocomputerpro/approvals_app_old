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

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Request

class RequestCreateView(CreateView):
    model = Request
    fields = ['title', 'description']
    template_name = 'approvals/request_create.html'
    success_url = reverse_lazy('index')

from django.views.generic.detail import DetailView

class RequestDetailView(DetailView):
    model = Request
    template_name = 'approvals/request_detail.html'

from django.views.generic.edit import UpdateView

class RequestUpdateView(UpdateView):
    model = Request
    fields = ['title', 'description', 'status']
    template_name = 'approvals/request_update.html'
    success_url = reverse_lazy('index')

from django.views.generic.list import ListView

class RequestListView(ListView):
    model = Request
    template_name = 'approvals/request_list.html'
    context_object_name = 'requests'
