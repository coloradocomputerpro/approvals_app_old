# approvals/views.py

from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib.auth.forms import AuthenticationForm


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


from django.contrib.auth import logout


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("index")
    else:
        # If the request is not a POST request, just render the logout template
        return render(request, "auth/logout.html")


def index(request):
    requests = Request.objects.all()
    context = {'requests': requests}
    return render(request, 'index.html', context)


@login_required
def manage_notices(request):
    return render(request, "manage_notices.html")


@user_passes_test(lambda u: u.is_superuser)
def manage_users_groups(request):
    return render(request, "manage_users_groups.html")


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from approvals.models import Request


@method_decorator(login_required, name='dispatch')
class RequestCreateView(LoginRequiredMixin, CreateView):
    model = Request
    fields = ['title', 'description']
    template_name = 'approvals/request_create.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('approvals:index')


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


from django.urls import reverse_lazy

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
