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