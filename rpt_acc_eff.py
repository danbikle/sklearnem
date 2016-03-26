# rpt_acc_eff.py

import numpy  as np
import pandas as pd

# This script should help report accuracy and effectiveness.

def rpt_acc_eff(predictions_l):
  # I should match the predictions to the test observations.
  test_df         = pd.read_csv('test.csv')
  test_df['pdir'] = predictions_l
  # Get actual_direction of each test observation, which is sign of pctlead
  
  test_df['actual_dir'] = np.sign(test_df['pctlead'])
  
  # I should count positive predictions.
  posp_df  = test_df[['pdir','actual_dir']][test_df['pdir'] == 1]
  # I should count true positive predictions.
  tposp_df = posp_df[posp_df['actual_dir'] == 1]
  # I should calculate positive accuracy.
  pos_acc  = 100.0 * len(tposp_df)/len(posp_df)
  
  # I should count negative predictions.
  negp_df  = test_df[['pdir','actual_dir']][test_df['pdir'] == -1]
  # I should count true negative predictions.
  tnegp_df = negp_df[negp_df['actual_dir'] == -1]
  # I should calculate negative accuracy.
  neg_acc  = 100.0 * len(tnegp_df)/len(negp_df)
  
  # I should calculate combined accuracy
  com_acc  = 100.0 * (len(tposp_df)+len(tnegp_df))/len(test_df)
  
  # I should calculate 'effectiveness'.
  pos_pctlead_a = np.array(test_df[['pctlead']][test_df['pdir'] == 1])
  pos_eff       = np.mean(pos_pctlead_a)
  neg_pctlead_a = np.array(test_df[['pctlead']][test_df['pdir'] == -1])
  neg_eff       = np.mean(neg_pctlead_a)
  longonly_eff  = np.mean(test_df['pctlead'].values)
  # I should report
  print('True  positive count: '+str(len(tposp_df)))
  print('False positive count: '+str(len(posp_df)-len(tposp_df)))
  print('True  negative count: '+str(len(tnegp_df)))
  print('False negative count: '+str(len(negp_df)-len(tnegp_df)))
  
  print('Accuracy of positive predictions: ' +str(pos_acc)[:6]+'%')
  print('Accuracy of negative predictions: ' +str(neg_acc)[:6]+'%')
  print('Combined Accuracy of predictions: ' +str(com_acc)[:6]+'%')
  print('Positive Effectiveness: '  +str(pos_eff)[:6]+'%')
  print('Negative Effectiveness: '  +str(neg_eff)[:6]+'%')
  print('Long Only Effectiveness: ' +str(longonly_eff)[:6]+'%')
  
  'bye'
