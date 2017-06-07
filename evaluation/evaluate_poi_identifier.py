#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here
from sklearn.model_selection import train_test_split

features_train,features_test,labels_train,labels_test=train_test_split(
    features,labels,test_size=0.3,random_state=42)

from sklearn.tree import DecisionTreeClassifier

clf=DecisionTreeClassifier()
clf.fit(features_train,labels_train)
print "Accuracy Score ", clf.score(features_test,labels_test)

pred= clf.predict(features_test)

num_pois=0

for preds in pred:
    if preds==1:
        num_pois+=1

true_positives = 0
false_positives = 0
false_negatives = 0

for preds, actual in zip(pred, labels_test):
    if preds == actual and actual == 1:
        true_positives += 1
    elif preds == 1 and actual == 0:
        false_positives += 1
    elif preds == 0 and actual == 1:
        false_negatives += 1

print "True Positives:", true_positives
print "False Positives", false_positives
print "False Negatives", false_negatives

print "\nPrecision (POIs):", true_positives/(true_positives + false_positives)
print "Recall (POIs)", true_positives/(true_positives + false_negatives)



















