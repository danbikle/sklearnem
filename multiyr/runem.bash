#!/bin/bash

# runem.bash

# This script should collect accuracy and effectiveness of ML algorithms
# which predict multiple years.

# This script depends on wgetGSPCnight.bash
# I should/can run       wgetGSPCnight.bash
# before I run this script:
# ~/sklearnem/multiyr/wgetGSPCnight.bash
# I dont need to run it everytime though.

# I start by generating features from prices:
cd     ~/ddata
python ~/sklearnem/multiyr/genf.py GSPC2.csv
head   ftrGSPC2.csv
tail   ftrGSPC2.csv

exit

