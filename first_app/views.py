from django.shortcuts import render,redirect
from first_app.models import TaskStoreModel
from first_app.forms import TaskStoreForm,TaskCompleteModelForm
from django.views.generic import ListView
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

class TaskFormView(CreateView):
    model = TaskStoreModel
    template_name = 'store_task.html'
    form_class = TaskStoreForm
    success_url = reverse_lazy('taskList')
    
    


class TaskListView(ListView):
    model = TaskStoreModel
    template_name = 'task_list.html'
    context_object_name='data'
    
    
class TaskUpdateView(UpdateView):
    model = TaskStoreModel
    template_name = 'store_task.html'
    form_class = TaskStoreForm
    success_url = reverse_lazy('taskList')
    

class DeleteTaskView(DeleteView):
    model = TaskStoreModel
    template_name = 'delete_confirmation.html'
    success_url = reverse_lazy('taskList')
    



class CompletedTaskView(UpdateView):
    model = TaskStoreModel
    form_class = TaskCompleteModelForm
    template_name = 'confirm_confirmation.html'
    success_url = reverse_lazy('completedTaskList')
    
    
class CompletedTaskListView(ListView):
    model = TaskStoreModel
    template_name = 'complete_tasklist.html'
    context_object_name = 'data'


    
class CompletedTaskUpdateView(UpdateView):
    model = TaskStoreModel
    template_name = 'store_task.html'
    form_class = TaskStoreForm
    success_url = reverse_lazy('completedTaskList')
    

class CompletedDeleteTaskView(DeleteView):
    model = TaskStoreModel
    template_name = 'completed_delete_confirmation.html'
    success_url = reverse_lazy('completedTaskList')



# def MakeCompleteView(UpdateView):
#     model = TaskStoreModel
#     print(model)
#     # template_name = 'store_task.html'
#     # form_class = TaskStoreForm
#     success_url = reverse_lazy('taskList')