import pandas as pd
import numpy as np
import pymatgen as mg
import matplotlib.pyplot as plt
import os 
os.chdir(r'C:\Users\Ziyan\Downloads\xgboost\python-package') # CHANGE WORKING DIRECTORY

class Vectorize_Formula:

	def __init__(self):
		elem_dict = pd.read_excel(r'elementsnew.xlsx') # CHECK NAME OF FILE 
		self.element_df = pd.DataFrame(elem_dict)
		self.element_df.set_index('Symbol',inplace=True)
		self.column_names = []
		for string in ['avg','diff','max','min']:
			for column_name in self.element_df.columns.values:
				self.column_names.append(string+'_'+column_name)

	def get_features(self, formula):
		'''
		Parameters
		----------
		formula: string
			put a valid chemical fomula as a string. Example( 'NaCl')

		Return
		----------
		features: np.array()
			This is an 1xN length array containing feature values for use in the
			machine learning model.
		'''
		try:
			fractional_composition = mg.Composition(formula).fractional_composition.as_dict()
			element_composition = mg.Composition(formula).element_composition.as_dict()
			avg_feature = np.zeros(len(self.element_df.iloc[0]))
			sum_feature = np.zeros(len(self.element_df.iloc[0]))
			for key in fractional_composition:
				try:
					avg_feature += self.element_df.loc[key].values * fractional_composition[key]
					diff_feature = self.element_df.loc[list(fractional_composition.keys())].max()-self.element_df.loc[list(fractional_composition.keys())].min()
				except:
					print('The element:', key, 'from formula', formula,'is not currently supported in our database')
					return np.array([np.nan]*len(self.element_df.iloc[0])*4)
			max_feature = self.element_df.loc[list(fractional_composition.keys())].max()
			min_feature = self.element_df.loc[list(fractional_composition.keys())].min()

			features = pd.DataFrame(np.concatenate([avg_feature, diff_feature, np.array(max_feature), np.array(min_feature)]))
			features = np.concatenate([avg_feature, diff_feature, np.array(max_feature), np.array(min_feature)])
			return features.transpose()
		except:
			print('There was an error with the Formula: '+ formula + ', this is a general exception with an unkown error')
			return [np.nan]*len(self.element_df.iloc[0])*4
	
def rf_feature_importance(rf, X_train, N='all', std_deviation=False):
	'''Get feature importances for trained random forest object
	
    Parameters
    ----------
	rf : sklearn RandomForest object
		This needs to be a sklearn.ensemble.RandomForestRegressor of RandomForestClassifier object that has been fit to data
	N : integer, optional (default=10)
		The N most important features are displayed with their relative importance scores
	std_deviation : Boolean, optional (default=False)
		Whether or not error bars are plotted with the feature importance. (error can be very large if maximum_features!='all' while training random forest
    Output
    --------
	graphic :
		return plot showing relative feature importance and confidence intervals

    Examples
    --------
    >>> from sklearn.ensemble import RandomForestRegressor
    >>> rf = RandomForestRegressor(max_depth=20, random_state=0)
    >>> rf.fit(X_train, y_train)
    >>> rf_feature_importance(rf, N=15)
	'''

	if N=='all':
		N=X_train.shape[1]
	importance_dic = {}
	importances = rf.feature_importances_
	std = np.std([tree.feature_importances_ for tree in rf.estimators_],
				 axis=0)
	indices = np.argsort(importances)[::-1]
	indices = indices[0:N]
	
	# Print the feature ranking
	print("Feature ranking:")
	
	for f in range(0, N):
		importance_dic[X_train.columns.values[indices[f]]]=importances[indices[f]]
		print(("%d. feature %d (%.3f)" % (f + 1, indices[f], importances[indices[f]])),':', X_train.columns.values[indices[f]])
	
	
	# Plot the feature importances of the forest
	plt.figure()
	plt.title("Feature importances")
	if std_deviation == True:
		plt.bar(range(0, N), importances[indices], color="r", yerr=std[indices], align="center")
	else:
		plt.bar(range(0, N), importances[indices], color="r", align="center")
	plt.xticks(range(0, N), indices, rotation=90)
	plt.xlim([-1, N])
	plt.show()

