from django.contrib import admin
from .models import Project, Task, Comment, Label
# Register your models here.
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(Label)