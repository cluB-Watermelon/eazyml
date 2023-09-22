from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from . import forms, functions, models

class Start(View):
	def get(self, request):
		return render(request, 'home/start_page.html')

class Home(LoginRequiredMixin, View):
	def get(self, request):
		form = forms.HomeForm
		ctx = {'form':form}
		return render(request, 'home/home_page.html', ctx)

	def post(self, request):
		form = forms.HomeForm(request.POST, request.FILES)
		wait_url = 'waiting_page/'
		if form.is_valid():
			form = form.cleaned_data
			best_params, train_acc, test_acc, results = functions.handle_files(request.FILES['Upload_csv_file_here'], form['option'], form['model_type'])
			models.MLModelData.objects.create(
					owner = request.user, 
					model_type = form['model_type'], 
					best_params_names = '<->'.join(best_params.keys()),
					best_params_values = '<->'.join([str(x) for x in best_params.values()]), 
					best_train_results = round(train_acc, 4), 
					best_test_results = round(test_acc, 4), 
					used_metric_results = round(results, 4)
				)
			return redirect(wait_url)
		return render(request, 'home/home_page.html', ctx)

class Wait_view(LoginRequiredMixin, View):
	def get(self, request):
		return render(request, 'home/waiting_page.html')

class History(LoginRequiredMixin, View):
	def get(self, request):
		view_template = 'home/history.html'
		data = models.MLModelData.objects.all().values().filter(owner = request.user).order_by('-created_at')
		ctx = {'data' : data}
		return render(request, view_template, ctx)

class Results(LoginRequiredMixin, View):
	def get(self, request):
		results_template = 'home/result_page.html'
		data = models.MLModelData.objects.filter(owner = request.user).latest('created_at')
		ctx = {'data' : data}
		return render(request, results_template, ctx)

	def post(self, request):
		data = request.POST.get('fname')
		saved_url = 'results_saved_page/'
		return redirect(saved_url)

class Results_saved(LoginRequiredMixin, View):
	def get(self, request):
		results_template = 'home/result_saved_page.html'
		data = models.MLModelData.objects.filter(owner = request.user).latest('created_at')
		ctx = {'data' : data}
		return render(request, results_template, ctx)

class CreateUser(View):
	def get(self, request):
		form = forms.UserForm
		ctx = {'form': form}
		return render(request, 'registration/register.html', ctx)

	def post(self, request):
		form = forms.UserForm(request.POST)
		success_url = reverse('login')
		if form.is_valid():
			form.save()
			messages.success(request, 'Account Created Successfully')
			return redirect(success_url)
		else:
			form = forms.UserForm
			ctx = {'form': form}

		return render(request, 'registration/register.html', ctx)

class Contact(View):
	def get(self, request):
		return render(request, 'home/contact_page.html')