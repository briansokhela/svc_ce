from django.db import models

class Volunteer(models.Model):
  choices_cmp = (
    ('APK', 'APK'),
    ('APB', 'APB'),
    ('SWC', 'SWC'),
    ('DFC', 'DFC'),
  )
  choices_gnd = (
    ('M', 'Male'),
    ('F', 'Female'),
  )
  name = models.CharField(max_length=50)
  surname = models.CharField(max_length=50)
  email = models.EmailField()
  access_number = models.CharField(max_length=9)
  cellphone = models.CharField(max_length=10)
  gender = models.CharField(max_length=7, choices=choices_gnd, null=True)
  campus = models.CharField(max_length=3,choices=choices_cmp, default='APK')
  date_joined = models.DateField(auto_now_add=True, blank=True)
  hours_completed = models.IntegerField(null=True ,default=0)
  active = models.BooleanField(default=False, blank=True)
  
  class meta:
    abstract = True
  
  def __str__(self):
    return self.access_number

class Staff(Volunteer):
  occupation = models.CharField(max_length=50,null=True)
  
class Student(Volunteer):
  FALCULTIES = (
    ('Faculty of Science', 'Faculty of Science'),
    ('Faculty of Education', 'Faculty of Eduction'),
    ('Faculty of Humanities', 'Faculty of Humanities'),
    ('Faculty of Law', 'Faculty of Law'),
    ('Faculty of Health Sciences', 'Faculty of Health Sciences'),
    ('Faculty of Arts, Design and Architecture', 'Faculty of Arts, Design and Architecture'),
    ('College of Business and Economics','College of Business and Economics'),
    ('Faculty of Engineering and The Built Enviroment','Faculty of Engineering and The Built Enviroment'),
    
  )
  #every student has a number of recruits and optionally, a recruiter(relationship where many
  # students can be recruited by one recruiter/student)
  recruiter = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
  faculty = models.CharField(max_length=100, choices=FALCULTIES, blank=True)
  recruiting_id = models.CharField(max_length=64, null=True, blank=True)


 
class Project(models.Model):
  SD_GOALS = (
    ('NO POVERTY', 'NO POVERTY'),
    ('ZERO HUNGER', 'ZERO HUNGER'),
    ('GOOD HEALTH & WELL-BEING', 'GOOD HEALTH & WELL-BEING'),
    ('QUALITY EDUCATION', 'QUALITY EDUCATION'),
    ('GENDER EQUALITY', 'GENDER EQUALITY'),
    ('CLEAN WATER & SANITATION', 'CLEAN WATER & SANITATION'),
    ('AFFORDABLE & CLEAN ENERGY', 'AFFORDABLE & CLEAN ENERGY'),
    ('DECENT WORK & ECONOMIC GROWTH', 'DECENT WORK & ECONOMIC GROWTH'),
    ('INDUSTRY, INNOVATION & INFRASTRUCTURE', 'INDUSTRY, INNOVATION & INFRASTRUCTURE'),
    ('REDUCE INEQUALITIES', 'REDUCE INEQUALITIES'),
    ('SUSTAINABLE CITIES & COMMUNITIES', 'SUSTAINABLE CITIES & COMMUNITIES'),
    ('RESPONSIBLE CONSUMPTION', 'RESPONSIBLE CONSUMPTION'),
    ('CLIMATE ACTION', 'CLIMATE ACTION'),
    ('LIFE BELOW WATER', 'LIFE BELOW WATER'),
    ('LIFE ON LAND', 'LIFE ON LAND'),
    ('PEACE, JUSTICE & STRONG INSTITUTIONS', 'PEACE, JUSTICE & STRONG INSTITUTIONS'),
    ('PARTNERSHIPS FOR THE GOALS', 'PARTNERSHIPS FOR THE GOALS'),
  )
  choices_type = (
    ('Service Learning', 'Service Learning'),
    ('Community-Based Research', 'Community-Based Research'),
    ('Organised Outreach', 'Organised Outreach'),
  )
  goal= models.CharField(max_length=50, choices=SD_GOALS)
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=3000, null=True)
  date = models.DateTimeField()
  expected_duration = models.IntegerField()
  vcs_needed = models.IntegerField()
  project_type = models.CharField(max_length=80, choices=choices_type)
  venue = models.CharField(max_length=120)
  completion_code = models.CharField(max_length=60, null=True)
  active = models.BooleanField(default=False)

class Participant(models.Model):
  project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
  vc = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
  staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True)
  date = models.DateTimeField()







