from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView
from .models import Student, Project
from .forms import CreateParticipant, CreateProject, CreateStudentVC
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .utils import gen_recruiting_id

class Dashboard(ListView):
    model = Project
    queryset = Project.objects.all().filter(active=True)
    context_object_name = 'projects'
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
            return redirect('recruitment-success')
                
        else:
            messages.info(request, "Invalid Data")
            return redirect('recruitment-form')
    else:
        recruitment_form = CreateStudentVC() 
    
    context = {
        'form': recruitment_form,
    }
    return render(request, "form.html", context)

class RecruitmentSuccess(TemplateView):
    template_name = "form-success.html"

class StudentVolunteers(ListView):
    model = Student
    queryset = Student.objects.all()
    context_object_name = 'students'
    template_name = 'table.html'

def NewRecruitingId(request, pk):
    gen_recruiting_id(pk)
    return redirect('vcs')
