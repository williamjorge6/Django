from django.contrib import admin
from .models import Task

# Register your models here.4

class TaskAdmin(admin.ModelAdmin):
  readonly_fields = ('created', )
  
admin.site.register(Task, TaskAdmin)