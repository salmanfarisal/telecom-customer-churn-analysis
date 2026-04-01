import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Telco-Customer-Churn.csv")

# Convert TotalCharges and drop the hidden empty spaces
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(inplace=True)

# Convert Churn and other important categories to numbers
df['Churn_Numeric'] = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)
df['PaperlessBilling_Numeric'] = df['PaperlessBilling'].apply(lambda x: 1 if x == 'Yes' else 0)

# Select numerical columns
numeric_cols = ['tenure', 'MonthlyCharges', 'TotalCharges', 'Churn_Numeric', 'PaperlessBilling_Numeric']
corr_matrix = df[numeric_cols].corr()

# Visualization
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

plt.title("Key Feature Correlation with Churn")
plt.savefig("Visual Correlation Matrix.png")
plt.show()

print("✅ Correlation Heatmap generated and saved!")