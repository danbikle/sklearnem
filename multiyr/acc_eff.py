# acc_eff.py

# This script should report accuracy and effectiveness from CSV files in ~/ddata/

import numpy  as np
import pandas as pd
import pdb

# I should check cmd line arg
import sys
if (len(sys.argv) < 3):
  print('Demo:')
  print('cd ~/ddata')
  print('python ~/sklearnem/multiyr/acc_eff 2010 2016')
  print('...')
  sys.exit()

startyr = int(sys.argv[1])
finalyr = int(sys.argv[2])

# I should create a loop which does train and test for each yr.
for yr in range(startyr,1+finalyr):
  predf   = 'predictions'+str(yr)+'.csv'
  pred_df = pd.read_csv(predf)
  # I should count
  tp_pred = (pred_df['accuracy'] == 'tp')
  tn_pred = (pred_df['accuracy'] == 'tn')
  fp_pred = (pred_df['accuracy'] == 'fp')
  fn_pred = (pred_df['accuracy'] == 'fn')
  tp_df   =  pred_df[tp_pred]
  tn_df   =  pred_df[tn_pred]
  fp_df   =  pred_df[fp_pred]
  fn_df   =  pred_df[fn_pred]
  tp_i = len(tp_df)
  tn_i = len(tn_df)
  fp_i = len(fp_df)
  fn_i = len(fn_df)
  print('For '+str(yr)+':')
  print('Positive, Up,   Prediction Count is '+str(tp_i+fp_i))
  print('Negative, Down, Prediciton Count is '+str(tn_i+fn_i))
  print('Positive Accuracy is '+str(tp_i / (tp_i+fp_i)))
  print('Negative Accuracy is '+str(tn_i / (tn_i+fn_i)))


