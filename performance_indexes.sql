CREATE INDEX idx_sales_product
ON sales(product_id);

CREATE INDEX idx_sales_date
ON sales(sale_date);

CREATE INDEX idx_inventory_product
ON inventory(product_id);

CREATE INDEX idx_supplier_product
ON suppliers(product_id);

CREATE INDEX idx_po_product
ON purchase_orders(product_id);

CREATE INDEX idx_po_supplier
ON purchase_orders(supplier_id);

SHOW INDEX FROM sales;
SHOW INDEX FROM inventory;
SHOW INDEX FROM suppliers;
SHOW INDEX FROM purchase_orders;