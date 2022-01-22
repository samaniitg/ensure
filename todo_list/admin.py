from django.contrib import admin
from  .models import Task
 

@admin.register(Task)
class TaskAdminModel(admin.ModelAdmin):
    list_display = ["name","details"]