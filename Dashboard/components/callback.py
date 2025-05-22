# components/callbacks.py
from dash import callback, Input, Output, State
import pandas as pd
from urllib.parse import unquote
from data.database import DatabaseManager
from utils.data_processing import DataProcessor
from components.graphs import GraphGenerator
from components.layout import LayoutManager
import config

# Initialize components
db_manager = DatabaseManager()
data_processor = DataProcessor()
graph_generator = GraphGenerator()
layout_manager = LayoutManager()

@callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def display_page(pathname):
    """Handle page routing."""
    if pathname == "/" or pathname is None:
        return layout_manager.create_home_page()
    
    elif pathname.startswith("/crop/"):
        try:
            # Extract crop name from URL
            crop_slug = pathname.split("/crop/")[1]
            crop_name = unquote(crop_slug).replace("-", " ").title()
            
            # Verify crop exists in database
            available_crops = db_manager.get_available_crops()
            
            # Try to find exact match or similar match
            matching_crop = None
            for crop in available_crops:
                if crop.lower() == crop_name.lower():
                    matching_crop = crop
                    break
            
            if matching_crop:
                return layout_manager.create_crop_page_layout(matching_crop)
            else:
                return layout_manager.create_error_page(f"Crop '{crop_name}' not found in database.")
        
        except Exception as e:
            return layout_manager.create_error_page(f"Error loading crop data: {str(e)}")
    
    else:
        return layout_manager.create_error_page("Page not found.")

@callback(
    Output("crop-data-store", "data"),
    [Input("selected-crop", "data")]
)
def load_crop_data(crop):
    """Load and store crop data."""
    if not crop:
        return {}
    
    try:
        # Get production data
        production_data = db_manager.get_production_data(crop)
        
        # Get trade data
        trade_data = db_manager.get_india_trade_partners(crop)
        
        # Process and store data
        data = {
            "crop": crop,
            "production_data": production_data.to_dict('records') if not production_data.empty else [],
            "trade_imports": trade_data['imports'].to_dict('records') if not trade_data['imports'].empty else [],
            "trade_exports": trade_data['exports'].to_dict('records') if not trade_data['exports'].empty else []
        }
        
        return data
    
    except Exception as e:
        print(f"Error loading crop data: {e}")
        return {}

@callback(
    Output("world-trade-map", "figure"),
    [Input("crop-data-store", "data")]
)
def update_world_trade_map(stored_data):
    """Update the world trade map."""
    if not stored_data or not stored_data.get("crop"):
        return graph_generator.create_world_trade_map({}, "")
    
    try:
        # Reconstruct dataframes from stored data
        imports_df = pd.DataFrame(stored_data.get("trade_imports", []))
        exports_df = pd.DataFrame(stored_data.get("trade_exports", []))
        
        trade_data = {
            'imports': imports_df,
            'exports': exports_df
        }
        
        return graph_generator.create_world_trade_map(trade_data, stored_data["crop"])
    
    except Exception as e:
        print(f"Error creating world trade map: {e}")
        return graph_generator.create_world_trade_map({}, "")

@callback(
    Output("trade-breakdown-chart", "figure"),
    [Input("crop-data-store", "data")]
)
def update_trade_breakdown(stored_data):
    """Update trade breakdown chart."""
    if not stored_data or not stored_data.get("crop"):
        return graph_generator.create_combined_trade_bar({}, "")
    
    try:
        imports_df = pd.DataFrame(stored_data.get("trade_imports", []))
        exports_df = pd.DataFrame(stored_data.get("trade_exports", []))
        
        trade_data = {
            'imports': imports_df,
            'exports': exports_df
        }
        
        return graph_generator.create_combined_trade_bar(trade_data, stored_data["crop"])
    
    except Exception as e:
        print(f"Error creating trade breakdown: {e}")
        return graph_generator.create_combined_trade_bar({}, "")

