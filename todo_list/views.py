from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_item  = List.objects.all()
            messages.success(request, ('Item has been Added Successfuly'))
            return render(request, 'home.html', {'all_items': all_item})
    else:
        all_items = List.objects.all()
        return render(request, 'home.html', {'all_items' : all_items })

def about(request):
    return render(request, 'about.html', {})

def delete(request, list_id):
    item_del = List.objects.get(pk=list_id)
    item_del.delete()
    messages.success(request, ('Item has been Deleted Successfully'))
    return redirect('home')

def completed(request, list_id):
    item_completed = List.objects.get(pk = list_id)
    item_completed.completed = True
    item_completed.save()
    return redirect('home')

def uncompleted(request, list_id):
    item_uncompleted = List.objects.get(pk = list_id)
    item_uncompleted.completed = False
    item_uncompleted.save()
    return redirect('home')

def edit(request, list_id):
    if request.method =='POST':
        item = List.objects.get(pk = list_id)
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ("Item has been Edited"))
            return redirect('home')
    else:
        item = List.objects.get(pk = list_id)
        return render(request, 'edit.html', {'item': item})