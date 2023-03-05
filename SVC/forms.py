from django import forms
from .models import Student, Project, Participant

class CreateStudentVC(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'surname','email', 'gender', 'campus', 'faculty', 'access_number', 'cellphone', 'course', 'goal')
        widgets = {
            'name':forms.TextInput(
                attrs={
                    'id':'name',
                    'type':'text',
                    'class':'form-control',
                }
            ),
            'surname':forms.TextInput(
                attrs={
                    'id':'surname',
                    'type':'text',
                    'class':'form-control',
                }
            ),
            'email':forms.EmailInput(
                attrs={
                    'id':'email',
                    'type':'email',
                    'class':'form-control',
                }
            ),
            'gender':forms.Select(
                attrs={
                    'id':'gender',
                    'class':'form-control',
                }
            ),
            'campus':forms.Select(
                attrs={
                    'id':'campus',
                    'class':'form-control',
                }
            ),
            'faculty':forms.Select(
                attrs={
                    'id':'faculty',
                    'class':'form-control',
                }
            ),
            'access_number':forms.TextInput(
                attrs={
                    'id':'access_number',
                    'class':'form-control',
                }
            ),
            'cellphone':forms.TextInput(
                attrs={
                    'id':'cellphone',
                    'type':'text',
                    'class':'form-control',
                }
            ),
            'course':forms.TextInput(
                attrs={
                    'id':'course',
                    'type':'text',
                    'class':'form-control',
                }
            ),
            'goal':forms.Select(
                attrs={
                    'id':'access_number',
                    'class':'form-control',
                    'multiple':'True',
                }
            ),
        }

class CreateProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class CreateParticipant(forms.ModelForm):
    class Meta:
        models = Participant
        fields = '__all__'
