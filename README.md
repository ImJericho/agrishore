# Agricultural Dashboard Setup Guide

## Project Structure
```
agricultural_dashboard/
├── app.py                      # Main application entry point
├── config.py                   # Configuration settings
├── requirements.txt            # Python dependencies
├── data/
│   └── database.py            # Database connection and queries
├── components/
│   ├── __init__.py
│   ├── layout.py              # UI layout components
│   ├── graphs.py              # Chart generation functions
│   └── callbacks.py           # Dash callback functions
├── utils/
│   ├── __init__.py
│   ├── data_processing.py     # Data processing utilities
│   └── constants.py           # Application constants
└── assets/
    └── style.css              # Custom CSS styling
```

## Setup Instructions

### 1. Environment Setup
```bash
# Create virtual environment
python -m venv ag_dashboard_env

# Activate environment
# On Windows:
ag_dashboard_env\Scripts\activate
# On macOS/Linux:
source ag_dashboard_env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Database Configuration
Update `config.py` with your database details:

```python
# Update these paths according to your setup
DATABASE_PATH = "path/to/your/database.db"
PRODUCTION_TABLE = "your_production_table_name"
TRADE_TABLE = "your_trade_table_name"
```

### 3. Database Schema Requirements
Your database tables should have the following structure:

**Production Table:**
- `Area` (Country name)
- `Item` (Crop name)
- `Element` (Should contain 'Production')
- `Y1961`, `Y1962`, ..., `Y2023` (Year columns with production values)

**Trade Table:**
- `Reporter` (Reporting country, should include 'India')
- `Partner` (Trading partner country)
- `Item` (Crop name)
- `Element` (Should contain 'Import Quantity', 'Export Quantity', etc.)
- `Y1961`, `Y1962`, ..., `Y2023` (Year columns with trade values)

### 4. Running the Application
```bash
python app.py
```

The dashboard will be available at `http://127.0.0.1:8050`

## Features

### 1. Multi-Crop Analysis
- Navigate between different crops using the sidebar
- Each crop gets its own dedicated analysis page

### 2. India's Trade Analysis
- Interactive world map showing trade relationships
- Top 10 import/export partners
- Combined bar charts for trade comparison

### 3. Global Production Analysis
- Top 10 producing countries
- India's ranking among global producers
- Year-wise production trends

### 4. Interactive Controls
- Year range slider for trend analysis
- Hover tooltips for detailed information
- Responsive design for different screen sizes

## Customization Options

### Adding New Visualizations
1. Add new graph functions in `components/graphs.py`
2. Create corresponding callbacks in `components/callbacks.py`
3. Update layouts in `components/layout.py`

### Styling
- Modify `assets/style.css` for custom styling
- Update colors in `utils/constants.py`
- Adjust layout in `config.py`

### Data Processing
- Add new processing functions in `utils/data_processing.py`
- Update database queries in `data/database.py`

## Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Check database path in `config.py`
   - Ensure database file exists and is accessible
   - Verify table names match your database schema

2. **No Data Displayed**
   - Check if crop names match exactly between database and application
   - Verify year columns exist in your tables
   - Check for data type issues (ensure numeric values)

3. **Import Errors**
   - Ensure all dependencies are installed
   - Check Python version compatibility (3.7+)
   - Verify virtual environment is activated

### Performance Optimization

1. **Large Datasets**
   - Consider adding data caching with Redis
   - Implement pagination for crop selection
   - Add database indexing on frequently queried columns

2. **Memory Usage**
   - Limit the number of crops loaded at once
   - Implement lazy loading for data
   - Use data compression for storage

## Extending the Dashboard

### Adding New Analysis Pages
1. Create new layout functions in `components/layout.py`
2. Add routing logic in `components/callbacks.py`
3. Implement new graph types in `components/graphs.py`

### Integration with Other Data Sources
1. Extend `DatabaseManager` class for new data sources
2. Add new processing functions for different data formats
3. Update configuration for new data connections

### Export Functionality
Consider adding:
- PDF report generation
- Data export to CSV/Excel
- Chart image downloads
- Automated report scheduling

This dashboard provides a solid foundation for agricultural data analysis and can be extended based on specific requirements and additional data sources.