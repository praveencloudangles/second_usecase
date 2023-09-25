print("data visualization")

from data_cleaning import final_df
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

final_df_copy = final_df.copy()

categ = []
numer = []

for col in final_df_copy.columns:
    if final_df_copy[col].dtypes == object:
        categ.append(col)
    else:
        numer.append(col)

# print("categorical values-------", categ)
# print("numerical values---------", numer)

for x in numer:
        q75,q25 = np.percentile(final_df_copy.loc[:,x],[75,25])
        intr_qr = q75-q25    
        max = q75+(1.5*intr_qr)
        min = q25-(1.5*intr_qr)    
        final_df_copy.loc[final_df_copy[x] < min,x] = np.nan
        final_df_copy.loc[final_df_copy[x] > max,x] = np.nan

# Box plot for numerical values.
for num in numer:
    plt.figure(figsize=(5,5))
    sns.boxplot(data=final_df_copy, x=num)
    plt.xlabel(num)
plt.show()


# violin plots for numeric values.
for num in numer:
    plt.figure(figsize=(5, 5))
    sns.violinplot(data=final_df_copy, x=num)
    plt.xlabel(num)
plt.show()

final_df = final_df_copy
