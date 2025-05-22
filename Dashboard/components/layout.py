# components/layout.py
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from typing import List
from utils.constants import SIDEBAR_STYLE, CONTENT_STYLE
import config

class LayoutManager:
    """Manages the layout components of the dashboard."""
    
    @staticmethod
    def create_sidebar(crops: List[str]) -> html.Div:
        """Create the sidebar with navigation."""
        return html.Div([
            html.H2("Agricultural Dashboard", className="display-4"),
            html.Hr(),
            html.P("Select a crop to analyze:", className="lead"),
            dbc.Nav([
                dbc.NavLink(
                    crop, 
                    href=f"/crop/{crop.lower().replace(' ', '-')}", 
                    active="exact",
                    className="mb-1"
                ) for crop in crops[:20]  # Limit to first 20 crops for display
            ], vertical=True, pills=True),
            html.Hr(),
            html.P(f"Data from {config.YEAR_COLUMNS[0][1:]} to {config.LATEST_YEAR}", 
                   className="text-muted small")
        ], style=SIDEBAR_STYLE)
    
    @staticmethod
    def create_main_content() -> html.Div:
        """Create the main content area."""
        return html.Div([
            dcc.Location(id="url", refresh=False),
            html.Div(id="page-content")
        ], style=CONTENT_STYLE)
    
    @staticmethod
    def create_crop_page_layout(crop: str) -> html.Div:
        """Create layout for individual crop pages."""
        return html.Div([
            # Header
            dbc.Row([
                dbc.Col([
                    html.H1(f"{crop} Analysis Dashboard", className="text-center mb-4"),
                    html.Hr()
                ])
            ]),
            
            # Loading component
            dcc.Loading(
                id="loading",
                type="default",
                children=[
                    # India's Trade with World
                    dbc.Row([
                        dbc.Col([
                            html.H3("India's Trade Network", className="mb-3"),
                            dbc.Card([
                                dbc.CardBody([
                                    dcc.Graph(id="world-trade-map")
                                ])
                            ])
                        ])
                    ], className="mb-4"),
                    
                    # Trade breakdown charts
                    dbc.Row([
                        dbc.Col([
                            html.H4("Import/Export Breakdown", className="mb-3"),
                            dcc.Graph(id="trade-breakdown-chart")
                        ], width=12)
                    ], className="mb-4"),
                    
                    # Top Producers
                    dbc.Row([
                        dbc.Col([
                            html.H3("Top Producing Countries", className="mb-3"),
                            dbc.Card([
                                dbc.CardBody([
                                    dcc.Graph(id="top-producers-chart")
                                ])
                            ])
                        ])
                    ], className="mb-4"),
                    
                    # Year-wise Production Trends
                    dbc.Row([
                        dbc.Col([
                            html.H3("Production Trends Over Time", className="mb-3"),
                            dbc.Card([
                                dbc.CardBody([
                                    html.Div([
                                        html.Label("Select Year Range:", className="mb-2"),
                                        dcc.RangeSlider(
                                            id="year-range-slider",
                                            min=1961,
                                            max=config.LATEST_YEAR,
                                            value=[2000, config.LATEST_YEAR],
                                            marks={
                                                1961: '1961',
                                                1980: '1980',
                                                2000: '2000',
                                                2020: '2020',
                                                config.LATEST_YEAR: str(config.LATEST_YEAR)
                                            },
                                            step=1,
                                            className="mb-3"
                                        )
                                    ]),
                                    dcc.Graph(id="yearwise-production-chart")
                                ])
                            ])
                        ])
                    ], className="mb-4"),
                    
                    # Summary Statistics
                    dbc.Row([
                        dbc.Col([
                            html.H3("Key Statistics", className="mb-3"),
                            html.Div(id="summary-stats")
                        ])
                    ])
                ]
            ),
            
            # Store components for data
            dcc.Store(id="crop-data-store"),
            dcc.Store(id="selected-crop", data=crop)
        ])
    
    @staticmethod
    def create_summary_cards(stats: dict) -> html.Div:
        """Create summary statistics cards."""
        cards = []
        
        for title, value, description in [
            ("Global Production", f"{stats.get('global_production', 0):,.0f} tonnes", "Total world production"),
            ("India's Rank", f"#{stats.get('india_rank', 'N/A')}", "Among world producers"),
            ("India's Production", f"{stats.get('india_production', 0):,.0f} tonnes", "India's contribution"),
            ("Growth Rate", f"{stats.get('growth_rate', 0):.1f}%", "10-year CAGR")
        ]:
            card = dbc.Card([
                dbc.CardBody([
                    html.H4(title, className="card-title"),
                    html.H2(value, className="text-primary"),
                    html.P(description, className="card-text text-muted")
                ])
            ], className="mb-3 summary-card")
            cards.append(dbc.Col(card, width=3))
        
        return dbc.Row(cards)
    
    @staticmethod
    def create_home_page() -> html.Div:
        """Create the home page layout."""
        return html.Div([
            dbc.Container([
                dbc.Jumbotron([
                    html.H1("Agricultural Data Dashboard", className="display-3"),
                    html.P("Explore global agricultural production and trade data", 
                           className="lead"),
                    html.Hr(className="my-2"),
                    html.P("Select a crop from the sidebar to view detailed analysis including:"),
                    html.Ul([
                        html.Li("India's trade relationships with other countries"),
                        html.Li("Top producing countries worldwide"),
                        html.Li("Production trends over time"),
                        html.Li("Key statistics and insights")
                    ]),
                    html.P("Data sourced from FAO (Food and Agriculture Organization)", 
                           className="text-muted")
                ], fluid=True),
                
                # Quick stats or overview cards
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H4("📊 Multi-Crop Analysis", className="card-title"),
                                html.P("Analyze production and trade data for various agricultural crops", 
                                       className="card-text")
                            ])
                        ])
                    ], width=4),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H4("🌍 Global Trade Insights", className="card-title"),
                                html.P("Visualize India's trade relationships with countries worldwide", 
                                       className="card-text")
                            ])
                        ])
                    ], width=4),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H4("📈 Trend Analysis", className="card-title"),
                                html.P("Track production trends over decades with interactive charts", 
                                       className="card-text")
                            ])
                        ])
                    ], width=4)
                ], className="mt-4")
            ], fluid=True)
        ])
    
    @staticmethod
    def create_error_page(error_message: str) -> html.Div:
        """Create error page layout."""
        return html.Div([
            dbc.Container([
                dbc.Alert([
                    html.H4("Error", className="alert-heading"),
                    html.P(error_message),
                    html.Hr(),
                    html.P("Please try selecting a different crop from the sidebar.", 
                           className="mb-0")
                ], color="danger"),
                
                # Add some helpful information
                dbc.Card([
                    dbc.CardHeader("Troubleshooting Tips"),
                    dbc.CardBody([
                        html.Ul([
                            html.Li("Check if the crop name exists in your database"),
                            html.Li("Verify your database connection settings in config.py"),
                            html.Li("Ensure the database tables have the required columns"),
                            html.Li("Check the application logs for detailed error information")
                        ])
                    ])
                ], className="mt-3")
            ], fluid=True)
        ])
    
    @staticmethod
    def create_loading_placeholder() -> html.Div:
        """Create a loading placeholder layout."""
        return html.Div([
            dbc.Container([
                dbc.Row([
                    dbc.Col([
                        dbc.Spinner(
                            html.Div([
                                html.H3("Loading crop data..."),
                                html.P("Please wait while we fetch the latest agricultural data.")
                            ]),
                            size="lg",
                            color="primary"
                        )
                    ], className="text-center")
                ], justify="center", className="mt-5")
            ])
        ])
    
    @staticmethod
    def create_no_data_message(crop: str) -> html.Div:
        """Create a no data available message."""
        return html.Div([
            dbc.Container([
                dbc.Alert([
                    html.H4("No Data Available", className="alert-heading"),
                    html.P(f"No data found for {crop} in the database."),
                    html.Hr(),
                    html.P([
                        "This could mean:",
                        html.Ul([
                            html.Li("The crop data hasn't been imported yet"),
                            html.Li("The crop name doesn't match the database records"),
                            html.Li("Data for this crop is not available in the selected time range")
                        ])
                    ], className="mb-0")
                ], color="warning")
            ])
        ])