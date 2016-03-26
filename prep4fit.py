# prep4fit.py

# This script should read training.csv
# and then prepare data for fit().
# Another way to describe this script:
# Prepare data so I can learn from it.
# Also I use this script to prepare data for testing.

import pandas as pd
import numpy  as np
import pdb

def get_x_train_a():
  trainf   = 'training.csv'
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
  upf_i     = 7
  lowf_i    = 8
  end_i     = 9
  x_train_a = train_a[:,pctlag1_i:end_i]
  return x_train_a

def get_train_a():
  trainf    = 'training.csv'
  train_df  = pd.read_csv(trainf)
  train_a   = np.array(train_df)
  return train_a

def get_y_train_a():
  train_a   = get_train_a()
  # I should declare some integers to help me navigate the Arrays.
  cdate_i   = 0
  cp_i      = 1
  pctlead_i = 2
  y_train_a = train_a[:,pctlead_i]
  return y_train_a

def get_label_train_a():
  trainf   = 'training.csv'
  train_df = pd.read_csv(trainf)
  train_a  = np.array(train_df)
  # I should declare some integers to help me navigate the Arrays.
  pctlead_i = 2
  y_train_a = train_a[:,pctlead_i]
  train_median  = np.median(y_train_a)
  label_train_a = y_train_a > train_median
  return label_train_a

def get_x_test_a():
  testf   = 'test.csv'
  test_df = pd.read_csv(testf)
  test_a  = np.array(test_df)
  # I should declare some integers to help me navigate the Arrays.
  cdate_i   = 0
  cp_i      = 1
  pctlead_i = 2
  pctlag1_i = 3
  pctlag2_i = 4
  pctlag4_i = 5
  pctlag8_i = 6
  upf_i     = 7
  lowf_i    = 8
  end_i     = 9
  x_test_a  = test_a[:,pctlag1_i:end_i]
  return x_test_a

def get_label_test_a():
  testf   = 'test.csv'
  test_df = pd.read_csv(testf)
  test_a  = np.array(test_df)
  # I should declare some integers to help me navigate the Arrays.
  pctlead_i = 2
  y_test_a  = test_a[:,pctlead_i]
  #
  trainf       = 'training.csv'
  train_df     = pd.read_csv(trainf)
  train_a      = np.array(train_df)
  y_train_a    = train_a[:,pctlead_i]
  train_median = np.median(y_train_a)
  #
  label_test_a = y_test_a > train_median
  return label_test_a

def get_test_a():
  testf    = 'test.csv'
  test_df  = pd.read_csv(testf)
  test_a   = np.array(test_df)
  return test_a

def get_y_test_a():
  test_a    = get_test_a()
  # I should declare some integers to help me navigate the Arrays.
  cdate_i   = 0
  cp_i      = 1
  pctlead_i = 2
  y_test_a  = test_a[:,pctlead_i]
  return y_test_a
