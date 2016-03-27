# gentrain.py

# This script should give me a set of CSV files.
# Each file should contain 30 years of data.
# Actually that is configurable, but 30 years is good.

# Demo:
# python ~/sklearnem/multiyr/gentrain.py ftrGSPC2.csv 30 2010 2016
# Above demo gives me:
# ~/ddata/train2010.csv
# ~/ddata/train2011.csv
# ~/ddata/train2012.csv
# ~/ddata/train2013.csv
# ~/ddata/train2014.csv
# ~/ddata/train2015.csv
# ~/ddata/train2016.csv
# Each file should contain 30 years of observations.
# For example, the last observation in train2016.csv
# Should be:
# 2015-12-31,2043.940,-1.530,-0.941,-1.656,-0.827,1.914

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
print('I am building training CSV files from this file:')
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
