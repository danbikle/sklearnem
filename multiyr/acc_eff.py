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
  pdb.set_trace()
  pred_df.tail()
  # I should count tp predictions
  tp_pred = (pred_df['accuracy'] == 'tp')
  tp_df   =  pred_df[tp_pred]
  tp_df.head()
  tp_df.tail()

