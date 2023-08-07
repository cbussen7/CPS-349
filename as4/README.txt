For this assignment, I used the following libraries (will just show them as import statements):
	- import sklearn as sk
	- from sklearn.model_selection import train_test_split
	- from sklearn.tree import DecisionTreeClassifier
	- from sklearn.tree import plot_tree
	- from sklearn.tree import export_graphviz
	- import graphviz
	- from sklearn.neighbors import KNeighborsClassifier
	- from sklearn.ensemble import RandomForestClassifier
	- from sklearn import metrics
	- from sklearn.metrics import confusion_matrix
	- import matplotlib.pyplot as plt
	- import pandas as pd
	- from google.colab import files

In order for this code to work, make sure you have these libraries installed on your machine. However, if you are running this file in Google Colab (as I did), you will not need to install any libraries as it already has them all loaded. Instead, Google Colab will simply need to import them as shown at the top of the code. For ease and access to different options, I will include both the py and ipynb files for my project in the zipped file. In terms of actually running the code, you can either import the ipynb file to Google Colab and run it there, you can run the py file in an IDE such as PyCharm, or you can run it in the terminal using "python3" followed by the name of the py file. If you are going to run in Google Colab, make sure that you upload the necessary datasets first so that it can successfully read the files.