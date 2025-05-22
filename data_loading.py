import os
import pandas as pd
import sqlalchemy as sa
from sqlalchemy import MetaData, Table, Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Configuration
CSV_DIRECTORY = "./Data"  # Directory containing your CSV files
MAIN_DB_URI = "sqlite:///main_database.db"  # Change to your preferred database URI

def create_connection(db_uri):
    """Create a database engine connection"""
    engine = create_engine(db_uri)
    return engine

def load_csv_to_dataframe(csv_path):
    """Load a CSV file into a pandas DataFrame"""
    try:
        df = pd.read_csv(csv_path)
        return df
    except Exception as e:
        print(f"Error loading CSV {csv_path}: {e}")
        return None


def record_metadata(session, metadata_class, data):
    """Record metadata in the metadata database"""
    new_record = metadata_class(**data)
    session.add(new_record)
    session.commit()

def main():
    # Create database connections
    main_engine = create_connection(MAIN_DB_URI)
    
    # Get list of CSV files
    # csv_files = [f for f in os.listdir(CSV_DIRECTORY) if f.endswith('.csv')]
    
    if False:
        csv_path = os.path.join(CSV_DIRECTORY, "Value_of_Production_E_All_Data/Value_of_Production_E_All_Data_Processed.csv")
        
        # Load CSV to DataFrame
        df = load_csv_to_dataframe(csv_path)
        
        # Generate table name from file name (remove .csv and convert to lowercase)
        table_name = "Value_of_Production_E_All_Data"
        
        # Save DataFrame to main database
        df.to_sql(table_name, main_engine, if_exists='replace', index=False)
        print(f"Loaded {table_name} into table '{table_name}'")

    if False:
        csv_path = os.path.join(CSV_DIRECTORY, "Production_Crops_Livestock_E_All_Data/Production_Crops_Livestock_E_All_Data_Processed.csv")
        
        # Load CSV to DataFrame
        df = load_csv_to_dataframe(csv_path)
        
        # Generate table name from file name (remove .csv and convert to lowercase)
        table_name = "Production_Crops_Livestock"
        
        # Save DataFrame to main database
        df.to_sql(table_name, main_engine, if_exists='replace', index=False)
        print(f"Loaded {table_name} into table '{table_name}'")
    
    if True:
        csv_path = os.path.join(CSV_DIRECTORY, "FAOSTAT_data_en_5-22-2025_Processed.csv")
        
        # Load CSV to DataFrame
        df = load_csv_to_dataframe(csv_path)
        
        # Generate table name from file name (remove .csv and convert to lowercase)
        table_name = "Trade_Matrix_India"
        
        # Save DataFrame to main database
        df.to_sql(table_name, main_engine, if_exists='replace', index=False)
        print(f"Loaded {table_name} into table '{table_name}'")

    print("Data loading complete!")
    print(f"Main database created at: {MAIN_DB_URI}")

if __name__ == "__main__":
    main()