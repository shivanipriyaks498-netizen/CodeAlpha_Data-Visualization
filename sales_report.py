
import pandas as pd

# Load dataset
df = pd.read_csv("SampleSuperstore.csv", encoding="latin1")

print("=" * 55)
print("          SUPERSTORE SALES ANALYSIS REPORT")
print("=" * 55)

# 1. Dataset overview
print("\n1. DATASET OVERVIEW")
print("Total Records:", len(df))
print("Total Columns:", len(df.columns))

# 2. Overall sales and profit
print("\n2. OVERALL PERFORMANCE")
print("Total Sales: $", round(df["Sales"].sum(), 2))
print("Total Profit: $", round(df["Profit"].sum(), 2))
print("Total Quantity Sold:", df["Quantity"].sum())

# 3. Category performance
print("\n3. SALES BY CATEGORY")
category_sales = df.groupby("Category")["Sales"].sum()
print(category_sales.sort_values(ascending=False))

# 4. Region performance
print("\n4. PROFIT BY REGION")
region_profit = df.groupby("Region")["Profit"].sum()
print(region_profit.sort_values(ascending=False))

# 5. Top 10 sub-categories
print("\n5. TOP 10 SUB-CATEGORIES BY SALES")
top_products = (
    df.groupby("Sub-Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print(top_products)

# 6. Average discount
print("\n6. DISCOUNT ANALYSIS")
print("Average Discount:", round(df["Discount"].mean(), 2))

# 7. Key findings
print("\n7. KEY BUSINESS INSIGHTS")
print("- Technology generates the highest category sales.")
print("- West region generates the highest regional profit.")
print("- Sales and profit vary across product categories.")
print("- Discount patterns should be reviewed alongside profit.")

print("\nSALES REPORT GENERATED SUCCESSFULLY!")
