from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView
from .models import Student, Project, Volunteer, Staff, Participant
from .forms import CreateParticipant, CreateProject, CreateStudentVC
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .utils import gen_recruiting_id,get_hours

class Dashboard(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'admin/index.html'

    def get_context_data(self, **kwargs):
        all_vcs = Student.objects.all()
        champions = Participant.objects.all()
        kwargs['active_vc'] = all_vcs.filter(active=True).count()
        kwargs['active_projects'] = 0
        kwargs['vc_hours'] = sum([vc.hours_completed for vc in all_vcs])
        kwargs['total_vc'] = all_vcs.count()
        kwargs['CBE'] = get_hours('College of Business and Economics',champions)
        kwargs['FADA'] = get_hours('Faculty of Arts, Design and Architecture',champions)
        kwargs['FEBE'] = get_hours('Faculty of Engineering and The Built Enviroment',champions)
        kwargs['FED'] = get_hours('Faculty of Education',champions)
        kwargs['FHS'] = get_hours('Faculty of Health Sciences',champions)
        kwargs['FSC'] = get_hours('Faculty of Science',champions)
        kwargs['LAW'] = get_hours('Faculty of Law',champions)
        kwargs['HMT'] = get_hours('Faculty of Humanities',champions)
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

class Programs(ListView):
    model = Project
    queryset = Project.objects.all()
    context_object_name = 'projects'
    template_name = 'admin/programs.html'

class ProgramsDetails(DetailView):
    model = Project
    context_object_name = 'program'
    template_name = 'admin/program-details.html'

    def get_context_data(self, **kwargs):
        kwargs['project_occurrences'] = self.get_object().occurrence_set.all()
        return super().get_context_data(**kwargs)

class AddNewProgram(CreateView):
    model = Project
    form_class = CreateProject
    success_url = '/volunteering-programs/'
    template_name = 'admin/add-program.html'



