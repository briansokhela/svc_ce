from django.db import models

class Volunteer(models.Model):
  choices_cmp = (
    ('APK', 'Kingsway'),
    ('APB', 'Bunting'),
    ('SWC', 'Soweto'),
    ('DFC', 'Doornfontein'),
  )
  choices_gnd = (
    ('M', 'Male'),
    ('F', 'Female'),
  )
  name = models.CharField(max_length=50)
  surname = models.CharField(max_length=50)
  email = models.EmailField()
  gender = models.CharField(max_length=7, choices=choices_gnd, null=True)
  campus = models.CharField(max_length=3,choices=choices_cmp)
  date_joined = models.DateField(auto_now_add=True)
  login_number = models.IntegerField()
  hours_completed = models.IntegerField(null=True)

  class meta:
    abstract = True
  
  def __str__(self):
    return self.login_number

class Faculty(models.Model):
  name = models.CharField(max_length=100)
  hours_completed = models.IntegerField(null=True)
  def __str__(self):
    return self.name


class Staff(Volunteer):
  occupation = models.CharField(max_length=50,null=True)
  
class Student(Volunteer):
  #every student has a number of recruits and optionally, a recruiter(relationship where many
  # students can be recruited by one recruiter/student)
  num_recruits = models.IntegerField()
  recruiter = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
  faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)

class SD_goal(models.Model):
  name = models.CharField(max_length=100)
  hours_completed = models.IntegerField(null=True)

  def __str__(self):
    return self.name

class Projects(models.Model):
  choices_type = (
    ('SL', 'Service Learning'),
    ('CBR', 'Community-Based Research'),
    ('OO', 'Organised Outreach'),
  )
  goal= models.ForeignKey(SD_goal, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=3000, null=True)
  date = models.DateTimeField()
  expected_duration = models.IntegerField()
  VCs_needed = models.IntegerField()
  project_type = models.CharField(max_length=80, choices=choices_type)
  venue = models.CharField(max_length=120)
  completion_code = models.CharField(max_length=60, null=True)

  def __str__(self):
    return self.name






