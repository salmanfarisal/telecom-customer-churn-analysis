import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. LOAD DATA
# ------------
df = pd.read_csv("Telco-Customer-Churn.csv")

# Convert Churn to 1 and 0 for calculation
df['Churn_Numeric'] = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)

# 2. ANALYSIS
# -----------
factors = ['Contract', 'InternetService', 'PaymentMethod']

print("--- CHURN RATE ANALYSIS ---")
for factor in factors:
    analysis = df.groupby(factor)['Churn_Numeric']. mean().sort_values(ascending=False)
    print(f"\nKey Driver: {factor}")
    print(analysis * 100)

# 3. VISUALIZATION
# ----------------
plt.figure(figsize=(12, 5))

# Plotting Contract Type vs Churn
plt.subplot(1, 2, 1)
sns.barplot(x='Contract', y='Churn_Numeric', data=df, palette='viridis')
plt.xlabel("Contract Type")
plt.ylabel("Churn Risk")
plt.title("Churn Risk by Contract")

# Plotting Internet Service vs Churn
plt.subplot(1, 2, 2)
sns.barplot(x='InternetService', y='Churn_Numeric', data=df, palette='rocket')
plt.title("Churn Risk by Internet Type")
plt.xlabel("Internet Type")
plt.ylabel("Churn Risk")

plt.tight_layout()
plt.savefig("Churn Rate Analysis.png")
plt.show()