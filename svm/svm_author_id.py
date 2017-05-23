#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]


#########################################################
### your code goes here ###
from sklearn import svm
clf=svm.SVC(C=10000.0, kernel='linear', gamma='auto')
# using kernel=rbf && C=10000 => accuracy=0.990
# using kernel=linear && C=1.0 => accuracy= 0.98
# using kernel=linear && C=10000 => accuracy= 0.994

t0=time()
clf.fit(features_train,labels_train)
print "training time :", round(time()-t0,3), "s"

t0=time()
pred=clf.predict(features_test)
print "prediciting time :", round(time()-t0,3), "s"
print(pred)

# for counting the number of chris=1
count=0
for i in pred:
    if i==1:
        count+=1

print count
#####################

from sklearn.metrics import accuracy_score
print(accuracy_score(pred,labels_test))
#########################################################


