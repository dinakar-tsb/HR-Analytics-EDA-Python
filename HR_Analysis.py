import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HR_Database.csv")

print(df.head())
print(df.columns)
print(df.info())
print(df.describe())

#Employee count by department
plt.figure()
ax = sns.countplot(x = "Department",data = df)
plt.title("Employee Count by Department")
plt.xticks(rotation = 30)
for bar in ax.patches:
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        int(bar.get_height()),
        ha = "center",
        va = "bottom"
    )
plt.show()

# Salary distribution
mean_salary = df["Monthly_Salary"].mean()
median_salary = df["Monthly_Salary"].median()
plt.figure()
sns.histplot(df["Monthly_Salary"],kde=True)
plt.axvline(mean_salary, color = "red", linestyle = "--",label = "Mean")
plt.axvline(median_salary, color = "green", linestyle = "--", label = "median")
plt.title("Montly Salary Distribution")
plt.legend()
plt.show()

#Salary by department
plt.figure(figsize=(8, 5))
ax = sns.boxplot(x="Department", y="Monthly_Salary", data=df)
plt.title("Salary by Department")
plt.xticks(rotation=30)

medians = df.groupby("Department")["Monthly_Salary"].median()

for i, dept in enumerate(medians.index):
    ax.text(
        i,
        medians[dept],
        f"{int(medians[dept])}",
        ha="center",
        va="bottom",
        fontsize=9,
        color="black"
    )
plt.show()

#Attrition count
plt.figure()
ax = sns.countplot(x="Attrition", data= df)
plt.title("Employee Attrition count")
for bar in ax.patches:
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        int(bar.get_height()),
        ha = "center",
        va = "bottom"
    )
plt.show()

#Attrition by Departement
plt.figure()
ax = sns.countplot(x="Department",hue="Attrition", data = df)
plt.xticks(rotation = 30)
plt.title("Attirtion by Department")
for bar in ax.patches:
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        int(bar.get_height()),
         va= "bottom"
    )
plt.show()




