import time
from extract import extract
from transform import transform
from loaddata import load_data

if __name__ == "__main__":
    print("Waiting 10 seconds for PostgreSQL to initialize...")
    time.sleep(10)
    
    # 1. Extract
    raw_data = extract()
    
    if raw_data:
        # 2. Transform
        clean_df = transform(raw_data)
        
        # 3. Load
        load_data(clean_df)
        print("ETL Pipeline finished successfully.")
    else:
        print("No data extracted. Exiting pipeline.")
