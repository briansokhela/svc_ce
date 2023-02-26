from django import forms
from .models import Student, Project, Participant

class CreateStudentVC(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'surname','email', 'gender', 'campus', 'faculty', 'access_number', 'cellphone')

class CreateProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class CreateParticipant(forms.ModelForm):
    class Meta:
        models = Participant
        fields = '__all__'
