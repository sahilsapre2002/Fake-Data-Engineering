-- 1. users table
CREATE TABLE dataset_name.users (
    user_id INT64,
    username STRING,
    email STRING,
    country STRING,
    registration_date DATE,
    status STRING,
    is_premium BOOL,
    date_of_birth DATE,
    device_type STRING,
    last_login_time TIMESTAMP
);

-- 2. products table
CREATE TABLE dataset_name.products (
    product_id INT64,
    sku STRING,
    category STRING,
    brand STRING,
    title STRING,
    price NUMERIC,
    weight NUMERIC,
    tags STRING,
    dimensions STRING,
    origin_country STRING,
    available_since DATE,
    rating FLOAT64,
    is_active BOOL
);

-- 3. orders table
CREATE TABLE dataset_name.orders (
    order_id INT64,
    user_id INT64,
    order_date TIMESTAMP,
    shipping_address STRING,
    order_total NUMERIC,
    payment_method STRING,
    discount_code STRING,
    delivery_window STRING,
    order_status STRING
);

-- 4. order_items table
CREATE TABLE dataset_name.order_items (
    item_id INT64,
    order_id INT64,
    product_id INT64,
    quantity INT64,
    unit_price NUMERIC,
    discount_amount NUMERIC,
    fulfillment_center STRING,
    batch_id STRING,
    is_gift_wrapped BOOL
);

-- 5. inventory_snapshots table
CREATE TABLE dataset_name.inventory_snapshots (
    snapshot_id INT64,
    product_id INT64,
    warehouse_id INT64,
    recorded_at TIMESTAMP,
    available_stock INT64,
    reserved_stock INT64,
    safety_stock_threshold INT64
);

-- 6. warehouses table
CREATE TABLE dataset_name.warehouses (
    warehouse_id INT64,
    region STRING,
    manager_name STRING,
    capacity INT64,
    last_audit DATE,
    is_automated BOOL,
    temperature_controlled BOOL,
    timezone STRING,
    operational_hours STRING
);

-- 7. support_tickets table
CREATE TABLE dataset_name.support_tickets (
    ticket_id INT64,
    user_id INT64,
    order_id INT64,
    issue_type STRING,
    description STRING,
    created_at TIMESTAMP,
    resolved_at TIMESTAMP,
    support_agent STRING,
    resolution_status STRING,
    feedback_score INT64
);
