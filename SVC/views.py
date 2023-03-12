from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView
from .models import Student, Project, Volunteer, Staff
from .forms import CreateParticipant, CreateProject, CreateStudentVC
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .utils import gen_recruiting_id

class Dashboard(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'admin/index.html'

    def get_context_data(self, **kwargs):
        all_vcs = Student.objects.all()
        kwargs['active_vc'] = all_vcs.filter(active=True).count()
        kwargs['active_projects'] = 0
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

class Volunteers(TemplateView):
    template_name = 'admin/volunteers.html'

    def get_context_data(self, **kwargs):
        kwargs['volunteers'] = []
        all_stu = Student.objects.all()
        all_sta = Staff.objects.all()
        for stu_vc in all_stu:
            kwargs['volunteers'].append(stu_vc)
        
        for sta_vc in all_sta:
            kwargs['volunteers'].append(sta_vc)
        print(kwargs['volunteers'])
        return super().get_context_data(**kwargs)

class svcDetials(DetailView):
    model = Student
    context_object_name = 'student'
    template_name = 'admin/vc-details.html'

    def get_context_data(self, **kwargs):
        kwargs['programs'] = self.get_object().participant_set.all()
        return super().get_context_data(**kwargs)


