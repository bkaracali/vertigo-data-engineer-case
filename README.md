# Vertigo Games - Data Engineer Case Study

This repository contains a two-part solution for the Vertigo Games Data Engineer case. 

- **Part 1:** A robust Backend API for managing game clans, integrated with Google Cloud.
- **Part 2:** Analytical data modeling using dbt and BigQuery (Work in Progress).

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
