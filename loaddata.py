import os
from sqlalchemy import create_engine

def load_data(df):
    print("Connecting to PostgreSQL container...")
    
    # Pulling credentials dynamically from the Docker environment
    user = os.getenv('POSTGRES_USER', 'postgres')
    password = os.getenv('POSTGRES_PASSWORD', 'dev123')
    host = os.getenv('DB_HOST', 'postgres_db')
    db = os.getenv('POSTGRES_DB', 'crypto_db')

    # Create the SQLAlchemy engine
    engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:5432/{db}')
    
    print("Loading data into 'top_coins' table...")
    # if_exists='replace' will overwrite the table every time the container runs
    df.to_sql('top_coins', engine, if_exists='replace', index=False)
    
    print("Data loaded successfully!")
