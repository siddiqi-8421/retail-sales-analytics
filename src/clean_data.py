import pandas as pd

def clean_superstore_data(input_path, output_path):
    df = pd.read_csv(input_path, encoding="latin1")

    # Standardize column names
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    # Convert date columns
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["ship_date"] = pd.to_datetime(df["ship_date"])

    # Handle missing values
    df = df.dropna(subset=["customer_id", "order_id"])

    # Derived columns useful for analysis
    df["shipping_delay_days"] = (df["ship_date"] - df["order_date"]).dt.days
    df["order_month"] = df["order_date"].dt.to_period("M")

    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved: {df.shape[0]} rows, {df.shape[1]} columns")
    return df

if __name__ == "__main__":
    clean_superstore_data("data/raw/superstore.csv", "data/processed/superstore_clean.csv")