# analytics.py
import pymysql
import pandas as pd
from config import DB_CONFIG

def run_analytics():
    conn = pymysql.connect(**DB_CONFIG)
    print("✅ Connected!\n")

    # --- Query 1: Total Revenue & Orders ---
    df1 = pd.read_sql("""
        SELECT 
            COUNT(*) as total_orders,
            ROUND(SUM(final_amount), 2) as total_revenue,
            ROUND(AVG(final_amount), 2) as avg_order_value
        FROM sales_orders
        WHERE order_status = 'Delivered'
    """, conn)
    print("📊 Overall Business Performance:")
    print(df1.to_string(index=False))

    # --- Query 2: Revenue by Category ---
    df2 = pd.read_sql("""
        SELECT 
            category,
            COUNT(*) as total_orders,
            ROUND(SUM(final_amount), 2) as revenue,
            ROUND(AVG(final_amount), 2) as avg_order_value
        FROM sales_orders
        WHERE order_status = 'Delivered'
        GROUP BY category
        ORDER BY revenue DESC
    """, conn)
    print("\n📊 Revenue by Category:")
    print(df2.to_string(index=False))

    # --- Query 3: Top 5 Cities ---
    df3 = pd.read_sql("""
        SELECT 
            city,
            COUNT(*) as orders,
            ROUND(SUM(final_amount), 2) as revenue
        FROM sales_orders
        WHERE order_status = 'Delivered'
        GROUP BY city
        ORDER BY revenue DESC
        LIMIT 5
    """, conn)
    print("\n📊 Top 5 Cities by Revenue:")
    print(df3.to_string(index=False))

    # --- Query 4: Monthly Trend ---
    df4 = pd.read_sql("""
        SELECT 
            order_month,
            COUNT(*) as orders,
            ROUND(SUM(final_amount), 2) as revenue
        FROM sales_orders
        WHERE order_status = 'Delivered'
        GROUP BY order_month
        ORDER BY order_month
    """, conn)
    print("\n📊 Monthly Sales Trend:")
    print(df4.to_string(index=False))

    # --- Query 5: Return Rate by Category ---
    df5 = pd.read_sql("""
        SELECT 
            category,
            COUNT(*) as total_orders,
            SUM(is_returned) as returned,
            ROUND(SUM(is_returned) * 100.0 / COUNT(*), 1) as return_rate_percent
        FROM sales_orders
        GROUP BY category
        ORDER BY return_rate_percent DESC
    """, conn)
    print("\n📊 Return Rate by Category:")
    print(df5.to_string(index=False))

    # --- Query 6: Payment Method Breakdown ---
    df6 = pd.read_sql("""
        SELECT 
            payment_method,
            COUNT(*) as orders,
            ROUND(SUM(final_amount), 2) as revenue
        FROM sales_orders
        GROUP BY payment_method
        ORDER BY orders DESC
    """, conn)
    print("\n📊 Payment Method Breakdown:")
    print(df6.to_string(index=False))

    conn.close()
    print("\n✅ Analytics complete!")

if __name__ == "__main__":
    run_analytics()