@callback(
    Output("top-producers-chart", "figure"),
    [Input("crop-data-store", "data")]
)
def update_top_producers(stored_data):
    """Update top producers chart."""
    if not stored_data or not stored_data.get("crop"):
        return graph_generator.create_top_producers_bar(pd.DataFrame(), "")
    
    try:
        production_df = pd.DataFrame(stored_data.get("production_data", []))
        
        if not production_df.empty:
            # Get top producers
            top_producers = data_processor.get_top_producers(production_df, config.TOP_N_COUNTRIES)
            
            # Ensure India is included
            top_producers_with_india = data_processor.add_india_to_top_producers(
                top_producers, production_df
            )
            
            return graph_generator.create_top_producers_bar(
                top_producers_with_india, stored_data["crop"]
            )
        else:
            return graph_generator.create_top_producers_bar(pd.DataFrame(), stored_data["crop"])
    
    except Exception as e:
        print(f"Error creating top producers chart: {e}")
        return graph_generator.create_top_producers_bar(pd.DataFrame(), "")

@callback(
    Output("yearwise-production-chart", "figure"),
    [Input("crop-data-store", "data"),
     Input("year-range-slider", "value")]
)
def update_yearwise_production(stored_data, year_range):
    """Update year-wise production chart."""
    if not stored_data or not stored_data.get("crop"):
        return graph_generator.create_yearwise_production_line(pd.DataFrame(), "")
    
    try:
        production_df = pd.DataFrame(stored_data.get("production_data", []))
        
        if not production_df.empty:
            # Get top producers for the selected countries
            top_producers = data_processor.get_top_producers(production_df, config.TOP_N_COUNTRIES)
            
            # Add India if not in top producers
            top_producers_with_india = data_processor.add_india_to_top_producers(
                top_producers, production_df
            )
            
            countries = top_producers_with_india['Area'].tolist()
            
            # Get year-wise data for these countries
            yearwise_data = data_processor.get_yearwise_production(production_df, countries)
            
            # Filter by year range if provided
            if year_range and len(year_range) == 2:
                yearwise_data = yearwise_data[
                    (yearwise_data['Year'] >= year_range[0]) & 
                    (yearwise_data['Year'] <= year_range[1])
                ]
            
            return graph_generator.create_yearwise_production_line(
                yearwise_data, stored_data["crop"], countries
            )
        else:
            return graph_generator.create_yearwise_production_line(pd.DataFrame(), stored_data["crop"])
    
    except Exception as e:
        print(f"Error creating yearwise production chart: {e}")
        return graph_generator.create_yearwise_production_line(pd.DataFrame(), "")

@callback(
    Output("summary-stats", "children"),
    [Input("crop-data-store", "data")]
)
def update_summary_stats(stored_data):
    """Update summary statistics."""
    if not stored_data or not stored_data.get("crop"):
        return layout_manager.create_summary_cards({})
    
    try:
        production_df = pd.DataFrame(stored_data.get("production_data", []))
        
        if not production_df.empty:
            year_col = f"Y{config.LATEST_YEAR}"
            
            # Calculate statistics
            stats = {}
            
            # Global production
            if year_col in production_df.columns:
                stats['global_production'] = production_df[year_col].sum()
                
                # India's production and rank
                india_data = production_df[production_df['Area'] == 'India']
                if not india_data.empty:
                    stats['india_production'] = india_data[year_col].iloc[0]
                    
                    # Calculate India's rank
                    sorted_countries = production_df.sort_values(year_col, ascending=False).reset_index(drop=True)
                    india_rank = sorted_countries[sorted_countries['Area'] == 'India'].index
                    if len(india_rank) > 0:
                        stats['india_rank'] = india_rank[0] + 1
                
                # Calculate growth rate (10-year CAGR)
                growth_data = data_processor.calculate_growth_rate(
                    production_df, config.LATEST_YEAR - 10, config.LATEST_YEAR
                )
                if not growth_data.empty:
                    global_growth = growth_data['CAGR'].mean()
                    stats['growth_rate'] = global_growth
            
            return layout_manager.create_summary_cards(stats)
        else:
            return layout_manager.create_summary_cards({})
    
    except Exception as e:
        print(f"Error calculating summary stats: {e}")
        return layout_manager.create_summary_cards({})