# gbrt11.py

# This script should give demo of sklearn.ensemble.GradientBoostingRegressor

# Ref:
# http://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html

import numpy  as np
import pandas as pd
import prep4fit
import rpt_acc_eff
import pdb

x_train_a = prep4fit.get_x_train_a()
y_train_a = prep4fit.get_y_train_a()
# I should learn from x_train_a,label_train_a:
from sklearn import ensemble
params = {'n_estimators': 500, 'max_depth': 4, 'min_samples_split': 1,
          'learning_rate': 0.01, 'loss': 'ls'}
clf = ensemble.GradientBoostingRegressor(**params)
clf.fit(x_train_a, y_train_a)
# Now that I have learned, I should predict:
x_test_a = prep4fit.get_x_test_a()
y_test_a = prep4fit.get_y_test_a()
predictions_l = []
for xoos_a in x_test_a:
  xf_a        = xoos_a.astype(float)
  xr_a        = xf_a.reshape(1, -1)
  aprediction = clf.predict(xr_a)
  pdb.set_trace()
  aprediction
  if aprediction[0] > 0:
    predictions_l.append(1)  # up   prediction
  else:
    predictions_l.append(-1) # down prediction

# I should report accuracy and effectiveness.
rpt_acc_eff.rpt_acc_eff(predictions_l)
'bye'



