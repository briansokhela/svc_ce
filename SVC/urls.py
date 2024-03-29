from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name="home"),
    path('recruitment/', views.recruiment, name='recruitment-form'),
    path('recruitment/success/', views.RecruitmentSuccess.as_view(), name='recruitment-success'),

    path('volunteer-champions/', views.Volunteers.as_view(), name='vc'),
    path('volunteer-champions/student-vc/<int:pk>/details', views.svcDetials.as_view(), name='svc-details'),

    path('volunteering-programs/', views.Programs.as_view(), name='programs'),
    path('volunteering-programs/<int:pk>/details', views.ProgramsDetails.as_view(), name='program-details'),
    path('volunteering-programs/add-new/', views.AddNewProgram.as_view(), name='add-program'),
    path('volunteering-programs/new-occurrence/', views.AddProgramOccurrence.as_view(), name='add-occurrence'),
    path('volunteering-programs/occurrences/add-participant/', views.AddParticipants.as_view(), name='add-participant'),


]
