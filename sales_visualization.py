
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("SampleSuperstore.csv", encoding="latin1")

# Set visualization style
sns.set_theme(style="whitegrid")

# 1. Sales by Category
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Category", y="Sales", estimator=sum, errorbar=None)
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("sales_by_category.png")
plt.show()

# 2. Profit by Region
region_profit = df.groupby("Region")["Profit"].sum().reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(data=region_profit, x="Region", y="Profit")
plt.title("Total Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.tight_layout()
plt.savefig("profit_by_region.png")
plt.show()

# 3. Sales by Sub-Category
plt.figure(figsize=(12, 6))
sns.barplot(
    data=df,
    x="Sub-Category",
    y="Sales",
    estimator=sum,
    errorbar=None
)
plt.title("Sales by Sub-Category")
plt.xticks(rotation=45)
plt.xlabel("Sub-Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("sales_by_subcategory.png")
plt.show()

# 4. Profit vs Discount
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Discount", y="Profit", alpha=0.5)
plt.title("Relationship Between Discount and Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("profit_vs_discount.png")
plt.show()

print("All visualizations created successfully!")
