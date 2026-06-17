# 🚀 Automated Sales Data Pipeline

An end-to-end ETL (Extract, Transform, Load) data pipeline that generates realistic e-commerce sales data, cleans and transforms it using Python & Pandas, loads it into MySQL, and extracts business insights through SQL analytics.

---

## 📌 Project Architecture

```
Raw Data Generation (Faker)
        ↓
Data Transformation (Pandas)
        ↓
MySQL Database (PyMySQL)
        ↓
Business Analytics (SQL Queries)
        ↓
Automated Report (main.py)
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10 |
| Data Generation | Faker, Random |
| Data Transformation | Pandas |
| Database | MySQL 9.7 |
| DB Connector | PyMySQL |
| Version Control | Git & GitHub |

---

## 📁 Project Structure

```
sales-pipeline/
│
├── generate_data.py      # Generate 1000 realistic sales records
├── transform.py          # Clean & transform raw data
├── load_to_db.py         # Load cleaned data into MySQL
├── analytics.py          # Run SQL analytics queries
├── main.py               # Run full pipeline in one command
├── config.py             # Database configuration
├── raw_sales_data.csv    # Generated raw data
├── cleaned_sales_data.csv# Cleaned data
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/KAIF1409/sales-data-pipeline.git
cd sales-data-pipeline
```

### 2. Install Dependencies
```bash
pip install pandas pymysql faker requests
```

### 3. Setup MySQL Database
```sql
CREATE DATABASE sales_pipeline;
```

### 4. Configure Database
Edit `config.py` with your MySQL credentials:
```python
DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "your_password",
    "database": "sales_pipeline"
}
```

### 5. Run the Pipeline
```bash
python main.py
```

---

## 📊 Business Insights Generated

| Insight | Result |
|---|---|
| Total Orders | 1,000 |
| Total Revenue | ₹2.72 Crore+ |
| Top Category | Electronics (47% revenue share) |
| Top City | Hyderabad |
| Avg Order Value | ₹27,169 |
| Return Rate | ~19% |

### Analytics Queries Included:
- ✅ Overall Business Performance (Revenue, Orders, AOV)
- ✅ Revenue by Category
- ✅ Top 5 Cities by Revenue
- ✅ Monthly Sales Trend (Jan–Dec)
- ✅ Return Rate by Category
- ✅ Payment Method Breakdown

---

## 🗄️ Database Schema

```sql
CREATE TABLE sales_orders (
    order_id        VARCHAR(20) PRIMARY KEY,
    customer_name   VARCHAR(100),
    customer_email  VARCHAR(100),
    city            VARCHAR(50),
    category        VARCHAR(50),
    product_name    VARCHAR(100),
    unit_price      DECIMAL(10,2),
    quantity        INT,
    total_amount    DECIMAL(10,2),
    discount_percent DECIMAL(5,2),
    final_amount    DECIMAL(10,2),
    payment_method  VARCHAR(50),
    order_status    VARCHAR(20),
    order_date      DATE,
    order_month     INT,
    order_quarter   INT,
    order_year      INT,
    is_returned     TINYINT,
    is_cancelled    TINYINT
);
```

---

## 💡 Key Concepts Demonstrated

- **ETL Pipeline** — Extract, Transform, Load architecture
- **Data Cleaning** — Duplicate removal, null handling, type casting
- **Feature Engineering** — Derived columns (month, quarter, flags)
- **SQL Analytics** — Aggregations, GROUP BY, ORDER BY, filtering
- **Database Design** — Schema design with appropriate data types
- **Modular Code** — Separation of concerns across files

---

## 🔄 How to Re-run Pipeline

Every time you run `main.py`, it:
1. Generates fresh 1000 sales records
2. Cleans and transforms the data
3. Drops and recreates the MySQL table
4. Loads fresh data
5. Runs all analytics queries

```bash
python main.py
```

---

## 👤 Author

**Mohammed Kaif**  
B.Tech Computer Science — PES University, Bengaluru  
[GitHub](https://github.com/KAIF1409) | [LinkedIn](https://www.linkedin.com/in/mohammed-kaif-714a79242)
