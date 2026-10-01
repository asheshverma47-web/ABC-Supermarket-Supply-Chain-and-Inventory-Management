CREATE TABLE fact_sales (
    sales_key INT AUTO_INCREMENT PRIMARY KEY,
    date_key INT,
    product_key INT,
    store_key INT,
    quantity_sold INT,
    revenue DECIMAL(12,2)
);

CREATE TABLE fact_inventory (
    inventory_key INT AUTO_INCREMENT PRIMARY KEY,
    date_key INT,
    product_key INT,
    store_key INT,
    warehouse_key INT,
    stock_level INT,
    reorder_level INT
);

