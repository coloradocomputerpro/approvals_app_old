# approvals/views.py

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages



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
    context = {"requests": requests}
    return render(request, "index.html", context)


@login_required
def manage_notices(request):
    return render(request, "manage_notices.html")


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from approvals.models import Request


@method_decorator(login_required, name="dispatch")
class RequestCreateView(LoginRequiredMixin, CreateView):
    model = Request
    fields = ["title", "description", "program"]
    template_name = "approvals/request_create.html"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("approvals:index")

    def get_context_data(self, **kwargs):
        context = super(RequestCreateView, self).get_context_data(**kwargs)
        context["programs"] = Program.objects.all()
        return context


from django.views.generic.detail import DetailView


class RequestDetailView(DetailView):
    model = Request
    template_name = "approvals/request_detail.html"


from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User


class RequestUpdateView(UpdateView):
    model = Request
    fields = ["title", "description", "status", "program"]
    template_name = "approvals/request_update.html"
    success_url = reverse_lazy("approvals:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["programs"] = Program.objects.all()
        context["all_users"] = User.objects.all()
        context['assigned_users'] = self.object.assigned_to.all()
        return context


from django.views.generic.list import ListView


class RequestListView(ListView):
    model = Request
    template_name = "approvals/request_list.html"
    context_object_name = "requests"


from .models import Program


class ProgramDetailView(DetailView):
    model = Program
    template_name = "approvals/program_detail.html"


from django.views.generic.list import ListView
from approvals.models import Program


class ProgramListView(ListView):
    model = Program
    template_name = "approvals/program_list.html"


from django.views.generic import CreateView
from .models import Program


class ProgramCreateView(CreateView):
    model = Program
    fields = ["name", "description"]
    template_name = "approvals/program_form.html"


from django.urls import reverse_lazy

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})


from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from .models import Request


class RequestDeleteView(LoginRequiredMixin, DeleteView):
    model = Request
    template_name = "approvals/request_delete.html"
    success_url = reverse_lazy("approvals:request_list")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.views import View


class ManageUsersAndGroupsView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser
    
    def get(self, request):
        users = User.objects.all()
        groups = Group.objects.all()
        return render(
            request,
            "admin/manage_users_groups.html",
            {"users": users, "groups": groups},
        )

    def post(self, request):
        user_id = request.POST.get("user_id")
        group_id = request.POST.get("group_id")
        action = request.POST.get("action")

        if action == "add":
            user = User.objects.get(id=user_id)
            group = Group.objects.get(id=group_id)
            user.groups.add(group)
            return redirect("approvals:manage_users_groups")
        elif action == "remove":
            user = User.objects.get(id=user_id)
            group = Group.objects.get(id=group_id)
            user.groups.remove(group)
            return redirect("approvals:manage_users_groups")

from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import UpdateView

class UserUpdateView(UserPassesTestMixin, UpdateView):
    def test_func(self):
        return self.request.user.is_superuser
    
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    template_name = 'admin/edit_user.html'
    success_url = reverse_lazy('approvals:manage_user_groups')

from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import DeleteView

class UserDeleteView(UserPassesTestMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_superuser
    
    model = User
    template_name = 'admin/delete_user.html'
    success_url = reverse_lazy('approvals:manage_user_groups')

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

class UserCreateView(CreateView):
    model = User
    fields = ['username', 'email', 'password']
    template_name = 'admin/create_user.html'
    success_url = reverse_lazy('approvals:manage_users_groups')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'User created successfully.')
        return response