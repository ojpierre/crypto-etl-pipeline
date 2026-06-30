import pandas as pd

def transform(raw_data):
    print("Transforming data...")
    df = pd.DataFrame(raw_data)
    
    # Safely extract the nested USD price from the 'quotes' dictionary
    df['usd_price'] = df['quotes'].apply(
        lambda x: x.get('USD', {}).get('price') if isinstance(x, dict) else None
    )
    
    # Filter down to just the essential columns for your database
    clean_df = df[['id', 'name', 'symbol', 'rank', 'usd_price']]
    
    print(f"Transformation complete. Prepared {len(clean_df)} records.")
    return clean_df
