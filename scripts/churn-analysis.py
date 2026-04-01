import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. LOAD DATA
# ------------
df = pd.read_csv("Telco-Customer-Churn.csv")

# 2. DATA CLEANING
# ----------------
df.info()

# "TotalCharges"  is read as an object, convert it to float
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(inplace=True)

df.info()

# 3. INITIAL INSIGHT: How many people left?
# -----------------------------------------
print("Churn Distribution:")
print(df['Churn'].value_counts(normalize=True) * 100)

# 4. VISUALIZATION: Churn by Contract Type
# ----------------------------------------
plt.figure(figsize=(10, 6))
sns.countplot(x='Contract', hue='Churn', data=df, palette='magma')
plt.title("Churn Rate by Contract Type")
plt.savefig("Churn Rate by Contract Type.png")
plt.show()