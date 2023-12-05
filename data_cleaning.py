print("data cleaning")

from data_analysis import data_analysis
import pandas as pd

def data_cleaning():
    # Cleaning for df dataframe
    # Multiplying with a number for selling price and present price.

    df, df1,df2, df3 = data_analysis()
    multiplier = 100000
    column_name = ['Selling_Price', 'Present_Price']
    df_copy = df.copy()
    df_copy[column_name] = df_copy[column_name] * multiplier

    # Drop the duplicate values.
    df_copy = df_copy.drop_duplicates()

    # Drop a column from df dataframe.
    df_copy.drop(columns=column_name[1], inplace=True)

    # Rename a column from dataframe.
    df_column_name = {'Car_Name': 'name', 'Year': 'year', 'Selling_Price': 'selling_price', 'Kms_Driven': 'km_driven', 'Fuel_Type': 'fuel', 'Seller_Type': 'seller_type', 'Transmission': 'transmission', 'Owner': 'owner'}
    df = df_copy.rename(columns=df_column_name)



    # Cleaning for df1 dataframe.
    # drop the duplicates from dataframe.
    df1_copy = df1.copy()
    df1_copy = df1_copy.drop_duplicates()

    #replcae column data with o and 1.
    replacement_df1 = {'First Owner': 0, 'Second Owner': 1, 'Third Owner': 2, 'Fourth & Above Owner': 3, 'Test Drive Car': 4}

    # Replace values in the 'owner' column
    df1_copy['owner'] = df1_copy['owner'].replace(replacement_df1)
    df1 = df1_copy



    # Cleaning for df1 dataframe.
    # Replacing null values with zero.
    df2 = pd.DataFrame(df2)
    df2[["mileage", "engine", "max_power", "torque", "seats"]] = df2[["mileage", "engine", "max_power", "torque", "seats"]].fillna(0)

    # Removing duplicate values.
    df2_copy=df2.copy()
    df2_copy = df2_copy.drop_duplicates()

    # Replace column with 0's and 1's
    replacement_df2 = {"First Owner": 0, "Fourth & Above Owner": 3, "Second Owner": 1, "Third Owner": 2, 'Test Drive Car': 4} 
    df2_copy['owner'] = df2_copy['owner'].replace(replacement_df2)

    # Displaying only one column from dataframe.
    column_name_df2 = ['owner']
    selected_columns = df2_copy[column_name_df2]

    # Drop columns from dataframe.
    df2_column_name = ['mileage', 'engine', 'max_power', 'torque', 'seats']
    df2_copy.drop(columns=df2_column_name, inplace=True)
    df2 = df2_copy


    # Cleaning for df3 dataframe.
    # Replacing null values.
    df3 = pd.DataFrame(df3)
    df3[["Engine", "Max Power", "Max Torque", "Drivetrain", "Length", "Width", "Height", "Seating Capacity", "Fuel Tank Capacity"]] = df3[["Engine", "Max Power", "Max Torque", "Drivetrain", "Length", "Width", "Height", "Seating Capacity", "Fuel Tank Capacity"]].fillna(0)

    # Replace column with 0's and 1's
    df3_copy=df3.copy()
    replacement_df3 = {"First": 0, "4 or More": 4, "Second" : 1, "Third": 2,'Fourth': 3,  "UnRegistered Car": 5}
    df3_copy['Owner'] = df3_copy['Owner'].replace(replacement_df3)

    # concatinating two columns from a dataframe.
    df3_copy['name'] = df3_copy['Make'] + ' ' + df3_copy['Model']

    # Drop columns from dataframe.
    df3_column_name = ['Engine','Max Power', 'Max Torque', 'Drivetrain', 'Length', 'Width', 'Height','Seating Capacity', 'Fuel Tank Capacity', 'Location', 'Color', 'Make', 'Model']
    df3_copy.drop(columns=df3_column_name, inplace=True)

    # Rename a column from dataframe.
    df3_column_rename = {'Price': 'selling_price', 'Year': 'year', 'Kilometer': 'km_driven', 'Fuel Type': 'fuel', 'Seller Type': 'seller_type', 'Transmission': 'transmission', 'Owner': 'owner'}
    df3 = df3_copy.rename(columns=df3_column_rename)


    frames = [df, df1, df2, df3]
    result = pd.concat(frames, ignore_index=True)


    final_df = result.drop_duplicates()

    return final_df


data_cleaning()