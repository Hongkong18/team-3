from django.urls import path
from . import views

urlpatterns = [
	path ('login', views.loginPageView, name = 'login'),
	path ('admin', views.adminLandingPageView, name = 'admin'),
	path ('nonadmin', views.nonadminLandingPageView, name = 'nonadmin'),
	path ('loginsubmit', views.loginSubmitPageView, name = 'loginsubmit')
] 
