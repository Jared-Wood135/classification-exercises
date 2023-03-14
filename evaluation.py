# =======================================================================================================
# Table of Contents START
# =======================================================================================================

'''
1. Orientation
2. Imports
3. specificity
4. accuracy
5. precision
6. recall
7. sensitivity_true_positive_rate
8. negative_predictive_value
9. f1_score
'''

# =======================================================================================================
# Table of Contents END
# Table of Contents TO Orientation
# Orientation START
# =======================================================================================================

'''
The purpose of this file is to help with model evaluations and output their respective percents...

Friendly reminder...
sklearn.metrics.confusion_matrix returns a 2x2 array which then means:
    - True Positive (TP) = [0, 0]
    - False Positive (FP) = [0, 1]
    - True Negative (TN) = [1, 1]
    - False Negative (FN) = [1, 0]
    - POSITION OF LABELS DICTATE WHAT IS DETERMINED TP OR NOT
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
    '''
    Iterates through all columns with the specificity model metric...
    Specificity measures how well a model predicts negative outcomes...
    Specificity = (TN / (FP + TN))
    '''
    for col in df:
        matrix = confusion_matrix(df[actual_col], df[col], labels=(Truelabel, Falselabel))
        result = (matrix[1, 1] / (matrix[0, 1] + matrix[1, 1]))
        print(f'\033[32m{col}:\033[0m {result:.2%}\n')

# =======================================================================================================
# specificity END
# specificity TO accuracy
# accuracy START
# =======================================================================================================

def accuracy(df, actual_col):
    '''
    Iterates through all columns with the accuracy model metric...
    Accuracy measures how many correct predictions over total possible predictions...
    Accuracy = ((TP + TN) / (TP + FP + FN + TN))
    '''
    for col in df:
        ratio = (df[col] == df[actual_col]).mean()
        print(f'\033[32m{col}:\033[0m {ratio:.2%}\n')

# =======================================================================================================
# accuracy END
# accuracy TO precision
# precision START
# =======================================================================================================

def precision(df, actual_col, Truelabel, Falselabel):
    '''
    Iterates through all columns with the precision model metric...
    Precision measures how many of the positive predictions were correct...
    Precision = (TP / (TP + FP))
    '''
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
    '''
    Iterates through all columns with the recall model metric...
    Recall measures how the model handled all positive outcomes...
    Recall = (TP / (TP + FN))
    '''
    for col in df:
        matrix = confusion_matrix(df[actual_col], df[col], labels=(Truelabel, Falselabel))
        ratio = (matrix[0, 0] / (matrix[0, 0] + matrix[1, 0]))
        print(f'\033[32m{col}:\033[0m {ratio:.2%}\n')

# =======================================================================================================
# recall END
# recall TO sensitivity_true_positive_rate
# sensitivity_true_positive_rate START
# =======================================================================================================

def sensitivity_true_positive_rate(df, actual_col, Truelabel, Falselabel):
    '''
    Iterates through all columns with the sensitivity true positive rate model metric...
    Sensitivity true positive rate measures the proportion of positives correctly identified...
    Sensitivity true positive rate = (TP / (TP + FN))
    '''
    for col in df:
        matrix = confusion_matrix(df[actual_col], df[col], labels=(Truelabel, Falselabel))
        ratio = (matrix[0, 0] / (matrix[0, 0] + matrix[1, 0]))
        print(f'\033[32m{col}:\033[0m {ratio:.2%}\n')

# =======================================================================================================
# sensitivity_true_positive_rate END
# sensitivity_true_positive_rate TO negative_predictive_value
# negative_predictive_value START
# =======================================================================================================

def negative_predictive_value(df, actual_col, Truelabel, Falselabel):
    '''
    Iterates through all columns with the negative predictive value model metric...
    Negative predictive value measures the probability that a predicted negative is a true negative...
    Negative predictive value = (TN / (TN + FN))
    '''
    for col in df:
        matrix = confusion_matrix(df[actual_col], df[col], labels=(Truelabel, Falselabel))
        ratio = (matrix[1, 1] / (matrix[1, 1] + matrix[1, 0]))
        print(f'\033[32m{col}:\033[0m {ratio:.2%}\n')

# =======================================================================================================
# negative_predictive_value END
# negative_predictive_value TO f1_score
# f1_score START
# =======================================================================================================

def f1_score(df, actual_col, Truelabel, Falselabel):
    '''
    Iterates through all columns with the f1 score model metric...
    F1 score measures a model's accuracy on a dataset...
    F1 score = 2 * ((Precision * Recall) / (Precision + Recall))
    '''
    for col in df:
        matrix = confusion_matrix(df[actual_col], df[col], labels=(Truelabel, Falselabel))
        precision = (matrix[0, 0] / (matrix[0, 0] + matrix[0, 1]))
        recall = (matrix[0, 0] / (matrix[0, 0] + matrix[1, 0]))
        ratio = ((precision * recall) / (precision + recall))
        print(f'\033[32m{col}:\033[0m {ratio:.2%}\n')

# =======================================================================================================
# f1_score END
# =======================================================================================================