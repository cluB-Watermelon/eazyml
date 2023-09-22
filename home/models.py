from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class MLModelData(models.Model):
	choices = ['Linear Classification', 'Linear Regression', 'Decision Tree Classifier', 'Decision Tree Regressor', 'Random Forest Classifier', 'Random Forest Regressor']
	
	# Variable Creation
	LC = 'Linear Classification'
	LR = 'Linear Regression'
	RFC = 'Random Forest Classifier'
	RFR = 'Random Forest Regressor'

	model_choices = (
			(LC, 'Linear Classification'), 
			(LR, 'Linear Regression'), 
			(RFC, 'Random Forest Classifier'), 
			(RFR, 'Random Forest Regressor')
		)

	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null = True)
	model_type = models.CharField(max_length = 32, choices = model_choices)
	best_params_names = models.CharField(max_length = 256, null = True)
	best_params_values = models.CharField(max_length = 256, null = True)
	best_train_results = models.FloatField(null = True)
	best_test_results = models.FloatField(null = True)
	used_metric_results = models.FloatField(null = True)
	created_at = models.DateTimeField(auto_now_add=True, null = True)


