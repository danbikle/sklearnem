# gentrain_test.py

# This script should give me two sets of CSV files.
# In the first set, the training set,
# Each file should contain 30 years of data.
# Actually that is configurable, but 30 years is good.

# Demo:
# python ~/sklearnem/multiyr/gentrain_test.py ftrGSPC2.csv 30 2010 2016
# Above demo gives me:
# ~/ddata/train2010.csv
# ~/ddata/train2011.csv
# ~/ddata/train2012.csv
# ~/ddata/train2013.csv
# ~/ddata/train2014.csv
# ~/ddata/train2015.csv
# ~/ddata/train2016.csv
#
# ~/ddata/test2010.csv
# ~/ddata/test2011.csv
# ~/ddata/test2012.csv
# ~/ddata/test2013.csv
# ~/ddata/test2014.csv
# ~/ddata/test2015.csv
# ~/ddata/test2016.csv
# For each year, the train data should not overlap the test data.

import pandas as pd
import numpy  as np
import pdb

# I should check cmd line arg
import sys
if (len(sys.argv) < 5):
  print('Demo:')
  print('cd ~/ddata')
  print('python ~/sklearnem/multiyr/gentrain.py ftrGSPC2.csv 30 2010 2016')
  print('...')
  sys.exit()

infile = sys.argv[1]
print('I am building CSV files from this file:')
print(infile)
print('Busy...')
numyr   = int(sys.argv[2])
startyr = int(sys.argv[3])
finalyr = int(sys.argv[4])

# I should create a loop which builds the files I want:

for yr in range(startyr,1+finalyr):
  boundry_right = str(yr)
  boundry_left  = str(yr-numyr)
  # I should create a DF from infile
  in_df = pd.read_csv(infile)
  # I should get RHS of df:
  rhs_pred = (in_df['cdate'] > boundry_left)
  rhs_df   =  in_df[rhs_pred]
  # I should get LHS of df:
  lhs_pred = (rhs_df['cdate'] < boundry_right)
  lhs_df   =  rhs_df[lhs_pred]
  # I should write the df to csv file:
  lhs_df.to_csv('train'+str(yr)+'.csv', float_format='%4.3f', index=False)
  # I should get the test data now.
  boundry_right_test = str(yr+1)
  boundry_left_test  = str(yr)
  # I should create a DF from infile
  in_df = pd.read_csv(infile)
  # I should get RHS of df:
  rhs_test_pred = (in_df['cdate'] > boundry_left_test)
  rhs_test_df   =  in_df[rhs_test_pred]
  # I should get LHS of df:
  lhs_test_pred = (rhs_test_df['cdate'] < boundry_right_test)
  lhs_test_df   =  rhs_test_df[lhs_test_pred]
  # I should write the df to csv file:
  lhs_test_df.to_csv('test'+str(yr)+'.csv', float_format='%4.3f', index=False)
# I should now have some CSV files.
# They might look something like this:
#-rw-rw-r-- 1 dan dan   13144 Mar 27 09:17 /home/dan/ddata/test2010.csv
#-rw-rw-r-- 1 dan dan   13239 Mar 27 09:17 /home/dan/ddata/test2011.csv
#-rw-rw-r-- 1 dan dan   13093 Mar 27 09:17 /home/dan/ddata/test2012.csv
#-rw-rw-r-- 1 dan dan   13120 Mar 27 09:17 /home/dan/ddata/test2013.csv
#-rw-rw-r-- 1 dan dan   13144 Mar 27 09:17 /home/dan/ddata/test2014.csv
#-rw-rw-r-- 1 dan dan   13272 Mar 27 09:17 /home/dan/ddata/test2015.csv
#-rw-rw-r-- 1 dan dan    3031 Mar 27 09:17 /home/dan/ddata/test2016.csv
#-rw-rw-r-- 1 dan dan  390869 Mar 27 09:17 /home/dan/ddata/train2010.csv
#-rw-rw-r-- 1 dan dan  391049 Mar 27 09:17 /home/dan/ddata/train2011.csv
#-rw-rw-r-- 1 dan dan  391164 Mar 27 09:17 /home/dan/ddata/train2012.csv
#-rw-rw-r-- 1 dan dan  391136 Mar 27 09:17 /home/dan/ddata/train2013.csv
#-rw-rw-r-- 1 dan dan  391240 Mar 27 09:17 /home/dan/ddata/train2014.csv
#-rw-rw-r-- 1 dan dan  391246 Mar 27 09:17 /home/dan/ddata/train2015.csv
#-rw-rw-r-- 1 dan dan  391602 Mar 27 09:17 /home/dan/ddata/train2016.csv


