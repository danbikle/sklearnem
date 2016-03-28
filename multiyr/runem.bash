#!/bin/bash

# runem.bash

# This script should collect accuracy and effectiveness of ML algorithms
# which predict multiple years.

# This script depends on wgetGSPCnight.bash
# I should/can run       wgetGSPCnight.bash
# before I run runem.bash:
# ~/sklearnem/multiyr/wgetGSPCnight.bash
# I dont need to run it everytime though.
# wgetGSPCnight.bash should give me ~/ddata/GSPC2.csv
# I start by generating features from prices:
cd     ~/ddata
python ~/sklearnem/multiyr/genf.py GSPC2.csv
# Now, I should have ftrGSPC2.csv 
echo I should see some data:
head   ftrGSPC2.csv
echo I should see some data:
tail   ftrGSPC2.csv

# Next I generate training data CSV files:
STARTYR=2010
ENDYR=2016
python ~/sklearnem/multiyr/gentrain_test.py ftrGSPC2.csv 30 $STARTYR $ENDYR
# The above call should give me two sets of CSV files.
# Each training CSV file should contain 30 years of data.
# Each test CSV file should contain 1 year of data.

# Then I should train and test.
python ~/sklearnem/multiyr/train_test.py $STARTYR $ENDYR
# Now I should have CSV files with predictions mixed with actual results.

# Then I should report accuracy and effectiveness.
python ~/sklearnem/multiyr/acc_eff.py $STARTYR $ENDYR

# Then I should build blue-green visualizations.
python ~/sklearnem/multiyr/rgb.py $STARTYR $ENDYR

exit

