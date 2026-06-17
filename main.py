# main.py
from generate_data import generate_sales_data
from transform import transform_data
from load_to_db import load_data
from analytics import run_analytics

print("=" * 50)
print("🚀 SALES DATA PIPELINE STARTING...")
print("=" * 50)

print("\n📌 Step 1: Generating Data...")
df = generate_sales_data()
df.to_csv("raw_sales_data.csv", index=False)
print("✅ Done!")

print("\n📌 Step 2: Transforming Data...")
df_clean = transform_data()
df_clean.to_csv("cleaned_sales_data.csv", index=False)
print("✅ Done!")

print("\n📌 Step 3: Loading to MySQL...")
load_data()
print("✅ Done!")

print("\n📌 Step 4: Running Analytics...")
run_analytics()

print("\n" + "=" * 50)
print("✅ PIPELINE COMPLETE!")
print("=" * 50)