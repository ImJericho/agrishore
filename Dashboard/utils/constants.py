# utils/constants.py
"""Constants and configuration for the agricultural dashboard."""

# Common crop categories (update based on your data)
MAJOR_CROPS = [
    "Wheat", "Rice", "Maize", "Barley", "Oats", "Rye", "Millet", "Sorghum",
    "Potatoes", "Sweet potatoes", "Cassava", "Yams", "Sugar cane", "Sugar beet",
    "Soybeans", "Groundnuts", "Sunflower seed", "Rapeseed", "Oil palm fruit",
    "Coconuts", "Sesame seed", "Cottonseed", "Tomatoes", "Onions", "Carrots",
    "Cabbages", "Lettuce", "Spinach", "Bananas", "Apples", "Oranges", "Grapes"
]

# Country codes mapping (if needed)
COUNTRY_CODES = {
    'India': 'IND',
    'China': 'CHN',
    'United States of America': 'USA',
    'Brazil': 'BRA',
    'Russian Federation': 'RUS',
    # Add more as needed
}

# Chart colors
CHART_COLORS = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
]

# Layout constants
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

# Graph layout defaults
GRAPH_CONFIG = {
    'displayModeBar': True,
    'displaylogo': False,
    'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d']
}