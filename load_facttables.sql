USE supply_chain_dw;

INSERT INTO fact_sales
(
    date_key,
    product_key,
    store_key,
    quantity_sold,
    revenue
)
SELECT
    d.date_key,
    p.product_key,
    s.store_key,
    src.quantity_sold,
    src.revenue
FROM supply_chain_db.sales src
JOIN dim_product p
    ON src.product_id = p.product_id
JOIN dim_store s
    ON src.store_id = s.store_id
JOIN dim_date d
    ON src.sale_date = d.full_date;

USE supply_chain_dw;

INSERT INTO fact_inventory
(
    date_key,
    product_key,
    store_key,
    warehouse_key,
    stock_level,
    reorder_level
)
SELECT
    d.date_key,
    p.product_key,
    s.store_key,
    w.warehouse_key,
    i.stock_level,
    i.reorder_level
FROM supply_chain_db.inventory i
JOIN dim_product p
    ON i.product_id = p.product_id
JOIN dim_store s
    ON i.store_id = s.store_id
JOIN dim_warehouse w
    ON i.warehouse_id = w.warehouse_id
JOIN dim_date d
    ON i.last_updated = d.full_date;