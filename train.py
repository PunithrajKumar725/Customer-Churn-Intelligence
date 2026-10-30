
# ==========================================
# CUSTOMER CHURN INTELLIGENCE SYSTEM
# STEP 1: EXPLORATORY DATA ANALYSIS
# ==========================================

import pandas as pd

# 1. Load the customer dataset
df = pd.read_csv("customer_churn.csv")

print("\nDATASET LOADED SUCCESSFULLY!")

# 2. Display first five records
print("\nFIRST FIVE CUSTOMER RECORDS:")
print(df.head())

# 3. Display dataset shape
print("\nDATASET SHAPE:")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 4. Display column information
print("\nDATASET INFORMATION:")
df.info()

# 5. Check missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())

# 6. Check duplicate records
print("\nDUPLICATE RECORDS:")
print(df.duplicated().sum())

# 7. Analyze churn distribution
print("\nCUSTOMER CHURN DISTRIBUTION:")
print(df["Churn"].value_counts())

# 8. Calculate churn percentage
print("\nCHURN PERCENTAGE:")
print(df["Churn"].value_counts(normalize=True) * 100)

# 9. Statistical summary
print("\nSTATISTICAL SUMMARY:")
print(df.describe())

print("\nEDA COMPLETED SUCCESSFULLY!")
