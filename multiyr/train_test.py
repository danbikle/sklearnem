# train_test.py

# This script should use train and test CSV data in ~/ddata/
# to train and test.

# The results should get written to CSV files in ~/ddata/
import numpy  as np
import pandas as pd
import pdb

# I should check cmd line arg
import sys
if (len(sys.argv) < 3):
  print('Demo:')
  print('cd ~/ddata')
  print('python ~/sklearnem/multiyr/train_test.py 2010 2016')
  print('...')
  sys.exit()

startyr = int(sys.argv[1])
finalyr = int(sys.argv[2])

# I should create a loop which does train and test for each yr.
for yr in range(startyr,1+finalyr):
  trainf = 'train'+str(yr)+'.csv'
  train_df = pd.read_csv(trainf)
  train_a  = np.array(train_df)
  # I should declare some integers to help me navigate the Arrays.
  cdate_i   = 0
  cp_i      = 1
  pctlead_i = 2
  pctlag1_i = 3
  pctlag2_i = 4
  pctlag4_i = 5
  pctlag8_i = 6
  end_i     = 7
  x_train_a = train_a[:,pctlag1_i:end_i]
  y_train_a = train_a[:,pctlead_i]
  train_median  = np.median(y_train_a)
  label_train_a = y_train_a > train_median
  # I should learn from x_train_a,label_train_a:

  from sklearn import linear_model
  clf_lr = linear_model.LogisticRegression()

  from sklearn.naive_bayes import GaussianNB
  clf_nb = GaussianNB()

  clf_nb.fit(x_train_a, label_train_a)
  # Now that I have learned, I should predict:
  testf    = 'test'+str(yr)+'.csv'
  test_df  = pd.read_csv(testf)
  test_a   = np.array(test_df)
  x_test_a = test_a[:,pctlag1_i:end_i]
  y_test_a = test_a[:,pctlead_i]
  label_test_a  = y_test_a > train_median
  predictions_nb_l = []
  xcount           = -1
  x_eff_l          = [0.0]
  recent_eff_nb_l     = [0.0]
  acc_nb_l            = []
  for xoos_a in x_test_a:
    xcount        += 1 # should == 0 1st time through
    xf_a           = xoos_a.astype(float)
    xr_a           = xf_a.reshape(1, -1)
    # aprediction = clf.predict_proba(xr_a)[0,1]
    aprediction_nb    = clf_nb.predict(xr_a)
    # if (aprediction > 0.5):
    if (aprediction_nb[0] == True):
      predictions_nb_l.append(1)  # up   prediction
    else:
      predictions_nb_l.append(-1) # down prediction
    # I should save effectiveness of this prediction:
    pctlead = y_test_a[xcount]
    x_eff_l.append(predictions_nb_l[xcount]*pctlead)
    # I should save recent effectiveness of this prediction:
    if (xcount < 5):
      recent_eff_nb_l.append(0.0)
    else:
      recent_eff_nb_l.append(np.mean(x_eff_l[-5:]))
    # I should save accuracy of this prediction
    if ((y_test_a[xcount] > 0) and (aprediction_nb > 0.5)):
      acc_nb_l.append('tp')
    if ((y_test_a[xcount] > 0) and (aprediction_nb < 0.5)):
      acc_nb_l.append('fn')
    if ((y_test_a[xcount] < 0) and (aprediction_nb > 0.5)):
      acc_nb_l.append('fp')
    if ((y_test_a[xcount] < 0) and (aprediction_nb < 0.5)):
      acc_nb_l.append('tn')
  # I should save predictions_nb_l, eff, acc, so I can report later.
  test_df['actual_dir']       = np.sign(test_df['pctlead'])
  test_df['pdir_nb']          = predictions_nb_l
  test_df['x_eff']            = x_eff_l[1:]
  test_df['recent_eff_nb_nb'] = recent_eff_nb_l[1:]
  if (len(test_df) - len(acc_nb_l) == 1):
    # I should deal with most recent observation:
    acc_nb_l.append('unknown')
  test_df['accuracy_nb'] = acc_nb_l
  # I should write to CSV:
  test_df.to_csv('predictions'+str(yr)+'.csv', float_format='%4.3f', index=False)

'bye'

