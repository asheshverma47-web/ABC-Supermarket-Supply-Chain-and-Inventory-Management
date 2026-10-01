USE supply_chain_db;

CREATE TABLE sales (
    sale_id VARCHAR(20),
    product_id VARCHAR(10),
    store_id VARCHAR(10),
    sale_date DATE,
    quantity_sold INT,
    revenue DECIMAL(12,2)
);

CREATE TABLE inventory (
    product_id VARCHAR(10),
    store_id VARCHAR(10),
    warehouse_id VARCHAR(10),
    stock_level INT,
    reorder_level INT,
    last_updated DATE
);

CREATE TABLE suppliers (
    supplier_id VARCHAR(10),
    supplier_name VARCHAR(100),
    product_id VARCHAR(10),
    lead_time_days INT,
    order_frequency VARCHAR(20)
);

CREATE TABLE purchase_orders (
    order_id VARCHAR(20),
    product_id VARCHAR(10),
    supplier_id VARCHAR(10),
    order_date DATE,
    quantity INT,
    arrival_date DATE
);