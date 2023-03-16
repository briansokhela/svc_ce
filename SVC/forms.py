from django import forms
from .models import Student, Project, Participant, Occurrence

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
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'type':'text',
                }
            ),
            'project_type': forms.Select(
                attrs={
                    'class':'form-control',
                }
            ),
            'goal': forms.Select(
                attrs={
                    'class':'form-control',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'row':'5',
                    'placeholder':'Enter text here',
                }
            ),

        }

class CreateOccurence(forms.ModelForm):
    class Meta:
        model = Occurrence
        fields = '__all__'
        widgets = {
            'project':forms.Select(
                attrs={
                    'class':'form-control',
                }
            ),
            'venue':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'type':'text',

                }
            ),
            'vcs_needed':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'type':'number',
                }
            ),
            'expected_duration':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'type':'number',
                }
            )

        }
        
class CreateParticipant(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'
        widgets = {
            'occurrence':forms.Select(
                attrs={
                    'class':'form-control',
                }
            ),
            'vc':forms.Select(
                attrs={
                    'class':'form-control',
                }
            ),
            'staff':forms.Select(
                attrs={
                    'class':'form-control',
                }
            ),
        }
