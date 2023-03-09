# =======================================================================================================
# Table of Contents START
# =======================================================================================================

'''
1. Orientation
2. Imports
3. prep_iris
4. prep_titanic
5. prep_telco
6. prep_split
'''

# =======================================================================================================
# Table of Contents END
# Table of Contents TO Orientation
# Orientation START
# =======================================================================================================

'''
The purpose of this file is to prepare the dataframes created from the 'acquire.py' file to ensure
consistency with users and starting data
'''

# =======================================================================================================
# Orientation END
# Orientation TO Imports
# Imports START
# =======================================================================================================

import pandas as pd
import acquire

# =======================================================================================================
# Imports END
# Imports TO prep_iris
# prep_iris START
# =======================================================================================================

def prep_iris():
    '''
    Takes the 'iris.csv' dataframe from 'acquire.py' and prepares the dataframe for use with
    consistent data structuring
    '''
    iris_db = acquire.get_iris_data()
    iris_db = iris_db.drop(columns=['species_id', 'measurement_id'])
    iris_db = iris_db.rename(columns={'species_name' : 'species'})
    return iris_db

# =======================================================================================================
# prep_iris END
# prep_iris TO prep_titanic
# prep_titanic START
# =======================================================================================================

def prep_titanic():
    '''
    Takes the 'titanic.csv' dataframe from 'acquire.py' and prepares the dataframe for use with
    consistent data structuring
    '''
    titanic_db = acquire.get_titanic_data()
    titanic_db = titanic_db.drop(columns=['passenger_id', 'sibsp', 'parch', 'embarked', 'class'])
    return titanic_db

# =======================================================================================================
# prep_titanic END
# prep_titanic TO prep_telco
# prep_telco START
# =======================================================================================================

def prep_telco():
    '''
    Takes the 'telco.csv' dataframe from 'acquire.py' and prepares the dataframe for use with
    consistent data structuring
    '''
    telco_db = acquire.get_telco_data()
    telco_db = telco_db.drop(columns=['contract_type_id', 'payment_type_id', 'internet_service_type_id'])
    return telco_db

# =======================================================================================================
# prep_telco END
# prep_telco TO prep_split
# prep_split START
# =======================================================================================================

def prep_split():
    '''
    Takes a dataframe and splits the data into a train, test and validate datasets
    '''
    print('stuff')

# =======================================================================================================
# prep_split END
# =======================================================================================================