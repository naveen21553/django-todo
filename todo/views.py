from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    #return render(request, 'index.html', {})

    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('Item has been added to List!'))
            return render(request, 'index.html', {'all_items': all_items})

    else:
        all_items = List.objects.all
        return render(request, 'index.html', {'all_items': all_items})


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item deleted successfully!'))
    return redirect('index')

def check(request, list_id):
    item = List.objects.get(pk = list_id)
    item.completed = True
    item.save()
    return redirect('index')

def uncheck(request, list_id):
    item = List.objects.get(pk = list_id)
    item.completed = False
    item.save()
    return redirect('index')

def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk = list_id)
        
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item edited successfully!'))
            return redirect('index')

    else:
        item = List.objects.get(pk = list_id)
        return render(request, 'edit.html', {'item':item})
