from django.urls import path
from . import views

urlpatterns = [
	path ('login.html', views.loginPageView, name = 'login'),
	path ('admin', views.adminLandingPageView, name = 'admin'),
	path ('nonadmin', views.nonadminLandingPageView, name = 'nonadmin'),
	path ('loginsubmit', views.loginSubmitPageView, name = 'loginsubmit'),
	path ('signupsubmit', views.signupSubmitPageView, name = 'signupsubmit'),
	path ('home.html', views.homePageView, name = 'home'),
	path ('signup.html', views.signupPageView, name = 'signup')
] 
