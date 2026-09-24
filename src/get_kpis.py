import os
import pandas as pd

# List of possible paths for superstore_clean.csv
possible_paths = [
    "reports/notebooks/data/processed/superstore_clean.csv",
    "data/processed/superstore_clean.csv",
    "superstore_clean.csv"
]

file_path = None
for p in possible_paths:
    if os.path.exists(p):
        file_path = p
        break

if not file_path:
    print("Error: Could not find superstore_clean.csv in expected locations.")
    exit()

print(f"Loading data from: {file_path}")
df = pd.read_csv(file_path)

# Ensure date parsing works properly
if "order_date" in df.columns:
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["quarter"] = df["order_date"].dt.to_period("Q")

print("\n" + "=" * 50)
print("1) TOP PRODUCTS BY PROFIT")
print("=" * 50)
if "product_name" in df.columns and "profit" in df.columns:
    top_products = df.groupby("product_name")["profit"].sum().sort_values(ascending=False)
    top10_profit = top_products.head(10).sum()
    total_profit = df["profit"].sum()
    print(f"Top 10 products profit: ${top10_profit:,.2f}")
    print(f"Total profit: ${total_profit:,.2f}")
    print(f"Top 10 products drive {top10_profit/total_profit*100:.1f}% of total profit")

print("\n" + "=" * 50)
print("2) SHIPPING DELAY BY REGION")
print("=" * 50)
if "shipping_delay_days" in df.columns and "region" in df.columns:
    region_delay = df.groupby("region")["shipping_delay_days"].mean().sort_values(ascending=False)
    print(region_delay)
    overall_avg = df["shipping_delay_days"].mean()
    worst_region = region_delay.index[0]
    pct_diff = (region_delay.iloc[0] - overall_avg) / overall_avg * 100
    print(f"\n{worst_region} region is {pct_diff:.1f}% above the overall average delay")
else:
    print("shipping_delay_days column not found in dataset.")

print("\n" + "=" * 50)
print("3) QUARTERLY SALES TREND")
print("=" * 50)
if "quarter" in df.columns and "sales" in df.columns:
    quarterly_sales = df.groupby("quarter")["sales"].sum()
    print(quarterly_sales)

print("\n" + "=" * 50)
print("4) OVERALL SUMMARY")
print("=" * 50)
if "sales" in df.columns and "order_id" in df.columns:
    print(f"Total revenue: ${df['sales'].sum():,.2f}")
    print(f"Total orders: {df['order_id'].nunique():,}")
    print(f"Total rows analyzed: {len(df):,}")
    print(f"Average order value: ${df['sales'].sum()/df['order_id'].nunique():,.2f}")