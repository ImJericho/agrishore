# data/database.py
import sqlite3
import pandas as pd
from typing import List, Dict
import config

class DatabaseManager:
    """Handles all database operations for the agricultural dashboard."""
    
    def __init__(self, db_path: str = config.DATABASE_PATH):
        self.db_path = db_path
    
    def get_connection(self):
        """Create database connection."""
        return sqlite3.connect(self.db_path)
    
    def get_available_crops(self) -> List[str]:
        """Get list of all available crops from the database."""
        try:
            with self.get_connection() as conn:
                # Assuming there's a 'Crop' or 'Item' column
                query = f"SELECT DISTINCT Item FROM {config.PRODUCTION_TABLE}"
                crops = pd.read_sql_query(query, conn)['Item'].tolist()
                return sorted(crops)
        except Exception as e:
            print(f"Error getting crops: {e}")
            return []
    
    def get_production_data(self, crop: str) -> pd.DataFrame:
        """Get production data for a specific crop."""
        try:
            with self.get_connection() as conn:
                query = f"""
                SELECT * FROM {config.PRODUCTION_TABLE} 
                WHERE Item = ? AND Element = 'Gross Production Value (current thousand US$)'
                """
                df = pd.read_sql_query(query, conn, params=[crop])
                return df
        except Exception as e:
            print(f"Error getting production data: {e}")
            return pd.DataFrame()
    
    def get_trade_data(self, crop: str, trade_type: str = None) -> pd.DataFrame:
        """Get trade data for a specific crop.
        
        Args:
            crop: Crop name
            trade_type: 'Import' or 'Export' or None for both
        """
        try:
            with self.get_connection() as conn:
                if trade_type:
                    query = f"""
                    SELECT * FROM {config.TRADE_TABLE} 
                    WHERE Item = ? AND Element = ?
                    """
                    df = pd.read_sql_query(query, conn, params=[crop, trade_type])
                else:
                    query = f"""
                    SELECT * FROM {config.TRADE_TABLE} 
                    WHERE Item = ? AND Element IN ('Import value', 'Export value')
                    """
                    df = pd.read_sql_query(query, conn, params=[crop])
                return df
        except Exception as e:
            print(f"Error getting trade data: {e}")
            return pd.DataFrame()
    
    def get_india_trade_partners(self, crop: str) -> Dict[str, pd.DataFrame]:
        """Get India's trade partners for a specific crop."""
        try:
            with self.get_connection() as conn:
                # Import partners (countries India imports from)
                import_query = f"""
                SELECT Reporter Countries, Partner Countries, Element, {', '.join(config.YEAR_COLUMNS)}
                FROM {config.TRADE_TABLE} 
                WHERE Item = ? AND Reporter = 'India' AND Element LIKE '%Import%'
                """
                imports = pd.read_sql_query(import_query, conn, params=[crop])
                
                # Export partners (countries India exports to)
                export_query = f"""
                SELECT Reporter Countries, Partner Countries, Element, {', '.join(config.YEAR_COLUMNS)}
                FROM {config.TRADE_TABLE} 
                WHERE Item = ? AND Reporter = 'India' AND Element LIKE '%Export%'
                """
                exports = pd.read_sql_query(export_query, conn, params=[crop])
                
                return {'imports': imports, 'exports': exports}
        except Exception as e:
            print(f"Error getting India trade data: {e}")
            return {'imports': pd.DataFrame(), 'exports': pd.DataFrame()}