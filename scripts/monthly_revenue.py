import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. LOAD DATA
# ------------
df = pd.read_csv("Telco-Customer-Churn.csv")

# 2. CALCULATE TOTAL REVENUE LOST
total_churned_revenue = df[df['Churn'] == 'Yes']['MonthlyCharges'].sum()
total_active_revenue = df[df['Churn'] == 'No']['MonthlyCharges'].sum()

print(f"\n--- FINANCIAL IMPACT ANALYSIS ---")
print(f"Total Monthly Revenue Lost (Churn): ${total_churned_revenue:,.2f}")
print(f"Total Monthly Revenue RETAINED: ${total_active_revenue:,.2f}")

# 3. DRILL DOWN: Revenue Lost by Fiber Optic Users
fiber_churn_revenue = df[(df['Churn'] == 'Yes') & (df['InternetService'] == 'Fiber optic')]['MonthlyCharges'].sum()
print(f"Revenue Lost spesifically from Fiber Optic Churn: ${fiber_churn_revenue:,.2f}")

# 4.PERCENTAGE IMPACT
loss_percentage = (total_churned_revenue / (total_churned_revenue + total_active_revenue)) * 100
print(f"Revenue Loss Percentage: {loss_percentage:,.2f}%")