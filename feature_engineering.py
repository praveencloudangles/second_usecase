print("feature engineering")

from data_cleaning import data_cleaning
import pandas as pd
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()

def feat_eng():

    final_df = data_cleaning()
    final_copy = final_df.copy()

    # Checking the datatype for a column
    column_types = final_copy.dtypes
    print(column_types)


    columns_to_encode = ['name', 'selling_price', 'fuel', 'seller_type', 'transmission', 'owner', 'year', 'km_driven']
    for col in columns_to_encode:
        final_copy[col] = label_encoder.fit_transform(final_copy[col])

    final_df = final_copy
    print(final_df)

    final_df.to_csv('final.csv', index=False)


    return final_df

feat_eng()