# prep4fit.py

# This script should read training.csv
# and then prepare data for fit().
# Another way to describe this script:
# Prepare data so I can learn from it.

import pandas as pd
import numpy  as np
import pdb

trainf   = 'training.csv'
train_df = pd.read_csv(trainf)

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
# I should build X-arrays (I call this 'independent' data).
x_train_a = train_a[:,pctlag1_i:end_i]
