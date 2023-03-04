# approvals/views.py

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Request
from .forms import RequestForm


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")
    else:
        form = AuthenticationForm()
    return render(request, "auth/login.html", {"form": form})


from django.shortcuts import render, redirect
from django.contrib.auth import logout


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("index")
    else:
        # If the request is not a POST request, just render the logout template
        return render(request, "auth/logout.html")


def index(request):
    return render(request, "index.html")


@login_required
def manage_notices(request):
    return render(request, "manage_notices.html")


@user_passes_test(lambda u: u.is_superuser)
def manage_users_groups(request):
    return render(request, "manage_users_groups.html")


def create(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            # Check if request already exists
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            existing_request = Request.objects.filter(title=title, description=description).first()
            if existing_request:
                # Redirect to existing request
                return redirect('approvals:detail', existing_request.pk)

            # Create new request
            request_obj = form.save()
            return redirect('approvals:detail', request_obj.pk)
    else:
        form = RequestForm()

    return render(request, 'approvals/request_create.html', {'form': form})


class RequestCreateView(CreateView):
    model = Request
    form_class = RequestForm
    success_url = reverse_lazy('approvals:index')
    template_name = 'approvals/request_create.html'

    def form_valid(self, form):
        # Check if request already exists
        title = form.cleaned_data.get('title')
        description = form.cleaned_data.get('description')
        existing_request, created = Request.objects.get_or_create(title=title, description=description)

        if created:
            # New request created
            return super().form_valid(form)
        else:
            # Request already exists
            return redirect('approvals:detail', existing_request.pk)


from django.views.generic.detail import DetailView


class RequestDetailView(DetailView):
    model = Request
    template_name = "approvals/request_detail.html"


from django.views.generic.edit import UpdateView


class RequestUpdateView(UpdateView):
    model = Request
    fields = ["title", "description", "status"]
    template_name = "approvals/request_update.html"
    success_url = reverse_lazy("index")


from django.views.generic.list import ListView


class RequestListView(ListView):
    model = Request
    template_name = "approvals/request_list.html"
    context_object_name = "requests"

from .models import Program

class ProgramDetailView(DetailView):
    model = Program
    template_name = 'approvals/program_detail.html'
    
from django.views.generic.list import ListView
from approvals.models import Program

class ProgramListView(ListView):
    model = Program
    template_name = 'approvals/program_list.html'

from django.views.generic import CreateView
from .models import Program

class ProgramCreateView(CreateView):
    model = Program
    fields = ['name', 'description']
    template_name = 'approvals/program_form.html'
