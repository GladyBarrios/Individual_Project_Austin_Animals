from lib2to3.pgen2.pgen import DFAState
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.model_selection import train_test_split


def get_animal_data():
        # If csv file exists read in data from csv file.
    df = pd.read_csv('Austin_Animal_Center_Outcomes.csv', index_col=0)   
    return df


def prep_animal_data(df):
    df = df.rename(columns={'Date of Birth': 'DOB', 'Outcome Type':'outcome', 'Outcome Subtype':'subtype', 'Animal Type': 'animal_type', 'Sex upon Outcome': 'sex', 'Age upon Outcome': 'age_upon_outcome'})
    df['Name'] = df.Name.fillna(value='No_name')
    df = df.drop(columns='subtype')
    df = df.dropna()
    df = df.replace('-1 years', '1 year')
    df = df.replace('-2 years', '2 years')
    df = df.replace('-3 years', '3 years')
    df.DOB = pd.to_datetime(df.DOB)
    df['year_born'] = df.DOB.dt.year
    df['current_age'] = 2022 - df.year_born
    df['age_bin'] = pd.cut(df.current_age, 
                           bins = [0, 5, 10, 15, 20, 25, 30],
                           labels = ['below 5yrs', 'over 5yrs', 'over 10yrs', 'over 15yrs', 'over 20yrs', 'over 25yrs'])
    
    df.MonthYear = pd.to_datetime(df.MonthYear) 
    df.DateTime = pd.to_datetime(df.DateTime)
    df['year_released'] = df.DateTime.dt.year
    df['age_out_years'] = df.year_released - df.year_born
    df['Age_upon_out'] = df.DateTime - df.DOB
    df['days_old'] = df.Age_upon_out.dt.days

    df = df.replace(-1, 1)
    df = df.replace(-2, 2)
    df = df.replace(-3, 3)

    dummies = pd.get_dummies(df['outcome'])
    df = pd.concat([df, dummies], axis=1)
    
    dummies2 = pd.get_dummies(df[['animal_type','sex']])
    df = pd.concat([df, dummies2], axis=1)
    return df


def train_validate_test_split(df, target, seed=123):
    '''
    This function takes in a dataframe, the name of the target variable
    (for stratification purposes), and an integer for a setting a seed
    and splits the data into train, validate and test. 
    Test is 20% of the original dataset, validate is .30*.80= 24% of the 
    original dataset, and train is .70*.80= 56% of the original dataset. 
    The function returns, in this order, train, validate and test dataframes. 
    '''
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=seed, 
                                            stratify=df[target])
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=seed,
                                       stratify=train_validate[target])
    return train, validate, test