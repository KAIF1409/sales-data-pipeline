# generate_data.py
import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()


NUM_RECORDS = 1000

CATEGORIES = ["Electronics", "Clothing", "Food & Beverage", "Books", "Home & Kitchen"]

PRODUCTS = {
    "Electronics": ["Laptop", "Smartphone", "Headphones", "Smartwatch", "Tablet"],
    "Clothing": ["T-Shirt", "Jeans", "Jacket", "Sneakers", "Dress"],
    "Food & Beverage": ["Coffee Beans", "Protein Bar", "Green Tea", "Energy Drink", "Cookies"],
    "Books": ["Python Guide", "Data Science Handbook", "Novel", "Self Help Book", "Cook Book"],
    "Home & Kitchen": ["Blender", "Air Fryer", "Coffee Maker", "Knife Set", "Toaster"]
}

PRICE_RANGE = {
    "Electronics": (5000, 80000),
    "Clothing": (299, 5000),
    "Food & Beverage": (50, 800),
    "Books": (99, 999),
    "Home & Kitchen": (500, 15000)
}

CITIES = ["Mumbai", "Delhi", "Bengaluru", "Chennai", "Hyderabad", 
          "Pune", "Kolkata", "Ahmedabad", "Jaipur", "Surat"]

PAYMENT_METHODS = ["UPI", "Credit Card", "Debit Card", "Net Banking", "Cash on Delivery"]

STATUS = ["Delivered", "Delivered", "Delivered", "Returned", "Cancelled"]



def generate_sales_data():
    records = []

    start_date = datetime(2024, 1, 1)

    for i in range(NUM_RECORDS):
        category = random.choice(CATEGORIES)
        product = random.choice(PRODUCTS[category])
        price = round(random.uniform(*PRICE_RANGE[category]), 2)
        quantity = random.randint(1, 5)
        total_amount = round(price * quantity, 2)
        discount = round(random.uniform(0, 0.30), 2)  # 0% to 30% discount
        final_amount = round(total_amount * (1 - discount), 2)

        order_date = start_date + timedelta(days=random.randint(0, 365))

        record = {
            "order_id": f"ORD{10000 + i}",
            "customer_name": fake.name(),
            "customer_email": fake.email(),
            "city": random.choice(CITIES),
            "category": category,
            "product_name": product,
            "unit_price": price,
            "quantity": quantity,
            "total_amount": total_amount,
            "discount_percent": discount,
            "final_amount": final_amount,
            "payment_method": random.choice(PAYMENT_METHODS),
            "order_status": random.choice(STATUS),
            "order_date": order_date.strftime("%Y-%m-%d")
        }
        records.append(record)

    df = pd.DataFrame(records)
    return df


if __name__ == "__main__":
    df = generate_sales_data()
    print(f" {len(df)} records generated!")
    print("\nSample Data:")
    print(df.head())
    print("\nColumns:", list(df.columns))
    
   
    df.to_csv("raw_sales_data.csv", index=False)
    print("\n raw_sales_data.csv saved!")