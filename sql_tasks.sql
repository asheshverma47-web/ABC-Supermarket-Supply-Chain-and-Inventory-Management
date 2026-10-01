--Task 1 - Identify Fast-Moving and Slow-Moving Products

SELECT
    product_id,
    SUM(quantity_sold) AS total_quantity_sold,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY product_id
ORDER BY total_quantity_sold DESC;


--Create Fast-Moving & Slow-Moving Product Report

SELECT
    product_id,
    SUM(quantity_sold) AS total_quantity_sold,
    CASE
        WHEN SUM(quantity_sold) >= 260000 THEN 'Fast Moving'
        WHEN SUM(quantity_sold) <= 250000 THEN 'Slow Moving'
        ELSE 'Medium Moving'
    END AS product_category
FROM sales
GROUP BY product_id
ORDER BY total_quantity_sold DESC;


--Products Below Reorder Level (Restocking Analysis)

SELECT
    product_id,
    store_id,
    warehouse_id,
    stock_level,
    reorder_level,
    (reorder_level - stock_level) AS shortage_qty
FROM inventory
WHERE stock_level < reorder_level
ORDER BY shortage_qty DESC;


--Supplier Lead Time Analysis

SELECT
    supplier_id,
    supplier_name,
    product_id,
    lead_time_days,
    order_frequency
FROM suppliers
ORDER BY lead_time_days DESC;

--the highest lead time:

SELECT
    supplier_id,
    supplier_name,
    product_id,
    lead_time_days
FROM suppliers
WHERE lead_time_days >= 8
ORDER BY lead_time_days DESC;
