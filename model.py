# =======================================================================================================
# Table of Contents START
# =======================================================================================================

'''
1. Orientation
2. Imports
3. decisiontree_model_iterator
4. randomforest_model_iterator
5. knn_model_iterator
'''

# =======================================================================================================
# Table of Contents END
# Table of Contents TO Orientation
# Orientation START
# =======================================================================================================

'''
The purpose of this file is to help with modeling and speed up the process of creating models,
visualizations, and possible best models to utilize
'''

# =======================================================================================================
# Orientation END
# Orientation TO Imports
# Imports START
# =======================================================================================================

# Basic sheiza
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Stat/Exploration
from scipy import stats

# Modeling
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier

# .py files
import acquire
import prepare
import explore

# =======================================================================================================
# Imports END
# Imports TO decisiontree_model_iterator
# decisiontree_model_iterator START
# =======================================================================================================

def decisiontree_model_iterator():
    print('yeet')

# =======================================================================================================
# decisiontree_model_iterator END
# decisiontree_model_iterator TO randomforest_model_iterator
# randomforest_model_iterator START
# =======================================================================================================

def randomforest_model_iterator():
    print('yeet')

# =======================================================================================================
# randomforest_model_iterator END
# randomforest_model_iterator TO knn_model_iterator
# knn_model_iterator START
# =======================================================================================================

def knn_model_iterator():
    print('yeet')

# =======================================================================================================
# knn_model_iterator END
# =======================================================================================================