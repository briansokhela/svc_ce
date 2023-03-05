from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name="home"),
    path('student-vcs/', views.StudentVolunteers.as_view(), name='vcs'),
    path('student-vcs/new-rc-id/<int:pk>/', views.NewRecruitingId, name='new-rc-id'),
    path('recruitment/', views.recruiment, name='recruitment-form'),
    path('recruitment/success/', views.RecruitmentSuccess.as_view(), name='recruitment-success'),

]
