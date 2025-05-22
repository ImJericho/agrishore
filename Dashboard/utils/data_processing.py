# utils/data_processing.py
import pandas as pd
import numpy as np
from typing import List, Dict, Tuple
import config
from utils.constants import CHART_COLORS

class DataProcessor:
    """Handles data processing and transformation for visualizations."""
    
    @staticmethod
    def get_top_producers(df: pd.DataFrame, n: int = 10, year: int = None) -> pd.DataFrame:
        """Get top N producing countries for a specific year or latest available year."""
        if df.empty:
            return pd.DataFrame()
        
        # Use latest year if not specified
        if year is None:
            year = config.LATEST_YEAR
        
        year_col = f"Y{year}"
        
        # If specified year doesn't exist, find the latest available year
        if year_col not in df.columns:
            available_years = [col for col in df.columns if col.startswith('Y')]
            if not available_years:
                return pd.DataFrame()
            year_col = max(available_years)
        
        # Filter and sort by production value
        top_producers = df[['Area', year_col]].copy()
        top_producers = top_producers.dropna()
        top_producers = top_producers.sort_values(year_col, ascending=False).head(n)
        
        return top_producers
    
    @staticmethod
    def get_yearwise_production(df: pd.DataFrame, countries: List[str] = None) -> pd.DataFrame:
        """Get year-wise production data for specified countries."""
        if df.empty:
            return pd.DataFrame()
        
        # Filter for specified countries if provided
        if countries:
            df_filtered = df[df['Area'].isin(countries)].copy()
        else:
            df_filtered = df.copy()
        
        # Melt the dataframe to get year-wise data
        year_cols = [col for col in df_filtered.columns if col.startswith('Y')]
        id_cols = ['Area', 'Item'] if 'Item' in df_filtered.columns else ['Area']
        
        melted = pd.melt(df_filtered, 
                        id_vars=id_cols,
                        value_vars=year_cols,
                        var_name='Year',
                        value_name='Production')
        
        # Clean year column
        melted['Year'] = melted['Year'].str.replace('Y', '').astype(int)
        melted = melted.dropna(subset=['Production'])
        
        return melted
    
    @staticmethod
    def get_top_trade_partners(df: pd.DataFrame, n: int = 10, year: int = None) -> pd.DataFrame:
        """Get top N trade partners for India."""
        if df.empty:
            return pd.DataFrame()
        
        if year is None:
            year = config.LATEST_YEAR
        
        year_col = f"Y{year}"
        
        # If specified year doesn't exist, find the latest available year
        if year_col not in df.columns:
            available_years = [col for col in df.columns if col.startswith('Y')]
            if not available_years:
                return pd.DataFrame()
            year_col = max(available_years)
        
        # Get trade data for the specified year
        trade_data = df[['Partner', 'Element', year_col]].copy()
        trade_data = trade_data.dropna()
        
        # Group by partner and sum if multiple elements
        trade_summary = trade_data.groupby(['Partner', 'Element'])[year_col].sum().reset_index()
        
        # Get top partners
        top_partners = trade_summary.sort_values(year_col, ascending=False).head(n)
        
        return top_partners
    
    @staticmethod
    def prepare_world_map_data(df: pd.DataFrame, year: int = None) -> pd.DataFrame:
        """Prepare data for world map visualization."""
        if df.empty:
            return pd.DataFrame()
        
        if year is None:
            year = config.LATEST_YEAR
        
        year_col = f"Y{year}"
        
        if year_col not in df.columns:
            available_years = [col for col in df.columns if col.startswith('Y')]
            if not available_years:
                return pd.DataFrame()
            year_col = max(available_years)
        
        # Prepare data for choropleth map
        map_data = df[['Area', year_col]].copy()
        map_data = map_data.dropna()
        map_data.columns = ['Country', 'Value']
        
        return map_data
    
    @staticmethod
    def calculate_growth_rate(df: pd.DataFrame, start_year: int, end_year: int) -> pd.DataFrame:
        """Calculate compound annual growth rate for production."""
        if df.empty:
            return pd.DataFrame()
        
        start_col = f"Y{start_year}"
        end_col = f"Y{end_year}"
        
        if start_col not in df.columns or end_col not in df.columns:
            return pd.DataFrame()
        
        growth_data = df[['Area', start_col, end_col]].copy()
        growth_data = growth_data.dropna()
        
        # Calculate CAGR
        years = end_year - start_year
        growth_data['CAGR'] = ((growth_data[end_col] / growth_data[start_col]) ** (1/years) - 1) * 100
        
        return growth_data[['Area', 'CAGR']].sort_values('CAGR', ascending=False)
    
    @staticmethod
    def add_india_to_top_producers(top_producers: pd.DataFrame, all_data: pd.DataFrame, year: int = None) -> pd.DataFrame:
        """Ensure India is included in the top producers list."""
        if year is None:
            year = config.LATEST_YEAR
        
        year_col = f"Y{year}"
        
        # Check if India is already in top producers
        if 'India' in top_producers['Area'].values:
            return top_producers
        
        # Find India's production value
        india_data = all_data[all_data['Area'] == 'India']
        if not india_data.empty and year_col in india_data.columns:
            india_value = india_data[year_col].iloc[0]
            if pd.notna(india_value):
                # Add India to the list
                india_row = pd.DataFrame({'Area': ['India'], year_col: [india_value]})
                combined = pd.concat([top_producers, india_row], ignore_index=True)
                return combined.sort_values(year_col, ascending=False)
        
        return top_producers