USE supply_chain_dw;
INSERT INTO dim_product (product_id)
SELECT DISTINCT product_id
FROM supply_chain_db.sales;

INSERT INTO dim_store (store_id)
SELECT DISTINCT store_id
FROM supply_chain_db.sales;

INSERT INTO dim_warehouse (warehouse_id)
SELECT DISTINCT warehouse_id
FROM supply_chain_db.inventory;

INSERT INTO dim_supplier
(
    supplier_id,
    supplier_name,
    lead_time_days,
    order_frequency
)
SELECT
    supplier_id,
    supplier_name,
    lead_time_days,
    order_frequency
FROM supply_chain_db.suppliers;

USE supply_chain_dw;

INSERT INTO dim_date
(
    date_key,
    full_date,
    year,
    quarter_no,
    month_no,
    day_no
)
SELECT DISTINCT
    DATE_FORMAT(sale_date,'%Y%m%d') AS date_key,
    sale_date,
    YEAR(sale_date),
    QUARTER(sale_date),
    MONTH(sale_date),
    DAY(sale_date)
FROM supply_chain_db.sales;