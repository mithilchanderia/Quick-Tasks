from django.shortcuts import render,redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    if(request.method=='POST'):
        form=ListForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,('Task has been added to the list!'))
            list_items=List.objects.all()
            return render(request,'home.html',{'list_items':list_items})
    else:
        list_items=List.objects.all()
        return render(request,'home.html',{'list_items':list_items})

def about(request):
    return render(request,'about.html',{})

def delete(request,list_id):
    item=List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item has been deleted'))
    return redirect('home')

def cross_off(request,list_id):
    item=List.objects.get(pk=list_id)
    item.status=False
    item.save()
    return redirect('home')

def cross_on(request,list_id):
    items=List.objects.get(pk=list_id)
    items.status=True
    items.save()
    return redirect('home')

def edit(request,list_id):
    if(request.method=='POST'):
        item=List.objects.get(pk=list_id)
        form=ListForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            messages.success(request,('Task has been edited!'))
            return redirect('home')
    else:
        list_items=List.objects.get(pk=list_id)
        return render(request,'edit.html',{'list_items':list_items})
