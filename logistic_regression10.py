# logistic_regression10.py

# Ref:
# http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

from sklearn import linear_model
clf = linear_model.LogisticRegression()
clf.fit ([[0, 0], [1, 1], [2, 2]], [0, 0, 1])
# Predict the training data:
prediction0 = clf.predict_proba([[0.0,0.0]]) # 0
prediction1 = clf.predict_proba([[1.0,1.0]]) # 0
prediction2 = clf.predict_proba([[2.0,2.0]]) # 1
# Predict a test data point:
prediction08 = clf.predict_proba([[0.8,0.8]]) #?
print(prediction0)
print(prediction1)
print(prediction2)
print(prediction08)
'bye'




