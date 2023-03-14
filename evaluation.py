# =======================================================================================================
# Table of Contents START
# =======================================================================================================

'''
1. Orientation
2. Imports
3. specificity
4. accuracy
5. precision
'''

# =======================================================================================================
# Table of Contents END
# Table of Contents TO Orientation
# Orientation START
# =======================================================================================================

'''
The purpose of this file is to help with model evaluations and output their respective percents
'''

# =======================================================================================================
# Orientation END
# Orientation TO Imports
# Imports START
# =======================================================================================================

import pandas as pd
import sklearn.metrics
from sklearn.metrics import confusion_matrix

# =======================================================================================================
# Imports END
# Imports TO specificity
# specificity START
# =======================================================================================================

def specificity(df, actual_col, Truelabel, Falselabel):
    for col in df:
        matrix = confusion_matrix(df[actual_col], df[col], labels=(Truelabel, Falselabel))
        result = (matrix[1, 1] / (matrix[1, 0] + matrix[1, 1]))
        print(f'\033[32m{col}:\033[0m {result:.2%}\n')

# =======================================================================================================
# specificity END
# specificity TO accuracy
# accuracy START
# =======================================================================================================

def accuracy(df, actual_col):
    for col in df:
        ratio = (df[col] == df[actual_col]).mean()
        print(f'\033[32m{col}:\033[0m {ratio:.2%}\n')

# =======================================================================================================
# accuracy END
# accuracy TO precision
# precision START
# =======================================================================================================

def precision(df, actual_col, Truelabel, Falselabel):
    for col in df:
        matrix = confusion_matrix(df[actual_col], df[col], labels=(Truelabel, Falselabel))
        ratio = (matrix[0, 0] / (matrix[0, 0] + matrix[0, 1]))
        print(f'\033[32m{col}:\033[0m {ratio:.2%}\n')

# =======================================================================================================
# precision END
# precision TO recall
# recall START
# =======================================================================================================

def recall(df, actual_col, Truelabel, Falselabel):
    for col in df:
        matrix = confusion_matrix(df[actual_col], df[col], labels=(Truelabel, Falselabel))
        ratio = (matrix[0, 0] / (matrix[0, 0] + matrix[0, 1]))
        print(f'\033[32m{col}:\033[0m {ratio:.2%}\n')