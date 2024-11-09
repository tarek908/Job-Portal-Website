from django.urls import path, include
from .import views 

urlpatterns = [
   path('', views.index,  name='index'),
   path('signuppage/', views.signupPage, name='signuppage'),
   path('register/', views.register, name='register'),
   path('login/', views.loginPage, name='login'),
   path('otpVerify/', views.otpVerify, name='otpVerify'),
   path('loginuser/', views.LoginUser, name='loginuser'),
   path('profile/<int:pk>/', views.profile, name='profile'),
   path('profileImage/<int:pk>/', views.profielImage,name='profielImage'),
   path('proupdate/<int:pk>/',views.profileUpdate,name='proupdate'), 
   path('canjoblist/', views.can_job_table, name='canjoblist'),
   path('candidatelogout/',views.Candidatelogout, name='candidatelogout'),
   path('applypage/<int:pk>/',views.applyPage, name='applypage'),
   path('applyjob/<int:pk>/',views.ApplyJob, name='applyjob'),

   #### ---- Company ----########
   path('deshbord/',views.CompanyDeshbord,name='deshbord'),
   path('company/<int:pk>', views.comProfile, name='company'),
   path('comupdate/<int:pk>/',views.comUpdate,name='comupdate'),
   path('jobpostpage/<int:pk>/',views.jobPostPage, name='jobpostpage'),
   path('jobposted/', views.jobDetails, name='jobposted'),
   path('jobtable/', views.job_table, name='jobtable'),
   path('companyLogout/',views.companylogout, name='companylogout'), 
   path('applyList/',views.JobApplyList, name='applylist'),

   #### ---- Admin ----########
   path('adminloginpage/', views.AdminLoginPage, name='adminloginpage'),
   path('adminindex/', views.adminIndexPage, name='adminindex'),
   path('adminlogin/',views.adminLogin, name='adminlogin'),
   path('UserList/' , views.UserList, name='userList'),
   path('deleteuser/<int:pk>/', views.UserDelete, name='deleteusre'),
   path('companyList/' , views.CompanyList, name='companyList'),
   path('VerifidPage/<int:pk>/', views.VerifiedCompany, name='VerifidPage'),
   path('verified/<int:pk>/',views.Verified, name='verifiedcom'),
   path('comdelete/<int:pk>/',views.CompanyDelete, name='deletecom'),


   ########### About sectiion ###########
   path('aboutpage/' , views.AboutPage, name='aboutpage'),
]
