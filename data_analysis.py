print("data analysis")

from data_loading import df, df1, df2, df3

# Checking for null values in a dataframe.

df_null=df.isnull().sum()
# print("checking first dataframe null values ----------",df_null)

df1_null = df1.isnull().sum()
# print("checking second dataframe null values---------", df1_null)

df2_null=df2.isnull().sum()
# print("checking fourth dataframe null values----------", df2_null)

df3_null = df3.isnull().sum()
# print("checking fourth dataframe null values----------", df3_null)


#checking duplicated values in a dataframe.

df_duplicated=df.duplicated().sum()
# print("checking for duplicated values for first dataframe--------", df_duplicated)

df1_duplicated=df.duplicated().sum()
# print("checking for duplicated values for second dataframe---------", df1_duplicated)

df2_duplicated=df2.duplicated().sum()
# print("checking for duplicated values for third dataframe-----------", df2_duplicated)

df3_duplicated = df3.duplicated().sum ()
# print("checking for duplicated values for fourth dataframe---------", df3_duplicated)


# Checking for outliers.

df_outliers = df.describe()
# print("checking for outliers in first dataframe-----------", df_outliers)

df1_outliers = df1.describe()
# print("checking for outliers in second dataframe-----------", df1_outliers)

df2_outliers = df2.describe()
# print("checking for outliers in third dataframe-------------", df2_outliers)

df3_outliers = df3.describe()
# print("checking for outliers in fourth dataframe", df3_outliers)