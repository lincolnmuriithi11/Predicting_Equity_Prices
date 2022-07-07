# Stock Prices Predictor

## Purpose
This project aims to predict stock prices by using timeseries LSTM deep learning methodologies using the price alone.

The customer: Trading team.

## Deliverables
     - A clearly named final notebook. This notebook will be what you present and should contain plenty of markdown    documentation and cleaned up code.
    -A README that explains what the project is, how to reproduce you work, and your notes from project planning.
    -A Python module or modules that automate the data acquisistion and preparation process. These modules should be imported and used in your final notebook.
# Data Science Pipeline

## Acquiring and Preparing Stock Data
#### - Data is acquired from Yahoo finance from 2007-01-01 to 2022-06-30
#### - Engineered features: simple moving average(sma), percent_change
#### - Data has 3901 rows, 6 columns before cleaning and 3901 rows and 4 columns after
#### -  columns dropped : 
    "Open", "High", "Low", "Adj_Close"
#### - Split the data into train, validate, test
#### - Scaled data using a minmax scaler


## #Data Dictionary
        1. "Close" - Closing price for the S&P 500 from 2007 to June 2022
        2. "Volume" - number of stocks swithcing hands everyday in billions of dollars 
        3. "percent_change" - percent change of the price everyday
        4. "sma" - simple moving average of the closing price
# Data Exploration
### Goal: Address questions generated during planning and preparation phases
#### is there visible seasonality?
#### does any of the features have a normal distribution?
#### does the volume have a  relationship with the Closing price?

# Modeling & Evaluation
#### implimenting an LSTM model based on the price alone

