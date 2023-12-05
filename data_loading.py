print("data loading")

import pandas as pd

def data_loading():

    df = pd.read_csv('car data.csv')


    df1 =pd.read_csv('CAR DETAILS FROM CAR DEKHO.csv')


    df2 = pd.read_csv('Car details v3.csv')


    df3 = pd.read_csv('car details v4.csv')

    return df, df1, df2, df3

data_loading()