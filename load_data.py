import pandas as pd
from sqlalchemy import create_engine

# Change password if required
engine = create_engine(
    "mysql+pymysql://root:ashesh2708@localhost/supply_chain_db"
)

# Read CSV files
sales = pd.read_csv("sales_data-2.csv")
inventory = pd.read_csv("inventory_data.csv")
suppliers = pd.read_csv("suppliers_data.csv")
purchase_orders = pd.read_csv("purchase_orders_data.csv")

# Rename Sales columns
sales.columns = [
    "sale_id",
    "product_id",
    "store_id",
    "sale_date",
    "quantity_sold",
    "revenue"
]

# Rename Inventory columns
inventory.columns = [
    "product_id",
    "store_id",
    "warehouse_id",
    "stock_level",
    "reorder_level",
    "last_updated"
]

# Rename Supplier columns
suppliers.columns = [
    "supplier_id",
    "supplier_name",
    "product_id",
    "lead_time_days",
    "order_frequency"
]

# Rename Purchase Orders columns
purchase_orders.columns = [
    "order_id",
    "product_id",
    "supplier_id",
    "order_date",
    "quantity",
    "arrival_date"
]

# Load into MySQL
sales.to_sql("sales", engine, if_exists="append", index=False)
inventory.to_sql("inventory", engine, if_exists="append", index=False)
suppliers.to_sql("suppliers", engine, if_exists="append", index=False)
purchase_orders.to_sql("purchase_orders", engine, if_exists="append", index=False)

print("Data Loaded Successfully!")
