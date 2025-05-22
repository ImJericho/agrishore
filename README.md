# Agricultural Data Dashboard

A comprehensive Plotly Dash application for visualizing global agricultural production and trade data, with a focus on India's agricultural relationships and production trends.

## 📊 Features

### Multi-Crop Analysis
- **Dynamic Navigation**: Sidebar with crop selection
- **Responsive Design**: Works on desktop and mobile devices
- **Real-time Data**: Connects directly to your SQLite database

### India's Trade Analysis
- **Interactive World Map**: Visualize India's import/export relationships
- **Top Trading Partners**: Bar charts showing top 10 import/export partners
- **Trade Breakdown**: Detailed analysis of trade volumes and values

### Global Production Insights
- **Top Producers**: Rankings of leading producing countries
- **Production Trends**: Year-over-year analysis with interactive time controls
- **India's Position**: Highlighting India's rank among global producers

### Key Statistics Dashboard
- Global production totals
- India's production ranking
- Growth rate analysis (CAGR)
- Trade balance insights

## 🏗️ Project Structure

```
agricultural_dashboard/
├── app.py                      # Main Dash application
├── config.py                   # Configuration settings
├── requirements.txt            # Dependencies
├── test_database.py           # Database testing script
├── README.md                  # This file
├── data/
│   └── database.py           # Database operations
├── components/
│   ├── __init__.py
│   ├── layout.py             # UI layouts
│   ├── graphs.py            # Chart generation
│   └── callbacks.py         # Interactive callbacks
├── utils/
│   ├── __init__.py
│   ├── data_processing.py   # Data processing utilities
│   └── constants.py         # Application constants
└── assets/
    └── style.css           # Custom styling
```

## 🚀 Quick Start

### 1. Installation

```bash
# Clone or download the project
cd agricultural_dashboard

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Database Configuration

Update `config.py` with your database details:

```python
# Your database path
DATABASE_PATH = "path/to/your/database.db"

# Your table names
PRODUCTION_TABLE = "your_production_table"
TRADE_TABLE = "your_trade_table"
```

### 3. Database Schema Requirements

#### Production Table Structure:
- `Area` (Country name)
- `Item` (Crop name)
- `Element` (Should include 'Production')
- `Y1961`, `Y1962`, ..., `Y2023` (Year columns)

#### Trade Table Structure (Your Format):
- `Reporter Countries` (Reporting country)
- `Partner Countries` (Trading partner)
- `Element` (Import/Export type)
- `Item` (Crop name)
- `Year` (Single year column)
- `Value` (Trade value)
- `Unit` (Measurement unit)

### 4. Test Your Setup

```bash
# Test database connection
python test_database.py
```

This will verify:
- ✅ Database connection
- ✅ Table structure
- ✅ Sample data availability
- ✅ India's trade data

### 5. Run the Dashboard

```bash
python app.py
```

Visit `http://127.0.0.1:8050` in your browser.

## 📋 Usage Guide

### Navigation
1. **Select a Crop**: Use the sidebar to choose from available crops
2. **Explore Visualizations**: Each crop page contains three main sections:
   - Trade relationships map
   - Production rankings
   - Trend analysis

### Interactive Features
- **Year Range Slider**: Adjust the time period for trend analysis
- **Hover Tooltips**: Get detailed information on chart elements
- **Responsive Charts**: Zoom, pan, and explore data points

### Key Visualizations

#### 1. India's Trade Network
- **World Map**: Color-coded countries showing trade relationships
- **Import/Export Bars**: Side-by-side comparison of trade partners
- **Trade Values**: Actual monetary values and quantities

#### 2. Global Production Analysis
- **Top 10 Producers**: Bar chart with India highlighted
- **Country Rankings**: India's position in global production
- **Production Values**: Actual tonnage data

#### 3. Trend Analysis
- **Time Series**: Multi-country production trends
- **Growth Rates**: Calculate compound annual growth rates
- **Comparative Analysis**: India vs. other major producers

## 🔧 Customization

### Adding New Visualizations
1. Create new graph functions in `components/graphs.py`
2. Add callbacks in `components/callbacks.py`
3. Update layouts in `components/layout.py`

### Styling Modifications
- Edit `assets/style.css` for custom CSS
- Update colors in `utils/constants.py`
- Modify chart configurations in `config.py`

### Data Processing Extensions
- Add functions in `utils/data_processing.py`
- Extend database queries in `data/database.py`
- Create new analysis methods

## 🐛 Troubleshooting

### Common Issues

#### Database Connection Errors
```bash
# Run the test script first
python test_database.py

# Check these items:
# 1. Database path is correct
# 2. Database file exists
# 3. Table names match your database
# 4. Required columns exist
```

#### No Data Displayed
- Verify crop names match between database and application
- Check that India exists in your trade data
- Ensure year columns have numeric data

#### Import Errors
```bash
# Ensure virtual environment is activated
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Performance Tips

#### For Large Datasets
- Add database indexing on frequently queried columns
- Consider data caching for repeated queries
- Limit the number of crops displayed in sidebar

#### Memory Optimization
- Implement lazy loading for large datasets
- Use data sampling for initial visualizations
- Add progress indicators for long-running operations

## 📊 Data Sources

This dashboard is designed to work with FAO (Food and Agriculture Organization) data, but can be adapted for other agricultural datasets with similar structure.

### Expected Data Format
- **Production Data**: Country-wise production by crop and year
- **Trade Data**: Bilateral trade flows between countries
- **Temporal Coverage**: Multi-year data for trend analysis

## 🔄 Future Enhancements

### Planned Features
- [ ] PDF report generation
- [ ] Data export functionality
- [ ] Additional statistical analysis
- [ ] Multi-language support
- [ ] Real-time data updates

### Advanced Analytics
- [ ] Forecasting models
- [ ] Correlation analysis
- [ ] Market price integration
- [ ] Climate data overlay

## 📄 License

This project is open-source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## 📞 Support

If you encounter any issues:
1. Run `python test_database.py` to diagnose problems
2. Check the console for error messages
3. Verify your database schema matches the requirements
4. Ensure all dependencies are properly installed

---

**Happy Analyzing! 🌾📈**