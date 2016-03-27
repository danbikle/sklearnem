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
python ~/sklearnem/multiyr/gentrain_test.py ftrGSPC2.csv 30 2010 2016
# The above call should give me a set of CSV files.
# Each file should contain 30 years of data.

exit

