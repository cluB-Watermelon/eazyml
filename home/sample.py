import pandas as pd
import ml


if __name__ == '__main__':

	df = pd.read_csv('good.csv')
	obj = ml.RandomForestClassificationModel()
	a, b = obj.run_basic(df)
	print(a)
	b = pd.DataFrame(b)
	b.sort_values(by = 'mean_test_score', ascending = False, inplace = True)
	print(b.loc[:, 'mean_test_score'])