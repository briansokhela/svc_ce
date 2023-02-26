from django.contrib import admin
from .models import Student, Project 

class StudentAdmin(admin.ModelAdmin):
  list_display = ('name', 'surname', 'access_number', 'hours_completed')

class ProjectsAdmin(admin.ModelAdmin):
  list_display =('name', 'goal', 'date', 'project_type', 'venue', 'expected_duration')

admin.site.register(Student, StudentAdmin)
admin.site.register(Project, ProjectsAdmin)