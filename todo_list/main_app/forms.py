from django import forms
from .models import Task, Comment


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'project', 'assigned_to', 'due_date', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)

        for field in self.fields:
       с
            self.fields[field].widget.attrs["class"] = f"{existing_classes} form-control".strip()

        existing_status_classes = self.fields["status"].widget.attrs.get("class", "")
        self.fields["status"].widget.attrs["class"] = f"{existing_status_classes} myselector".strip()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class TaskFilterForm(forms.Form):
    STATUS_CHOICES = [
        ("", "Всі"),
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        required=False,
        label="Статус"
    )
