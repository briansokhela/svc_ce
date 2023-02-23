from django.contrib import admin
from .models import Volunteer, Faculty, SD_goal, Projects 

class VolunteerAdmin(admin.ModelAdmin):
  list_display = ('name', 'surname', 'login_number', 'hours_completed')

class FacultyAdmin(admin.ModelAdmin):
  list_display = ('name', 'hours_completed')

class SD_goalAdmin(admin.ModelAdmin):
  list_display = ('name', 'hours_completed')

class ProjectsAdmin(admin.ModelAdmin):
  list_display =('name', 'goal', 'date', 'project_type', 'venue', 'expected_duration')

admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(SD_goal, SD_goalAdmin)
admin.site.register(Projects, ProjectsAdmin)