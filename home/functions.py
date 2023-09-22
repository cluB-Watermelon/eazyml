import pandas as pd
import sklearn_json as skljson
from . import ml

def handle_files(file, option, model_type):

	if file.name.endswith('.csv'):
		df = pd.read_csv(file)
		return(run_model(df, option, model_type))
	else:
		return ('Please only upload csv files.')

def run_model(df, option, model_type):

	if model_type == 'Linear Regression':
		results_obj = ml.LinearRegressionModel()
	elif model_type == 'Linear Classification':
		results_obj = ml.LogisticRegressionModel()
	elif model_type == 'Random Forest Classifier':
		results_obj = ml.RandomForestClassificationModel()
	elif model_type == 'Random Forest Regressor':
		results_obj = ml.RandomForestRegressionModel()

	return(results_obj.run_basic(df))






