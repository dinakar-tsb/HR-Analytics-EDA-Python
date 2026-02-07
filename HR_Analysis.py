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
sns.countplot(x = "Department",data = df)
plt.title("Employee Count by Department")
plt.xticks(rotation = 30)
plt.show()

# Salary distribution
plt.figure()
sns.histplot(df["Monthly_Salary"],kde=True)
plt.title("Montly Salary Distribution")
plt.show()

#Salary by department
plt.figure()
sns.boxplot(x="Department", y="Monthly_Salary", data = df)
plt.xticks(rotation =30)
plt.title("Salary by Department")
plt.show()

#Attrition count
plt.figure()
sns.countplot(x="Attrition", data= df)
plt.title("Employee Attrition count")
plt.show()

#Attrition by Departement
plt.figure()
sns.countplot(x="Department",hue="Attrition", data = df)
plt.xticks(rotation = 30)
plt.title("Attirtion by Department")
plt.show()

dept_avg_salary = df.groupby("Department")["Monthly_Salary"].mean()
print(dept_avg_salary)


