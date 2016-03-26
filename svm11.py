# svm11.py

# This script should give demo of sklearn.svm.NuSVC

# Ref:
# http://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC

import numpy  as np
import pandas as pd
import prep4fit
import rpt_acc_eff
import pdb

x_train_a     = prep4fit.get_x_train_a()
label_train_a = prep4fit.get_label_train_a()
# I should learn from x_train_a,label_train_a:
from sklearn.svm import NuSVC
clf = NuSVC()
clf.fit(x_train_a, label_train_a)
# Now that I have learned, I should predict:
x_test_a      = prep4fit.get_x_test_a()
label_test_a  = prep4fit.get_label_test_a()
predictions_l = []
for xoos_a in x_test_a:
  xf_a        = xoos_a.astype(float)
  xr_a        = xf_a.reshape(1, -1)
  aprediction = clf.predict(xr_a)
  if (aprediction[0] == True):
    predictions_l.append(1)  # up   prediction
  else:
    predictions_l.append(-1) # down prediction

# I should report accuracy and effectiveness.
rpt_acc_eff.rpt_acc_eff(predictions_l)
'bye'



