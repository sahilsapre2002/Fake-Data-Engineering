# Fake-Data-Engineering

# 🌐 Cloud Data Warehouse Project – Multi-Store Ecommerce (Google BigQuery)

## 📌 Overview

This project simulates a real-world **cloud data onboarding** workflow using **Google BigQuery**. It is designed to model the backend data infrastructure for a **multi-store ecommerce platform** with a rich and realistic relational schema.

---

## ⚙️ Key Features

- 📊 **Complex Relational Schema** with 7 interlinked tables  
- 🤖 **Synthetic Data Generation** using Faker, Random, UUID, and Google Gemini API  
- ☁️ **Cloud Data Warehouse Setup** using Google BigQuery  
- ⚡ **Automated Table Creation & Data Ingestion** using Python scripts  
- 🔒 **Environment-Based Configuration** using `.env` file  
- ✅ **Production-Ready Structure** to simulate an enterprise data onboarding process

> 🛑 **NOTE**: Only the `users` table is populated due to Google Cloud free tier limitations. All other components (schema, generation, upload) are fully implemented and operational when valid cloud access is available.

---

## 🧠 Project Motivation

In real-world cloud data engineering, onboarding structured data from diverse domains (users, products, orders, inventory, support, etc.) into a centralized warehouse like BigQuery is crucial for analytics, reporting, and business insights.

This project reflects:
- Realistic schema design
- Best practices in data dependency ordering
- Use of AI (Gemini) for enhancing content realism
- Cloud-native ingestion using official SDKs

---

## 🗃️ Database Schema

The project includes **7 normalized, interlinked tables**:

| Table               | Description                                                 |
|---------------------|-------------------------------------------------------------|
| `users`             | Customer profiles with demographics, login history          |
| `products`          | Ecommerce products with attributes, pricing, and metadata   |
| `orders`            | Customer orders with payment and shipping details           |
| `order_items`       | Line items for each order (quantity, discounts, gift wrap)  |
| `warehouses`        | Storage locations with operational metadata                 |
| `inventory_snapshots` | Stock snapshots per product per warehouse                  |
| `support_tickets`   | Customer service issues linked to orders and users          |

Each table contains a diverse set of data types:
- `STRING`, `BOOL`, `DATE`, `TIMESTAMP`, `NUMERIC`, `FLOAT64`, `ENUM-like strings`

> Schema includes realistic column counts (10–15 fields) with nested logic and dependencies.

---

## 🏗️ Technologies Used

| Area             | Tool / Library                            |
|------------------|-------------------------------------------|
| Cloud Warehouse  | [Google BigQuery](https://cloud.google.com/bigquery) |
| SDK/API Access   | `google-cloud-bigquery`, `requests`       |
| Data Generation  | `Faker`, `uuid`, `random`                 |
| AI Integration   | [Gemini API](https://ai.google.dev/)      |
| Language         | Python 3.10+                              |
| Config Management| `dotenv`                                  |

---

## 📂 Repository Structure

```bash
.
├── data_generator.py        # Main script to generate and load all table data
├── gemini_api.py            # Utility for Gemini API calls
├── schema.sql               # BigQuery-compatible schema for all 7 tables
├── .env.example             # Template for credentials and config
├── README.md                # 📄 You are here!
└── requirements.txt         # Python package dependencies

