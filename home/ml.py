import pandas as pd
import numpy as np
from scipy import stats
import pickle

# model_selection
from sklearn.model_selection import train_test_split, RandomizedSearchCV

# actual_models
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

#metrics
from sklearn.metrics import accuracy_score as acc, r2_score


class CommonFunctions():

	def split(self, df):
		X = df.iloc[:, :-1].values
		y = df.iloc[:, -1].values

		return(train_test_split(X, y, test_size = 0.2))

	# Defining the hyperparameter space for Logistic Regression Basic option
	def basic_log_reg_get_param_grid(self):

		param_grid = dict(
			C = stats.uniform(0.1, 100), 
			penalty = ('l1', 'l2')
		)

		return param_grid
	
	# Defining the hyperparameter space for Random Forest Basic option
	# We will use the same hyperparameter space for both the Regressor and the Classifier
	def basic_rf_get_param_grid(self):

		param_grid = dict(
			n_estimators = stats.randint(10, 100), 
    		min_samples_split = stats.uniform(0, 1), 
    		max_depth = stats.randint(1, 6), 
		)

		return param_grid	

	def cross_val(self, ml_model, param_grid, scoring, X_train, y_train):

		search = RandomizedSearchCV(
				ml_model, 
				param_grid, 
				scoring = scoring, 
				cv = 5, 
				n_iter = 60, 
				n_jobs = 4, 
				refit = True
			)

		search.fit(X_train, y_train)

		results = pd.DataFrame(search.cv_results_)
		results.sort_values(by = 'mean_test_score', ascending = False, inplace = True)
		used_metric_results = results['mean_test_score'].iloc[0] 

		return (search.best_params_, used_metric_results, search.best_estimator_)

class LinearRegressionModel(CommonFunctions):

	def run_basic(self, csv):
		X_train, X_test, y_train, y_test = super().split(csv)

		regressor = LinearRegression()
		regressor.fit(X_train, y_train)

		y_pred = regressor.predict(X_test)
		accuracy = r2_score(y_test, y_pred)
		train_acc = r2_score(y_train, regressor.predict(X_train))
		test_acc = accuracy

		return(1, train_acc, test_acc, accuracy)

class LogisticRegressionModel(CommonFunctions):

	def run_basic(self, csv):
		X_train, X_test, y_train, y_test = super().split(csv)

		classifier = LogisticRegression(solver = 'liblinear')
		param_grid = super().basic_log_reg_get_param_grid()

		best_params, results, best_model = super().cross_val(classifier, param_grid, 'accuracy', X_train, y_train)

		train_acc = acc(y_train, best_model.predict(X_train))
		test_acc = acc(y_test, best_model.predict(X_test))

		return(best_params, train_acc, test_acc, results)

class RandomForestRegressionModel(CommonFunctions):

	def run_basic(self, csv):
		X_train, X_test, y_train, y_test = super().split(csv)

		classifier = RandomForestRegressor()
		param_grid = basic_rf_get_param_grid()

		best_params, results, best_model = super().cross_val(classifier, param_grid, 'r2', X_train, y_train)

		train_acc = r2_score(y_train, best_model.predict(X_train))
		test_acc = r2_score(y_test, best_model.predict(X_test))

		return(best_params, train_acc, test_acc, results)

class RandomForestClassificationModel(CommonFunctions):

	def run_basic(self, csv):
		X_train, X_test, y_train, y_test = super().split(csv)

		classifier = RandomForestClassifier()
		param_grid = super().basic_rf_get_param_grid()

		best_params, results, best_model = super().cross_val(classifier, param_grid, 'accuracy', X_train, y_train)

		train_acc = acc(y_train, best_model.predict(X_train))
		test_acc = acc(y_test, best_model.predict(X_test))

		return(best_params, train_acc, test_acc, results)
