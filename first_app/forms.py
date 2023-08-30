from django import forms
from first_app.models import TaskStoreModel



class TaskStoreForm(forms.ModelForm):
    class Meta:
        model = TaskStoreModel
        fields = ['task_title','task_description']
        widgets = {
            'task_description': forms.Textarea(attrs={'cols': 30, 'rows': 5})
        }
        labels = {
            'task_title':'Title: ',
            'task_description':'Descriptions: '
        }
        
class TaskCompleteModelForm(forms.ModelForm):
    class Meta:
        model = TaskStoreModel
        fields = ['is_completed']
        labels = {'is_completed':'Please Check Completed'}