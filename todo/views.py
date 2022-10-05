from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from todo.models import TodoItem
from django.contrib.auth import login, logout
from todo.forms import UserRegistrationForm, TodoForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required #A decorator that allows only authenticated users
def home(request):
    '''
    create todo items
    '''
    if request.method == "POST":
        todo_name = request.POST.get("new-todo")
        todo = TodoItem.objects.create(name=todo_name, user=request.user)
        return redirect("home")
        
    '''
    retrieve the todo items of this user which are not completed

    '''
    todos = TodoItem.objects.filter(user=request.user, is_completed=False).order_by("-id")

    # paginating 4 items per page
    paginator = Paginator(todos, 4)
    
    # URL param for getting the current page number
    page_number = request.GET.get("page")
    
    # retrieving all the todo items for that page
    page_obj = paginator.get_page(page_number)

    context = {"todos":todos, "page_obj":page_obj}
    return render(request, "todo/list.html", context)

def register(request):
    '''
    User Registration Form

    '''
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegistrationForm

    context = {"form":form}
    return render(request, "todo/register.html", context)

def logout_user(request):
    logout(request)
    return redirect("login")

def update_todo(request, pk):
    """
    Update todo item

    """

    todo = get_object_or_404(TodoItem, id=pk, user=request.user) #get_object_or_404() returns a data if exists else status 404 not found
    todo.name = request.POST.get(f"todo_{pk}")
    todo.save()
    # return redirect ("home")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def complete_todo(request, pk):
    """
    Marking a todo item as completed

    """    
    todo = get_object_or_404(TodoItem, id=pk, user=request.user)
    todo.is_completed = True
    todo.save()
    # return redirect("home")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_todo(request, pk):
    """
    Delete todo item

    """    
    todo = get_object_or_404(TodoItem, id=pk, user=request.user)
    todo.delete()
    # return redirect("home")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
