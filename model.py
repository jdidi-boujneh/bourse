# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

dataset = pd.read_csv('bourse.csv')


X = dataset

#Converting words to integer values


#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.


from sklearn.cluster import KMeans 
from sklearn.metrics.cluster import adjusted_rand_score

#Fitting model with trainig data
kmeans = KMeans(n_clusters=4, precompute_distances='auto')
kmeans.fit(dataF)

# Saving model to disk
pickle.dump(regressor, open('kmeans.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('kmeans.pkl','rb'))
#print(model.predict([[2, 9, 6 , 2, 9, 6 , 2, 9, 6]]))
