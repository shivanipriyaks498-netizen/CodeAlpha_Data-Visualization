
import pandas as pd

# Load sales dataset
df = pd.read_csv("SampleSuperstore.csv", encoding="latin1")

print("=" * 50)
print("       SUPERSTORE SALES DATA ANALYSIS")
print("=" * 50)

# 1. Dataset overview
print("\n1. DATASET OVERVIEW")
print("Total Records:", len(df))
print("Total Columns:", len(df.columns))
print("\nColumn Names:")
print(df.columns.tolist())

# 2. First five records
print("\n2. FIRST FIVE RECORDS")
print(df.head())

# 3. Dataset information
print("\n3. DATA TYPES")
print(df.dtypes)

# 4. Missing values
print("\n4. MISSING VALUES")
print(df.isnull().sum())

# 5. Total sales and profit
print("\n5. SALES AND PROFIT")
print("Total Sales:", round(df["Sales"].sum(), 2))
print("Total Profit:", round(df["Profit"].sum(), 2))

# 6. Sales by category
print("\n6. SALES BY CATEGORY")
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))

# 7. Profit by region
print("\n7. PROFIT BY REGION")
print(df.groupby("Region")["Profit"].sum().sort_values(ascending=False))

print("\nSales analysis completed successfully!")
