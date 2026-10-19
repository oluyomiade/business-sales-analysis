import pandas as pd
import matplotlib.pyplot as plt

# Load the sales dataset
df = pd.read_csv(
    "data/superstore.csv",
    encoding="latin1"
)


# Convert date columns to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Check the updated data types
print("\nUPDATED DATE TYPES")
print(df[["Order Date", "Ship Date"]].dtypes)

# Check the order date range
print("\nORDER DATE RANGE")
print("Earliest order:", df["Order Date"].min())
print("Latest order:", df["Order Date"].max())

# Calculate shipping days
df["Shipping Days"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days

# Display shipping information
print("\nSHIPPING DAYS")
print(df[["Order Date", "Ship Date", "Shipping Days"]].head())

# Calculate average shipping time
print("\nAVERAGE SHIPPING DAYS")
print(round(df["Shipping Days"].mean(), 2))

# Calculate total sales and profit
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

print("\nTOTAL SALES")
print(round(total_sales, 2))

print("\nTOTAL PROFIT")
print(round(total_profit, 2))

# Count unique orders
total_orders = df["Order ID"].nunique()

print("\nTOTAL ORDERS")
print(total_orders)

# Calculate profit margin
profit_margin = (total_profit / total_sales) * 100

print("\nPROFIT MARGIN")
print(round(profit_margin, 2), "%")

# Analyse sales and profit by category
category_performance = df.groupby("Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
)

# Calculate profit margin by category
category_performance["Profit_Margin"] = (
    category_performance["Total_Profit"]
    / category_performance["Total_Sales"]
) * 100

print("\nPROFIT BY CATEGORY")
print(category_performance.round(2))

# Analyse performance by sub-category
subcategory_performance = df.groupby("Sub-Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
)

# Calculate profit margin
subcategory_performance["Profit_Margin"] = (
    subcategory_performance["Total_Profit"]
    / subcategory_performance["Total_Sales"]
) * 100

# Sort by profit, from lowest to highest
subcategory_performance = subcategory_performance.sort_values(
    by="Total_Profit"
)

print("\nSUB-CATEGORY PERFORMANCE")
print(subcategory_performance.round(2))

# Analyse average discounts by sub-category
discount_analysis = df.groupby("Sub-Category").agg(
    Average_Discount=("Discount", "mean"),
    Total_Profit=("Profit", "sum")
)

# Sort by average discount, highest first
discount_analysis = discount_analysis.sort_values(
    by="Average_Discount",
    ascending=False
)

print("\nDISCOUNT ANALYSIS")
print(discount_analysis.round(3))

# Compare discount levels with average profit per sale
discount_profit = df.groupby("Discount").agg(
    Number_of_Sales=("Profit", "count"),
    Average_Profit=("Profit", "mean"),
    Total_Profit=("Profit", "sum")
)

print("\nPROFIT BY DISCOUNT LEVEL")
print(discount_profit.round(2))

# Plot average profit by discount level
plt.figure(figsize=(10, 6))

plt.plot(
    discount_profit.index * 100,
    discount_profit["Average_Profit"],
    marker="o"
)

plt.axhline(y=0, linestyle="--")

plt.title("Average Profit by Discount Level")
plt.xlabel("Discount (%)")
plt.ylabel("Average Profit")
plt.grid(True)

plt.tight_layout()
plt.savefig("charts/average_profit_by_discount.png")
plt.show()


# Analyse sales and profit by region
region_performance = df.groupby("Region").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Number_of_Orders=("Order ID", "nunique")
)

# Sort regions by total sales, highest first
region_performance = region_performance.sort_values(
    by="Total_Sales",
    ascending=False
)

# Calculate profit margin by region
region_performance["Profit_Margin"] = (
    region_performance["Total_Profit"]
    / region_performance["Total_Sales"]
) * 100

print("\nREGIONAL PERFORMANCE")
print(
    region_performance[
        ["Total_Sales", "Total_Profit", "Profit_Margin"]
    ].round(2)
)


# Plot total profit by region
plt.figure(figsize=(8, 5))

plt.bar(
    region_performance.index,
    region_performance["Total_Profit"]
)

plt.title("Total Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")

plt.tight_layout()
plt.savefig("charts/profit_by_region.png")
plt.show()

# Analyse monthly sales
df["Order Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = df.groupby("Order Month")["Sales"].sum()

print("\nMONTHLY SALES")
print(monthly_sales)

# Plot monthly sales over time
plt.figure(figsize=(12, 6))

plt.plot(
    monthly_sales.index.astype(str),
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()
plt.savefig("charts/monthly_sales_trend.png")
plt.show()

# Analyse monthly profit
monthly_profit = df.groupby("Order Month")["Profit"].sum()

print("\nMONTHLY PROFIT")
print(monthly_profit)

# Display only months with negative total profit
print("\nMONTHS WITH NEGATIVE PROFIT")
print(monthly_profit[monthly_profit < 0])

# Plot monthly profit over time
plt.figure(figsize=(12, 6))

plt.plot(
    monthly_profit.index.astype(str),
    monthly_profit.values,
    marker="o"
)

plt.axhline(y=0, linestyle="--")

plt.title("Monthly Profit Trend")
plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()
plt.savefig("charts/monthly_profit_trend.png")
plt.show()

# Analyse yearly sales and profit
df["Order Year"] = df["Order Date"].dt.year

yearly_performance = df.groupby("Order Year").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
)

print("\nYEARLY PERFORMANCE")
print(yearly_performance.round(2))

# Calculate yearly profit margin
yearly_performance["Profit_Margin"] = (
    yearly_performance["Total_Profit"] /
    yearly_performance["Total_Sales"]
) * 100

print("\nYEARLY PROFIT MARGINS")
print(yearly_performance.round(2))

# Plot yearly profit margin
plt.figure(figsize=(8, 5))

plt.plot(
    yearly_performance.index,
    yearly_performance["Profit_Margin"],
    marker="o"
)

plt.title("Yearly Profit Margin Trend")
plt.xlabel("Year")
plt.ylabel("Profit Margin (%)")
plt.xticks(yearly_performance.index)
plt.grid(True)
plt.tight_layout()
plt.savefig("charts/yearly_profit_margin.png")
plt.show()

# Analyse performance by product
product_performance = df.groupby("Product Name").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
)

# Sort products by total sales
product_performance = product_performance.sort_values(
    by="Total_Sales",
    ascending=False
)

print("\nTOP 10 PRODUCTS BY SALES")
print(product_performance.head(10).round(2))

# Top 10 products by profit
top_products_by_profit = product_performance.sort_values(
    by="Total_Profit",
    ascending=False
)

print("\nTOP 10 PRODUCTS BY PROFIT")
print(top_products_by_profit.head(10).round(2))

