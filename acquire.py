# =======================================================================================================
# Table of Contents START
# =======================================================================================================

'''
1. Orientation
2. Imports
3. get_titanic_data
4. get_iris_data
5. get_telco_data
'''

# =======================================================================================================
# Table of Contents END
# Table of Contents TO Orientation
# Orientation START
# =======================================================================================================

'''
The purpose of this file is to ensure that users have .csv files required for particular
exercises within this repository
'''

# =======================================================================================================
# Orientation END
# Orientation TO Imports
# Imports START
# =======================================================================================================

import pandas as pd
import env
import os

# =======================================================================================================
# Imports END
# Imports TO get_titanic_data
# get_titanic_data START
# =======================================================================================================

def get_titanic_data():
    if os.path.exists('titanic.csv'):
        return pd.read_csv('titanic.csv', index_col=0)
    else:
        titanic_df = pd.read_sql(
            '''
            SELECT * FROM passengers
            ''', env.get_db_url('titanic_db')
        )
        titanic_df.to_csv('titanic.csv')
        return pd.read_csv('titanic.csv', index_col=0)

# =======================================================================================================
# get_titanic_data END
# get_titanic_data TO get_iris_data
# get_iris_data START
# =======================================================================================================

def get_iris_data():
    if os.path.exists('iris.csv'):
        return pd.read_csv('iris.csv', index_col=0)
    else:
        iris_df = pd.read_sql(
            '''
            SELECT
                *
            FROM
                measurements
                LEFT JOIN species USING(species_id)
            ''', env.get_db_url('iris_db')
        )
        iris_df.to_csv('iris.csv')
        return pd.read_csv('iris.csv',index_col=0)

# =======================================================================================================
# get_iris_data END
# get_iris_data TO get_telco_data
# get_telco_data START
# =======================================================================================================

def get_telco_data():
    if os.path.exists('telco.csv'):
        return pd.read_csv('telco.csv', index_col=0)
    else:
        telco_df = pd.read_sql(
            '''
            SELECT 
                * 
            FROM 
                customers 
                LEFT JOIN internet_service_types USING(internet_service_type_id)
                LEFT JOIN payment_types USING(payment_type_id)
                LEFT JOIN contract_types USING(contract_type_id)
            ''', env.get_db_url('telco_churn')
        )
        telco_df.to_csv('telco.csv')
        return pd.read_csv('telco.csv', index_col=0)
    
# =======================================================================================================
# get_telco_data END
# =======================================================================================================