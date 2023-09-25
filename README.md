# eazyml
EazyML is a small website (created using Django) which can help you to quickly optimize your machine learning hyperparameters. 
<br>
<br>
All you need is a csv file of your dataset. It is assumed that the dataset is pre-cleaned, and is ready to be fit to a machine learning algorithm. Just upload the data (The dataset is not stored anywhere, as you can freely check on the github repository where this project is publicly available. Inspite of that, you can always upload the data without column names and its all cool!).
<br>
<br>
You can select which ML model you want to use for predictive modelling (4 available currently) and then choose between basic and advanced. 
<br>
<br>
The "Basic" option basically means that the hyperparameters to be optimized, their ranges, and the method of optimization will be decided by the website itself (currently using RandomizedSearchCV). <br>	
The "Advanced" option will allow the user to decide which hyperparameters to optimize, their ranges, and the method of optimization. This option is currently unavailable but will be up very very soon.
<br>
<br>
The main aim of this website is to reduce the time spent in model selection and also to assist in hyperparameter optimization.
<br>
<br>
Watch out for more features coming soon!
		
To run locally:
1. Clone this repo.
2. Run the command "pip install -r requirements.txt"
3. Run the command "python manage.py check" to check if everything is set up correctly.
4. Finally run "python manage.py runserver" and then go to the address 127.0.0.1:8000/home on your browser.
