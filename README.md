# Vertigo Games - Data Engineer Case Study

This repository contains a two-part solution for the Vertigo Games Data Engineer case. 

- **Part 1:** A robust Backend API for managing game clans, integrated with Google Cloud.
- **Part 2:** Analytical data modeling using dbt and BigQuery.

---

## Part 1: Clan Management API

A lightweight REST API built with **FastAPI**, designed to manage game clans with persistence on **Google Cloud SQL**.

### 🌐 Live Deployment
The application is fully containerized and deployed on Google Cloud.
- **API Base URL:** [https://vertigo-case-551504531238.europe-central2.run.app](https://vertigo-case-551504531238.europe-central2.run.app)
- **Interactive API Docs (Swagger):** [https://vertigo-case-551504531238.europe-central2.run.app/docs](https://vertigo-case-551504531238.europe-central2.run.app/docs)

### 🛠 Tech Stack
- **Framework:** FastAPI (Python)
- **Database:** PostgreSQL (Google Cloud SQL)
- **Infrastructure:** Google Cloud Run (Serverless)
- **Containerization:** Docker & Docker Compose
- **ORM:** SQLAlchemy with Pydantic for data validation.

### 📋 Key Features & Assumptions
- **UUID & Timestamps:** Every clan is assigned a unique UUID4. Timestamps are strictly handled in **UTC** to ensure global consistency.
- **Data Integrity:** During the initial data seeding (`clan_sample_data.csv`), I implemented a **data cleaning layer**. 
    - *Handling Missing Data:* Rows with null or empty clan names/regions were filtered out to maintain database constraints.
    - *Duplicate Prevention:* Ensured unique naming where applicable.
- **Search Functionality:** Implemented a case-insensitive search that finds clans containing the query string (minimum 3 characters required).

### 💻 Local Development
To run the project locally with a PostgreSQL instance:
1. Navigate to the backend folder: `cd clan-backend`
2. Start the services:
   ```bash
   docker-compose up --build

## Part 2: Analytical Data Modeling (dbt & BigQuery)

In this section, I transformed raw user-level activity logs into a structured analytical layer using **dbt** to drive business insights.

### 🛠 Tech Stack
- **Data Warehouse:** Google BigQuery
- **Transformation Tool:** dbt (Data Build Tool)
- **BI Tool:** Looker Studio

### 📋 Key Features & Modeling Logic
- **Single Source of Truth:** Created a centralized model named `daily_metrics` that aggregates granular user data into daily summaries by country and platform.
- **Advanced Business Metrics:**
    - **ARPDAU:** Calculated Average Revenue Per Daily Active User by merging IAP and Ad revenue streams.
    - **Gameplay Balance:** Developed **Win/Defeat Ratios** to provide signals for game difficulty and player retention.
    - **Technical Stability:** Implemented **Server Error per DAU** to monitor system health in real-time.
- **Data Quality & Robustness:**
    - **Data Cleaning:** Implemented a transformation layer to handle `NULL` or empty `country` values, remapping them to `Unknown`.
    - **Error Prevention:** Utilized `SAFE_DIVIDE` across all ratio calculations to ensure model stability against division-by-zero errors.
    - **Source Management:** Used dbt **Sources** and **Ref** macros to ensure clean data lineage and modularity.

### 💻 Local dbt Execution
To run the analytical models and view documentation:
1. Navigate to the dbt directory: `cd analytics-dbt/analytics_models`
2. Build the models:
   ```bash
   dbt run
3. Generate and view the interactive lineage graph:
   ```bash
   dbt docs generate
   dbt docs serve 

### 📊 Visualization
The final transformation layer is visualized through a **Looker Studio Dashboard**.

🔗 **[Click Here to View the Live Dashboard](https://lookerstudio.google.com/reporting/aabebc80-a2da-44e8-aa4f-01d3cdfb37f5)**

The dashboard focused on:
- **Monetization Trends:** Daily revenue tracking vs. DAU growth.
- **Platform Performance:** Comparison of stability and engagement between iOS and Android.
- **Global Reach:** Revenue and user distribution by country.

### 🚀 Getting Started & Installation
**Prerequisites**
- **Python 3.9+** 
- **Docker & Docker Compose** 
- **Google Cloud SDK (gcloud) (For BigQuery access)** 
- **Git** 

1. Clone the Repository
    ```bash
    git clone https://github.com/bkaracali/vertigo-data-engineer-case.git
    cd vertigo-data-engineer-case
2. Setup & Run Part 1 (Backend API)
    ```bash
    cd clan-backend
    # Install dependencies locally if not using Docker:
    # pip install -r requirements.txt
    docker-compose up --build
3. Setup & Run Part 2 (dbt)
    ```bash
    pip install dbt-bigquery
4. Navigate to the project and run:
    ```bash
    cd analytics-dbt/analytics_models
    dbt deps
    dbt run
    
