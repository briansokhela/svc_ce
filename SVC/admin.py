from django.contrib import admin
from .models import Student, Project, Staff, Occurrence, Participant

class StudentAdmin(admin.ModelAdmin):
  list_display = ('name', 'surname', 'access_number', 'hours_completed')

class ProjectsAdmin(admin.ModelAdmin):
  list_display =('name', 'goal', 'project_type')

admin.site.register(Student, StudentAdmin)
admin.site.register(Project, ProjectsAdmin)
admin.site.register(Staff, StudentAdmin)
admin.site.register(Occurrence)
admin.site.register(Participant)