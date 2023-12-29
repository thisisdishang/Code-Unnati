# Code to differentiate between Apples & Oranges
from sklearn import tree
# change strings to integers 0:bumpy 1:smooth
features=[[140,1],[130,1],[150,0],[170,0]]
# 0:apple 1:orange
labels=[0,0,1,1]
clf=tree.DecisionTreeClassifier() 
# classifier gets trained on input data
clf=clf.fit(features,labels)  # type: ignore
print(clf.predict([[150,0]]))
print(clf.predict([[140,1]]))