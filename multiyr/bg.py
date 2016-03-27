# bg.py

# This script should help me build the blue-green visualizations.

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
  # I should get leadp which is the price 1 ahead of cp:
  cp_l    = [p_f for p_f in pred_df['cp']]
  leadp_l = [cp_l[0]] + cp_l[:-1]
  # I should get lead_l which leadp - cp
  lead_l  = list(np.array(leadp_l)-np.array(cp_l))

pdb.set_trace()
cp_l[-4:]
leadp_l[-4:]
lead_l[-4:]
pred_df.tail()
