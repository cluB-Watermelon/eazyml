from django import forms 
from django.contrib.auth.forms import UserCreationForm
from home.models import MLModelData
from django.contrib.auth.models import User

class HomeForm(forms.ModelForm, forms.Form):
	class Meta:
		model = MLModelData
		fields = ['model_type']

	CHOICES = [
		('1', 'Basic (Choose this if you want US to handle the basic hyperparameter optimization, and thus just a quick accuracy check)'), 
		('2', 'Advanced (Choose this if you want to provide the hyperparameters and their range yourself. Doesnt work yet, so just use basic. It currently works the same as basic)')
	]
	option = forms.ChoiceField(
			widget = forms.RadioSelect, 
			choices = CHOICES, 
		)

	Upload_csv_file_here = forms.FileField()

class DisplayForm(forms.ModelForm):
	class Meta:
		model = MLModelData
		fields = '__all__'
		
class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name']
			