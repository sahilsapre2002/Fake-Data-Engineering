import os
import uuid
import random
import pandas as pd
from faker import Faker
from dotenv import load_dotenv
from google.cloud import bigquery

# Import Gemini API call function from separate file
from gemini_api import call_gemini

load_dotenv()

PROJECT_ID = os.getenv("GCP_PROJECT_ID")
DATASET_ID = os.getenv("DATASET_ID")

faker = Faker()

# Setup BigQuery client
bq_client = bigquery.Client(project=PROJECT_ID)

def generate_users(n=1050):
    users = []
    for _ in range(n):
        username = faker.user_name()
        user = {
            "user_id": str(uuid.uuid4()),
            "username": username,
            "email": faker.email(),
            "country": faker.country(),
            "registration_date": faker.date_time_this_decade(),
            "status": call_gemini(f"Write a short profile status for a user named {username}") or "Online shopper",
            "is_premium": faker.boolean(),
            "date_of_birth": faker.date_of_birth(minimum_age=18, maximum_age=70),
            "device_type": random.choice(["mobile", "desktop", "tablet"]),
            "last_login_time": faker.date_time_this_year(),
        }
        users.append(user)
    return pd.DataFrame(users)

def generate_products(n=500):
    categories = ["electronics", "fashion", "home", "sports", "beauty"]
    brands = ["Apple", "Samsung", "Nike", "Adidas", "IKEA", "Under Armour", "L'Oréal", "Revlon", "Sony", "H&M"]

    products = []
    for _ in range(n):
        category = random.choice(categories)
        brand = random.choice(brands)
        title = call_gemini(f"Generate an attractive product title for a {category} item by {brand}", 32) or f"{brand} {category} item"
        description = call_gemini(f"Write a short product description for: {title}", 64) or "High-quality product"
        product = {
            "product_id": str(uuid.uuid4()),
            "sku": faker.bothify(text="SKU-#######"),
            "category": category,
            "brand": brand,
            "title": title,
            "description": description,
            "price": round(random.uniform(10, 500), 2),
            "weight": round(random.uniform(0.1, 5.0), 2),
            "tags": ",".join(faker.words(3)),
            "dimensions": f"{random.randint(5,30)}x{random.randint(5,30)}x{random.randint(1,20)} cm",
            "origin_country": faker.country(),
            "available_since": faker.date_this_decade(),
            "rating": round(random.uniform(1.0, 5.0), 1),
            "is_active": faker.boolean(),
        }
        products.append(product)
    return pd.DataFrame(products)

def generate_warehouses(n=30):
    return pd.DataFrame([{
        "warehouse_id": str(uuid.uuid4()),
        "region": random.choice(["North", "South", "East", "West"]),
        "manager_name": faker.name(),
        "capacity": random.randint(5000, 100000),
        "last_audit": faker.date_time_this_year(),
        "is_automated": faker.boolean(),
        "temperature_controlled": faker.boolean(),
        "timezone": random.choice(["UTC", "EST", "PST", "CET"]),
        "operational_hours": "08:00-20:00",
    } for _ in range(n)])

def generate_orders(users_df, n=3000):
    return pd.DataFrame([{
        "order_id": str(uuid.uuid4()),
        "user_id": random.choice(users_df["user_id"]),
        "order_date": faker.date_time_this_year(),
        "shipping_address": faker.address().replace("\n", ", "),
        "order_total": round(random.uniform(20, 1000), 2),
        "payment_method": random.choice(["credit_card", "paypal", "upi", "net_banking"]),
        "discount_code": random.choice([None, "SAVE10", "WELCOME50", "FREESHIP"]),
        "delivery_window": random.choice(["Morning", "Evening", "Afternoon"]),
        "order_status": random.choice(["pending", "shipped", "delivered", "cancelled"]),
    } for _ in range(n)])

def generate_order_items(orders_df, products_df, n=6000):
    return pd.DataFrame([{
        "item_id": str(uuid.uuid4()),
        "order_id": random.choice(orders_df["order_id"]),
        "product_id": random.choice(products_df["product_id"]),
        "quantity": random.randint(1, 5),
        "unit_price": round(random.uniform(10, 500), 2),
        "discount_amount": round(random.uniform(0, 50), 2),
        "fulfillment_center": f"FC-{random.randint(100,999)}",
        "batch_id": faker.bothify("BATCH-#####"),
        "is_gift_wrapped": faker.boolean()
    } for _ in range(n)])

def generate_inventory_snapshots(products_df, warehouses_df, n=1500):
    return pd.DataFrame([{
        "snapshot_id": str(uuid.uuid4()),
        "product_id": random.choice(products_df["product_id"]),
        "warehouse_id": random.choice(warehouses_df["warehouse_id"]),
        "recorded_at": faker.date_time_this_year(),
        "available_stock": random.randint(0, 500),
        "reserved_stock": random.randint(0, 200),
        "safety_stock_threshold": random.randint(10, 100),
    } for _ in range(n)])

def generate_support_tickets(users_df, orders_df, n=800):
    tickets = []
    for _ in range(n):
        issue_type = call_gemini("Generate a short support issue type") or "Delivery issue"
        description = call_gemini(f"Write a support ticket description for issue: {issue_type}", max_tokens=128) or "Order not delivered on time."
        ticket = {
            "ticket_id": str(uuid.uuid4()),
            "user_id": random.choice(users_df["user_id"]),
            "order_id": random.choice(orders_df["order_id"]),
            "issue_type": issue_type,
            "description": description,
            "created_at": faker.date_time_this_year(),
            "resolved_at": faker.date_time_this_year() if random.random() > 0.3 else None,
            "support_agent": faker.first_name(),
            "resolution_status": random.choice(["Resolved", "Pending", "Escalated"]),
            "feedback_score": random.randint(1, 5),
        }
        tickets.append(ticket)
    return pd.DataFrame(tickets)

def upload_to_bigquery(df: pd.DataFrame, table: str):
    table_id = f"{PROJECT_ID}.{DATASET_ID}.{table}"
    job = bq_client.load_table_from_dataframe(df, table_id)
    job.result()
    print(f"✅ Uploaded {len(df)} rows to {table_id}")

if __name__ == "__main__":
    print("Generating users...")
    users_df = generate_users()
    upload_to_bigquery(users_df, "users")

    print("Generating products...")
    products_df = generate_products()
    upload_to_bigquery(products_df, "products")

    print("Generating warehouses...")
    warehouses_df = generate_warehouses()
    upload_to_bigquery(warehouses_df, "warehouses")

    print("Generating orders...")
    orders_df = generate_orders(users_df)
    upload_to_bigquery(orders_df, "orders")

    print("Generating order items...")
    order_items_df = generate_order_items(orders_df, products_df)
    upload_to_bigquery(order_items_df, "order_items")

    print("Generating inventory snapshots...")
    inventory_df = generate_inventory_snapshots(products_df, warehouses_df)
    upload_to_bigquery(inventory_df, "inventory_snapshots")

    print("Generating support tickets...")
    tickets_df = generate_support_tickets(users_df, orders_df)
    upload_to_bigquery(tickets_df, "support_tickets")

    print("🎉 All data successfully generated and uploaded!")
