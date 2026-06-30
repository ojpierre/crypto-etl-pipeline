# How I Built My First Crypto ETL Pipeline 🚀

If you had told me a few months ago that I'd be building automated data pipelines, I probably would have stared at you blankly. But this weekend, I rolled up my sleeves and built a fully functional ETL (Extract, Transform, Load) pipeline for cryptocurrency data, and honestly? It was incredibly fun.

Here is a quick breakdown of what I built, how it works, and why ETL is such a superpower.

## What is ETL anyway?

ETL stands for Extract, Transform, and Load. It’s the bread and butter of data engineering. 
- **Extract:** Go get the data from somewhere (like an API).
- **Transform:** Clean it up so it actually makes sense.
- **Load:** Save it somewhere safe (like a database) so you can analyze it later.

## My Project: Tracking the Top Cryptos 🪙

For this project, I wanted to track the prices of top cryptocurrencies like Bitcoin, Ethereum, and Solana. 

### Step 1: The Extract Phase
I used the free CoinPaprika API to fetch live data. I wrote a Python script using the `requests` library to ask the API, "Hey, what are the current stats for Bitcoin?" 
I made sure to add a small delay between requests so I wouldn't overload their servers—good manners are important in coding, too!

### Step 2: The Transform Phase
APIs usually return a massive wall of JSON data. While computers love JSON, it’s a nightmare to read. 
Using the `pandas` library, I grabbed only the exact data I cared about: the coin's ID, Name, Symbol, Rank, and its live USD Price. I threw away all the messy extra details and organized it into a neat, clean table.

### Step 3: The Load Phase
Now that I had clean data, I needed a place to store it. I spun up a PostgreSQL database using Docker. With the help of `SQLAlchemy`, I connected my Python script to the database and automatically inserted my clean crypto data into a table called `top_coins`. 

### Tying it all together with Docker 🐳
To make sure my code would work on *any* computer, I containerized the whole project using Docker Compose. With a single `docker-compose up` command, it spins up the database, waits a few seconds for it to get ready, and then perfectly executes my Extract, Transform, and Load scripts.

## What I Learned
Building this pipeline taught me that data engineering isn't just about writing code; it's about making data *useful*. 

It’s incredibly satisfying to watch a script pull chaotic, raw data from the internet, clean it up, and neatly store it in a database without me having to lift a finger. On to the next project! 💻
