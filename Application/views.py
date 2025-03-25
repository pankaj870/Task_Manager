from django.shortcuts import render
from django.http import HttpResponse,HttpRequest ,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from . import models

# Create your views here.

def index(request):
    temp = loader.get_template('index.html')
    return HttpResponse(temp.render())


# this is only for the data insertion
def data_collection(request:HttpRequest):
    all_tasks = models.task_manager.objects.all()

    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        discription = request.POST.get('discription')
        status = request.POST.get('status')
        # date_time = request.POST.get('data_time')
        models.task_manager(id,name,discription,status).save()

    return render(request,'website/data_collection.html',{'all_task' : all_tasks})


# previews details of task
def data_table(request,id):
    data = models.task_manager.objects.get(id=id)
    print(data)
    return render(request,'website/task_over_view.html',{'task':data})


# deletion in database - task_manager
def delete_task(request,id):
    instance=models.task_manager.objects.filter(id=id)
    instance.delete()
        
    return HttpResponseRedirect(reverse('data_collection'))


# updation in database - task_manager
def update_task(request:HttpRequest,id):
    if request.method=="POST" :
        discription = request.POST.get('up_discription')
        status = request.POST.get('up_status')
        model = models.task_manager.objects.get(id=id)
        model.discription = discription
        model.status = status
        model.save()
    return HttpResponseRedirect(reverse('data_collection'))

        