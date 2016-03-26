# gbrt10.py

# This script should demo GBRT.

# ref:
# http://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html

# Author: Peter Prettenhofer <peter.prettenhofer@gmail.com>
#
# License: BSD 3 clause

import numpy as np
import matplotlib.pyplot as plt

from sklearn import ensemble
from sklearn import datasets
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_error

