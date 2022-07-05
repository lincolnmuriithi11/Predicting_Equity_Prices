################ Libraries and documents needed for this project ################
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
# train test split from sklearn
from sklearn.model_selection import train_test_split
# imputer from sklearn
from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np
import os

import warnings
warnings.filterwarnings("ignore")

from math import sqrt
from scipy import stats
from statsmodels.formula.api import ols
from sklearn.metrics import mean_squared_error, explained_variance_score
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE, SelectKBest, f_regression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, QuantileTransformer


#this function takes the zillow data frame and cleans for modeling 
def wrangle_spy(df):
    df["sma"] = df["Close"].rolling(window = 20, min_periods =1).mean()
    df["percent_change"] = (df.Close - df.Open)/df.Open
    df.columns = df.columns.str.replace(' ','_') #replacing spaces for underscore
    column_to_drop = ["Open", "High", "Low", "Adj_Close"]#dropping unnecessary columns
    df = df.drop(columns = column_to_drop)# dropped taxamount column because of the high correlation with taxvaluedollarcnt(due to data leakage)

    return df


    
# this function is splitting data to train, validate, and test to avoid data leakage
def split_data(df):
    '''
    This function performs split on zillow data, stratify taxvaluedollarcnt.
    Returns train, validate, and test dfs.
    '''
    train_size = 1950
    validate_size = 1170
    test_size = 780
    validate_end_index = train_size + validate_size
    # train will go from 0 to 1259
    train = df[:train_size]
    validate = df[train_size:validate_end_index]
    test = df[validate_end_index:]

    return train, validate, test


