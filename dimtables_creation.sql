CREATE TABLE dim_product (
    product_key INT AUTO_INCREMENT PRIMARY KEY,
    product_id VARCHAR(10)
);

CREATE TABLE dim_store (
    store_key INT AUTO_INCREMENT PRIMARY KEY,
    store_id VARCHAR(10)
);

CREATE TABLE dim_supplier (
    supplier_key INT AUTO_INCREMENT PRIMARY KEY,
    supplier_id VARCHAR(10),
    supplier_name VARCHAR(100),
    lead_time_days INT,
    order_frequency VARCHAR(20)
);

CREATE TABLE dim_warehouse (
    warehouse_key INT AUTO_INCREMENT PRIMARY KEY,
    warehouse_id VARCHAR(10)
);

CREATE TABLE dim_date (
    date_key INT PRIMARY KEY,
    full_date DATE,
    year INT,
    quarter_no INT,
    month_no INT,
    day_no INT
);
