# naive_bayes11.py

# This script should give demo of sklearn.naive_bayes.GaussianNB

# ref:
# http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB

import numpy  as np
import pandas as pd
import prep4fit
import pdb

x_train_a     = prep4fit.get_x_train_a()
label_train_a = prep4fit.get_label_train_a()
# I should learn from x_train_a,label_train_a:
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(x_train_a,label_train_a)
# Now that I have learned, I should predict:
x_test_a     = prep4fit.get_x_test_a()
label_test_a = prep4fit.get_label_test_a()
predictions_l = []
for xoos_a in x_test_a:
  xf_a        = xoos_a.astype(float)
  xr_a        = xf_a.reshape(1, -1)
  aprediction = clf.predict(xr_a)
  if aprediction == True:
    predictions_l.append(1)  # up   prediction
  else:
    predictions_l.append(-1) # down prediction


predictions_l
# I should match the predictions to the test observations.
test_df         = pd.read_csv('test.csv')
test_df['pdir'] = predictions_l
# Get actual_direction of each test observation, which is sign of pctlead
pdb.set_trace()
test_df['actual_dir'] = np.sign(test_df['pctlead'])
test_df.head()
# I should count positive predictions.
posp_df  = test_df[['pdir','actual_dir']][test_df['pdir'] == 1]

'bye'
