# load_to_db.py
import pandas as pd
import pymysql  # mysql.connector ki jagah yeh
from config import DB_CONFIG

def load_data(filepath="cleaned_sales_data.csv"):
    print("📥 Loading cleaned data...")
    df = pd.read_csv(filepath)
    print(f"   Rows: {len(df)}")

    print("🔌 Connecting to MySQL...")
    conn = pymysql.connect(**DB_CONFIG)
    cursor = conn.cursor()
    print("✅ Connected!")

    print("🔧 Creating table...")
    cursor.execute("DROP TABLE IF EXISTS sales_orders")
    cursor.execute("""
        CREATE TABLE sales_orders (
            order_id VARCHAR(20) PRIMARY KEY,
            customer_name VARCHAR(100),
            customer_email VARCHAR(100),
            city VARCHAR(50),
            category VARCHAR(50),
            product_name VARCHAR(100),
            unit_price DECIMAL(10,2),
            quantity INT,
            total_amount DECIMAL(10,2),
            discount_percent DECIMAL(5,2),
            final_amount DECIMAL(10,2),
            payment_method VARCHAR(50),
            order_status VARCHAR(20),
            order_date DATE,
            order_month INT,
            order_quarter INT,
            order_year INT,
            is_returned TINYINT,
            is_cancelled TINYINT
        )
    """)
    print("✅ Table created!")

    print("📤 Inserting rows...")
    inserted = 0
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO sales_orders VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
        """, tuple(row))
        inserted += 1
        if inserted % 100 == 0:
            print(f"   {inserted} rows done...")

    conn.commit()
    print(f"✅ {inserted} rows inserted!")

    cursor.close()
    conn.close()
    print("🔌 Connection closed.")

if __name__ == "__main__":
    load_data()