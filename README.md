# Crypto ETL Project Overview

This repository contains a containerized ETL (Extract, Transform, Load) pipeline that fetches live cryptocurrency data, processes it, and loads it into a PostgreSQL database.

## 📂 File Structure

Here is a breakdown of what each file in this project does:

### 1. `extract.py`
This script handles the **Extract** phase. It connects to the public CoinPaprika API and fetches live ticker data for 5 major cryptocurrencies (Bitcoin, Ethereum, Tether, Binance Coin, and Solana). It includes error handling and timeouts to ensure stability.

### 2. `transform.py`
This script handles the **Transform** phase. It takes the raw JSON data extracted from the API and converts it into a `pandas` DataFrame. It filters the data to only include essential columns (`id`, `name`, `symbol`, `rank`, `usd_price`) and extracts the nested USD price for easy querying.

### 3. `loaddata.py`
This script handles the **Load** phase. It connects to a PostgreSQL database using SQLAlchemy and `psycopg2`. It takes the cleaned DataFrame and uploads it to a database table named `top_coins`.

### 4. `main.py`
This is the **Orchestrator**. It runs the Extract, Transform, and Load functions in the correct sequence. It also includes a brief 10-second sleep at the start to ensure the PostgreSQL database has fully initialized before attempting to connect.

### 5. `requirements.txt`
Lists all the Python dependencies required to run the scripts (e.g., `requests`, `pandas`, `SQLAlchemy`, `psycopg2-binary`).

### 6. `Dockerfile`
Contains the instructions to build the Python environment. It installs the required dependencies and sets up the container to run `main.py`.

### 7. `docker-compose.yml`
The configuration file that manages the multi-container Docker application. It sets up two services:
- **postgres_db**: A PostgreSQL database container.
- **python_etl**: The Python container that runs the ETL pipeline, configured to depend on the database.

## 🚀 How to Run
To run this pipeline, simply ensure Docker is installed and run:
```bash
docker-compose up --build
```
This will automatically spin up the database, extract the live data, transform it, and load it into PostgreSQL!
