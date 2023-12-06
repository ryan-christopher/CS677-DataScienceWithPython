'''
Ryan Christopher
Class: CS 677
Date: 12/2/2023
Assignment 6 Question 3

=======Description of Problem=======
Part 1 - Taking the original dataset with all 3 class labels, use k-means clustering with 
random initialization and defaults. Compute and plot distortion vs k, then use
the "knee" method to find the best k. 
Part 2 - Once the best k is found, re-run the clustering with the best k selectors and 
two random features, plot the datapoints, and examine for any interesting patterns. 
Part 3 - For each cluster, assign a cluster label based on the majority class of 
items and print out the centroid and assigned label.
Part 4 - For every point in the dataset, assign a label based on the label on the 
nearest centroid of A, B, or C where A, B, and C are the largest 3 clusters. Then
calculate the overall accuracy of this new classifier when applied to the complete 
data set.
Part 5 - Taking the new classifier from part 4, consider the same two labels used 
for SVM and calculate the accuracy and confusion matrix. 
'''
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.cluster import KMeans


def loadDataset():
    # store column names
    col_names = ["Area", "Perimeter", "Compactness", "Length", "Width", "Asymmetry",
                "GrooveLength", "Class"]
    
    # read CSV data and store into dataframe
    seed_data = pd.read_csv('assignment6/data/seeds_dataset.csv', names = col_names, 
                            header=None, delim_whitespace=True)
    
    return seed_data

seeds = loadDataset()

def findBestK(seeds, max_k):
    # separate data from class
    x = seeds.iloc[:, 0:7]
    sse = []

    # scale values using StandardScaler
    standardScaler = StandardScaler()
    x_scaled = standardScaler.fit_transform(x)

    # iterate through values for k, storing sse on each iteration
    for i in range(1, max_k + 1):
        kmeans = KMeans(n_clusters = i, n_init = 'auto')
        kmeans.fit(x_scaled)
        sse.append(kmeans.inertia_)

    # plot values   
    plt.plot(range(1, max_k + 1), sse, '-b')
    plt.xlabel('k')
    plt.ylabel('Inertia (SSE)')
    plt.title('Knee Plot')
    plt.show()

findBestK(seeds, 8)

