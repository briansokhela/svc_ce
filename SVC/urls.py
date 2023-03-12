from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name="home"),
    path('recruitment/', views.recruiment, name='recruitment-form'),
    path('recruitment/success/', views.RecruitmentSuccess.as_view(), name='recruitment-success'),

    path('volunteer-champions/', views.Volunteers.as_view(), name='vc'),
    path('volunteer-champions/student-vc/<int:pk>/details', views.svcDetials.as_view(), name='svc-details'),

]
