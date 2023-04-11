from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList
from .forms import TodoListForm, TodoListUpdateForm
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.views.generic import FormView, ListView, CreateView,DeleteView,UpdateView
from django.views.generic.edit import FormMixin



# Create your views here.

@login_required(login_url='account/login')
def home(request):
    task_list = TodoList.objects.filter(user=request.user)
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            slug = slugify(form.cleaned_data['task'])
            task.user = request.user
            task.slug = slug
            task.save()
            return redirect('todo:home')
    form = TodoListForm()
    context = {
        "form":form,
        'task_list':task_list,
    }
    return render(request, 'todo/index.html', context)


def update_task(request, slug):
    tasks = TodoList.objects.get(slug=slug, user=request.user)
    form = TodoListUpdateForm(request.POST or None, instance=tasks)
    if form.is_valid():
        form.save()
        return redirect('todo:home')
    return render(request, 'todo/update.html',{'form':form})

def delete_task(request,slug):
    task = TodoList.objects.get(slug=slug, user=request.user)
    task.delete()
    return redirect('todo:home')