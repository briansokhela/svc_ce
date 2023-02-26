from django.views.generic import TemplateView, CreateView
from .models import Student, Project
from .forms import CreateParticipant, CreateProject, CreateStudentVC
from django.http import HttpResponse
from django.shortcuts import render

class Dashboard(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        all_vcs = Student.objects.all()
        kwargs['active_vc'] = all_vcs.filter(active=True).count()
        kwargs['active_projects'] = Project.objects.all().filter(active=True).count()
        kwargs['vc_hours'] = sum([vc.hours_completed for vc in all_vcs])
        kwargs['total_vc'] = all_vcs.count()
        return super().get_context_data(**kwargs)   

def recruiment(request, code=None):
    if request.method == 'POST':
        recruitment_form = CreateStudentVC(request.POST)
        if recruitment_form.is_valid():
            access_number = recruitment_form.cleaned_data['access_number']
            recruitment_form.save()
            if code is not None:
                try:
                    recruiter = Student.objects.get(recruiting_id=code)
                    new_vc = Student.objects.get(access_number=access_number)

                    new_vc.recruiter = recruiter
                    new_vc.save()
                except:
                    pass
    else:
        recruitment_form = CreateStudentVC() 
    
    context = {
        'form': recruitment_form,
    }
    return HttpResponse