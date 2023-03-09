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
from sklearn.model_selection import train_test_split

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
    dummies = pd.get_dummies(iris_db['species'])
    iris_db = pd.concat([iris_db, dummies], axis=1)
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
    titanic_db = titanic_db.drop(columns=['passenger_id', 'sibsp', 'parch', 'embarked', 'class', 'deck'])
    titanic_db.embark_town = titanic_db.embark_town.fillna('Southampton')
    titanic_db.age = titanic_db.age.fillna(titanic_db.age.mean())
    dummies = pd.get_dummies(titanic_db[['sex', 'embark_town']])
    titanic_db = pd.concat([titanic_db, dummies], axis=1)
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
    dummies = pd.get_dummies(telco_db.select_dtypes(include='object'))
    telco_db = pd.concat([telco_db, dummies], axis=1)
    return telco_db

# =======================================================================================================
# prep_telco END
# prep_telco TO prep_split
# prep_split START
# =======================================================================================================

def prep_split(df):
    '''
    Takes a dataframe and splits the data into a train, validate and test datasets
    '''
    strat = input('What column do you want to stratify on')
    train_val, test = train_test_split(df, train_size=0.8, random_state=1349, stratify=df[strat])
    train, validate = train_test_split(train_val, train_size=0.7, random_state=1349, stratify=train_val[strat])
    print(f"train.shape:{train.shape}\nvalidate.shape:{validate.shape}\ntest.shape:{test.shape}")
    return train, validate, test

# =======================================================================================================
# prep_split END
# =======================================================================================================