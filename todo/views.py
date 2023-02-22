from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Todo, Priority, Status
from .forms import TodoForm


# Create your views here.
def index(request):
    return render(request, 'todo/index.html')



def userRegister(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User successfully signup.')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('user_profile')

        else:
            messages.warning(request, 'Invalid username or password.')
            return render(request, 'todo/signup.html', {'form':form})

    else:
        form = RegistrationForm()
    return render(request, 'todo/signup.html', {'form':form})


def userLogin(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'User successfully signin.')
            return redirect('user_profile')
        else:
            messages.warning(request, 'Invalid username or password.')
            return render(request, 'todo/login.html', {'form':form})

    # else:
    #     form = AuthenticationForm()
    return render(request, 'todo/login.html', {'form':form})


@login_required
def userLogout(request):
    logout(request)
    messages.warning(request, 'User successfully logout.')
    return redirect('home')

@login_required
def userChangePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('user_login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'todo/change_password.html', {'form': form})


@login_required
def userProfile(request):
    return render(request, 'todo/profile.html')


@login_required
def create_todo(request):
    if request.user.is_authenticated:
        user = request.user
        form = TodoForm(request.POST or None)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect('todo-list')
    return render(request, 'todo/create_todo.html', {'form': form})


@login_required
def list_todo(request):
    if request.user.is_authenticated:
        user = request.user
        todos = Todo.objects.filter(user=user)
    return render(request, 'todo/list_todo.html', {'todos': todos})




@login_required
def update_todo(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('todo-list')
    return render(request, 'todo/update_todo.html', {'form': form, 'todo': todo})


@login_required
def delete_todo(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo-list')
    return render(request, 'todo/delete_todo.html', {'todo': todo})


def search(request):
    if request.GET.get('search'): # write your form name here      
        search =  request.GET.get('search')      
        try:
            if request.user.is_authenticated:
                todos = Todo.objects.filter(title__icontains=search, user=request.user)
                return render(request,"todo/search.html",{"todos":todos})
            else:
                todos = Todo.objects.filter(title__icontains=search)
                return render(request,"todo/search.html",{"todos":todos})
        except:
            return render(request,"todo/search.html",{"todos":todos})
    else:
        return render(request,"todo/search.html",{"todos":todos})

