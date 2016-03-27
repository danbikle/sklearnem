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
  leadp_l = cp_l[1:] + [cp_l[-1]]
  # I should get lead_l which leadp - cp
  lead_l  = list(np.array(leadp_l)-np.array(cp_l))
  pred_df['lead']  = lead_l
  pred_df['gdelta']=pred_df['actual_dir']*pred_df['pdir']*np.sign(pred_df['lead'])*pred_df['lead']
  # I should get initial green_l
  green_l = [cp_l[0]]
  gcount  = 0
  for gdelta in pred_df['gdelta']:
    gcount += 1
    green_l.append(green_l[gcount-1]+gdelta)
  #pdb.set_trace()
  len(pred_df)
  len(green_l)
  pred_df['green'] = green_l[:-1]

pdb.set_trace()
pred_df.tail()

