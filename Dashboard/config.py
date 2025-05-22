# config.py
import os

# Database configuration
DATABASE_PATH = "/Users/vivek/DriveE/PROJECTS/agrishore/main_database.db"  # Update this path
PRODUCTION_TABLE = "Value_of_Production_E_All_Data"       # Update table name
TRADE_TABLE = "Trade_Matrix_India"                # Update table name

# Application configuration
APP_TITLE = "Agricultural Data Dashboard"
APP_HOST = "127.0.0.1"
APP_PORT = 8050
DEBUG_MODE = True

# Data configuration
YEAR_COLUMNS = [f"Y{year}" for year in range(1961, 2024)]
LATEST_YEAR = 2023
TOP_N_COUNTRIES = 10

# Colors for visualization
COLORS = {
    'primary': '#1f77b4',
    'secondary': '#ff7f0e',
    'success': '#2ca02c',
    'danger': '#d62728',
    'warning': '#ff7f0e',
    'info': '#17a2b8',
    'light': '#f8f9fa',
    'dark': '#343a40'
}