import pandas as pd

def load_data(sheet_url):
    try:
        df = pd.read_csv(sheet_url)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
