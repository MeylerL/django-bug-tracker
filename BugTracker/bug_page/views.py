from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import BugDetail
from .forms import UserForm, BugForm


def index(request):
    return render(request, 'index.html')

def user_form(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data = request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=True)
            user.set_password(user.password)
            user.save()
            registered = True
            return index(request)

        else:
            print(user_form.errors)
            return HttpResponse("An internal error has occurred")

    else:
        user_form = UserForm()

    return render(request, 'bug_page/user_form.html', {'user_form': user_form, 'registered': registered})

def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('index'))

        else:
            return HttpResponse("Invalid login")

    else:
        return render(request, 'bug_page/user_login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def bug_table(request):
    bugs = BugDetail.objects.all()
    return render(request, 'bug_page/bug_table.html', {'bugs': bugs})

@login_required
def bug_form(request):

        form = BugForm(request.POST)

        if form.is_valid():
            bug = form.save(commit=False)
            bug.author = request.user
            bug.save()
            return HttpResponseRedirect(reverse('index'))

        else:
            form = BugForm()

            return render(request, 'bug_page/bug_form.html', {'bug_form': form})


@login_required
def update_bug(request, pk):
    bug = BugDetail.objects.get(pk=pk)

    if request.user.role == 'developer':
        if request.method == 'POST':
            form = BugForm(request.POST, instance=bug)

            if form.is_valid():
                bug = form.save()
                return HttpResponseRedirect('bug_page/bug_table.html')

        else:
            form = BugForm(instance=bug)

        return render(request,'bug_page/update_bug.html', {'form': form})

    else:

        return HttpResponseRedirect('bug_page/bug_table.html')
