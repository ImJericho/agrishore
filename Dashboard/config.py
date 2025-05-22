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

# Production table configuration (using Y1961, Y1962, etc. format)
YEAR_COLUMNS = [f"Y{year}" for year in range(1961, 2024)]
LATEST_YEAR = 2023
TOP_N_COUNTRIES = 10

# Trade table specific configuration (based on your actual table structure)
TRADE_YEAR_COLUMN = "Year"
TRADE_VALUE_COLUMN = "Value"
TRADE_ELEMENT_COLUMN = "Element"
TRADE_REPORTER_COLUMN = "\"Reporter Countries\""
TRADE_PARTNER_COLUMN = "\"Partner Countries\""
TRADE_ITEM_COLUMN = "Item"
TRADE_UNIT_COLUMN = "Unit"

# Production table specific configuration
PRODUCTION_AREA_COLUMN = "Area"
PRODUCTION_ITEM_COLUMN = "Item"
PRODUCTION_ELEMENT_COLUMN = "Element"

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

# Chart configuration
CHART_HEIGHT = 500
CHART_COLORS = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
]

# Data filtering options
MIN_YEAR = 1961
MAX_YEAR = 2023
DEFAULT_YEAR_RANGE = [2000, 2023]

# Trade data filtering
IMPORT_KEYWORDS = ['Import', 'import']
EXPORT_KEYWORDS = ['Export', 'export']