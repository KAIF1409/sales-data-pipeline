# transform.py
import pandas as pd

def transform_data(filepath="raw_sales_data.csv"):
    print(" Loading raw data...")
    df = pd.read_csv(filepath)
    print(f"   Shape: {df.shape}")

    # --- Step 1: Duplicates hatao ---
    before = len(df)
    df = df.drop_duplicates(subset=["order_id"])
    after = len(df)
    print(f"\n Step 1 - Duplicates removed: {before - after}")

    # --- Step 2: Null values check karo ---
    print(f"\n Step 2 - Null values:\n{df.isnull().sum()}")
    df = df.dropna()  # null rows hatao

    # --- Step 3: Data types fix karo ---
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["unit_price"] = df["unit_price"].astype(float)
    df["final_amount"] = df["final_amount"].astype(float)
    df["quantity"] = df["quantity"].astype(int)
    print(f"\n Step 3 - Data types fixed")

    # --- Step 4: Naye columns add karo ---
    df["order_month"] = df["order_date"].dt.month
    df["order_quarter"] = df["order_date"].dt.quarter
    df["order_year"] = df["order_date"].dt.year
    df["is_returned"] = df["order_status"].apply(
        lambda x: 1 if x == "Returned" else 0
    )
    df["is_cancelled"] = df["order_status"].apply(
        lambda x: 1 if x == "Cancelled" else 0
    )
    print(f"\n Step 4 - New columns added: order_month, order_quarter, is_returned, is_cancelled")

    # --- Step 5: Business Insights ---
    print("\n Quick Insights:")
    print(f"   Total Revenue: ₹{df['final_amount'].sum():,.2f}")
    print(f"   Total Orders: {len(df)}")
    print(f"   Avg Order Value: ₹{df['final_amount'].mean():,.2f}")
    print(f"   Return Rate: {df['is_returned'].mean()*100:.1f}%")
    print(f"\n   Top Category:\n{df.groupby('category')['final_amount'].sum().sort_values(ascending=False)}")

    print(f"\n Transformation complete! Shape: {df.shape}")
    return df


if __name__ == "__main__":
    df = transform_data()
    df.to_csv("cleaned_sales_data.csv", index=False)
    print(" cleaned_sales_data.csv saved!")