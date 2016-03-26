# linear_regression10.py

# Ref:
# http://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares

from sklearn import linear_model
clf = linear_model.LinearRegression()
clf.fit ([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
print(clf.coef_)
prediction = clf.predict([[3,3]])
print(prediction)



