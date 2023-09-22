from django.urls import path, include
from . import views

app_name = 'home'
urlpatterns = [
	path('', views.Start.as_view(), name = 'start'),
	path('home_page/', views.Home.as_view(), name = 'home'),
	path('waiting_page/', views.Wait_view.as_view(), name = 'wait'), 
	path('history/', views.History.as_view(), name = 'history'), 
	path('results_page/', views.Results.as_view(), name = 'results'),
	path('register_page/', views.CreateUser.as_view(), name = 'register'),
	path('contact/', views.Contact.as_view(), name = 'contact')
	# path('results_page/results_saved_page/', views.Results_saved.as_view(), name = 'results_saved')
]