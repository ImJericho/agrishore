# components/graphs.py
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from typing import Dict, List
from utils.constants import CHART_COLORS, GRAPH_CONFIG
import config

class GraphGenerator:
    """Generates various types of graphs for the agricultural dashboard."""
    
    @staticmethod
    def create_world_trade_map(trade_data: Dict[str, pd.DataFrame], crop: str) -> go.Figure:
        """Create a world map showing India's trade relationships."""
        fig = go.Figure()
        
        # Process import data
        if not trade_data['imports'].empty:
            imports = trade_data['imports']
            year_col = f"Y{config.LATEST_YEAR}"
            if year_col in imports.columns:
                import_partners = imports.groupby('Partner')[year_col].sum().reset_index()
                import_partners = import_partners.sort_values(year_col, ascending=False).head(10)
                
                fig.add_trace(go.Choropleth(
                    locations=import_partners['Partner'],
                    z=import_partners[year_col],
                    locationmode='country names',
                    colorscale='Blues',
                    name='Imports',
                    hovertemplate='<b>%{location}</b><br>Import Value: %{z}<extra></extra>'
                ))
        
        # Process export data
        if not trade_data['exports'].empty:
            exports = trade_data['exports']
            year_col = f"Y{config.LATEST_YEAR}"
            if year_col in exports.columns:
                export_partners = exports.groupby('Partner')[year_col].sum().reset_index()
                export_partners = export_partners.sort_values(year_col, ascending=False).head(10)
                
                fig.add_trace(go.Choropleth(
                    locations=export_partners['Partner'],
                    z=export_partners[year_col],
                    locationmode='country names',
                    colorscale='Reds',
                    name='Exports',
                    hovertemplate='<b>%{location}</b><br>Export Value: %{z}<extra></extra>'
                ))
        
        fig.update_layout(
            title=f"India's {crop} Trade Partners ({config.LATEST_YEAR})",
            geo=dict(
                showframe=False,
                showcoastlines=True,
                projection_type='equirectangular'
            ),
            height=500
        )
        
        return fig
    
    @staticmethod
    def create_top_producers_bar(production_data: pd.DataFrame, crop: str, year: int = None) -> go.Figure:
        """Create bar chart of top producing countries."""
        if production_data.empty:
            return go.Figure().add_annotation(
                text="No data available", 
                xref="paper", yref="paper",
                x=0.5, y=0.5, showarrow=False
            )
        
        if year is None:
            year = config.LATEST_YEAR
        
        year_col = f"Y{year}"
        
        # Highlight India if present
        colors = []
        for country in production_data['Area']:
            if country == 'India':
                colors.append('#ff7f0e')  # Orange for India
            else:
                colors.append('#1f77b4')  # Blue for others
        
        fig = go.Figure(data=[
            go.Bar(
                x=production_data['Area'],
                y=production_data[year_col],
                marker_color=colors,
                hovertemplate='<b>%{x}</b><br>Production: %{y:,.0f}<extra></extra>'
            )
        ])
        
        fig.update_layout(
            title=f"Top {len(production_data)} {crop} Producers ({year})",
            xaxis_title="Country",
            yaxis_title="Production (tonnes)",
            xaxis_tickangle=-45,
            height=500
        )
        
        return fig
    
    @staticmethod
    def create_yearwise_production_line(yearwise_data: pd.DataFrame, crop: str, countries: List[str] = None) -> go.Figure:
        """Create line chart showing year-wise production trends."""
        if yearwise_data.empty:
            return go.Figure().add_annotation(
                text="No data available", 
                xref="paper", yref="paper",
                x=0.5, y=0.5, showarrow=False
            )
        
        fig = go.Figure()
        
        # Add line for each country
        for i, country in enumerate(yearwise_data['Area'].unique()):
            country_data = yearwise_data[yearwise_data['Area'] == country]
            
            # Special styling for India
            line_color = '#ff7f0e' if country == 'India' else CHART_COLORS[i % len(CHART_COLORS)]
            line_width = 3 if country == 'India' else 2
            
            fig.add_trace(go.Scatter(
                x=country_data['Year'],
                y=country_data['Production'],
                mode='lines+markers',
                name=country,
                line=dict(color=line_color, width=line_width),
                hovertemplate='<b>%{fullData.name}</b><br>Year: %{x}<br>Production: %{y:,.0f}<extra></extra>'
            ))
        
        fig.update_layout(
            title=f"{crop} Production Trends Over Time",
            xaxis_title="Year",
            yaxis_title="Production (tonnes)",
            height=500,
            hovermode='x unified'
        )
        
        return fig
    
    @staticmethod
    def create_trade_breakdown_pie(trade_data: pd.DataFrame, trade_type: str, crop: str) -> go.Figure:
        """Create pie chart showing trade breakdown by partners."""
        if trade_data.empty:
            return go.Figure().add_annotation(
                text="No data available", 
                xref="paper", yref="paper",
                x=0.5, y=0.5, showarrow=False
            )
        
        year_col = f"Y{config.LATEST_YEAR}"
        
        if year_col not in trade_data.columns:
            return go.Figure().add_annotation(
                text="No recent data available", 
                xref="paper", yref="paper",
                x=0.5, y=0.5, showarrow=False
            )
        
        # Group by partner and sum values
        trade_summary = trade_data.groupby('Partner')[year_col].sum().reset_index()
        trade_summary = trade_summary.sort_values(year_col, ascending=False).head(10)
        
        fig = go.Figure(data=[
            go.Pie(
                labels=trade_summary['Partner'],
                values=trade_summary[year_col],
                hole=0.3,
                hovertemplate='<b>%{label}</b><br>Value: %{value:,.0f}<br>Percentage: %{percent}<extra></extra>'
            )
        ])
        
        fig.update_layout(
            title=f"India's {crop} {trade_type} Partners ({config.LATEST_YEAR})",
            height=500
        )
        
        return fig
    
    @staticmethod
    def create_combined_trade_bar(trade_data: Dict[str, pd.DataFrame], crop: str) -> go.Figure:
        """Create combined bar chart showing both imports and exports."""
        fig = go.Figure()
        
        year_col = f"Y{config.LATEST_YEAR}"
        
        # Process imports
        if not trade_data['imports'].empty and year_col in trade_data['imports'].columns:
            imports = trade_data['imports'].groupby('Partner')[year_col].sum().reset_index()
            imports = imports.sort_values(year_col, ascending=False).head(10)
            
            fig.add_trace(go.Bar(
                name='Imports',
                x=imports['Partner'],
                y=imports[year_col],
                marker_color='lightblue',
                hovertemplate='<b>%{x}</b><br>Imports: %{y:,.0f}<extra></extra>'
            ))
        
        # Process exports
        if not trade_data['exports'].empty and year_col in trade_data['exports'].columns:
            exports = trade_data['exports'].groupby('Partner')[year_col].sum().reset_index()
            exports = exports.sort_values(year_col, ascending=False).head(10)
            
            fig.add_trace(go.Bar(
                name='Exports',
                x=exports['Partner'],
                y=exports[year_col],
                marker_color='lightcoral',
                hovertemplate='<b>%{x}</b><br>Exports: %{y:,.0f}<extra></extra>'
            ))
        
        fig.update_layout(
            title=f"India's {crop} Trade Overview ({config.LATEST_YEAR})",
            xaxis_title="Country",
            yaxis_title="Trade Value",
            barmode='group',
            xaxis_tickangle=-45,
            height=500
        )
        
        return fig