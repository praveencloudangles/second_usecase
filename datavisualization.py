print("data visualization")

from data_cleaning import final_df
import matplotlib.pyplot as plt
import seaborn as sns

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
        q75,q25 = np.percentile(dataset.loc[:,x],[75,25])
        intr_qr = q75-q25    
        max = q75+(1.5*intr_qr)
        min = q25-(1.5*intr_qr)    
        dataset.loc[dataset[x] < min,x] = np.nan
        dataset.loc[dataset[x] > max,x] = np.nan


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
