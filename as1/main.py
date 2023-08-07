"""
Data Science 349
Data Science and Pattern Recognition 592
Assignment 1 Code

Please run the following code in 3 different development
environments, as instructed in the homework write up.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import neighbors

#setting the random seed
np.random.seed = 42

#generating mock data
NUM_CITIES = 100
lat = np.random.uniform(-100, 100, NUM_CITIES)
lon = np.random.uniform(-100, 100, NUM_CITIES)
has_airport = np.random.choice(["yes", "no"], NUM_CITIES)
climate = np.random.choice(["tropical", "mild", "dry", "continental", "polar"], NUM_CITIES)
temp = np.random.normal(75, 45, NUM_CITIES)

#creating a data frame
data = {
    "Latitude" : lat,
    "Longitude" : lon,
    "Has Airport" : has_airport,
    "Climate" : climate
}
df = pd.DataFrame(data)
print(df.sample(5))

#finding unique values in a column
print(pd.unique(df["Longitude"]))

#showing number of unique elements in each column
print("No.of.unique values in each column :\n", df.nunique(axis=0))

#adding a new column
df["Average Temperature"] = temp
print(df.sample(5))

#plot lon and lat
df.plot.scatter(x="Latitude", y="Longitude")
plt.savefig("lat_long.png")

#classifier to predict climate from lon and lat
n_neighbors = 15
X = df[["Latitude", "Longitude"]]
y = df["Climate" ]

# k-nearest neighbors
clf = neighbors.KNeighborsClassifier(n_neighbors, weights="uniform")
clf.fit(X, y)

#predict the climate on unlabeled data
print(clf.predict([[-100, 100]]))