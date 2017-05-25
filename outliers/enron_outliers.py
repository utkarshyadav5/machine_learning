#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )

max_salary=0
max_salary_key=0

for key in data_dict:
    if data_dict[key]["salary"] != 'NaN' and data_dict[key]["salary"] > max_salary:
        max_salary=data_dict[key]["salary"]
        max_salary_key=key

data_dict.pop(max_salary_key,0)

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary=point[0]
    bonus=point[1]
    matplotlib.pyplot.scatter(salary,bonus)

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

