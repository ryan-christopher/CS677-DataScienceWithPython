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