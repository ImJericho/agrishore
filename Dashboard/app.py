# app.py
import dash
from dash import html
import dash_bootstrap_components as dbc
from data.database import DatabaseManager
from components.layout import LayoutManager
import config

# Initialize the Dash app
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
    title=config.APP_TITLE
)

# Initialize components
db_manager = DatabaseManager()
layout_manager = LayoutManager()

def create_app_layout():
    """Create the main app layout."""
    try:
        # Get available crops from database
        crops = db_manager.get_available_crops()
        
        if not crops:
            return html.Div([
                dbc.Alert([
                    html.H4("Database Connection Error", className="alert-heading"),
                    html.P("Could not connect to the database or no crops found."),
                    html.Hr(),
                    html.P([
                        "Please check your database configuration in ",
                        html.Code("config.py"),
                        " and ensure the database file exists."
                    ], className="mb-0")
                ], color="danger", style={"margin": "2rem"})
            ])
        
        return html.Div([
            layout_manager.create_sidebar(crops),
            layout_manager.create_main_content()
        ])
    
    except Exception as e:
        return html.Div([
            dbc.Alert([
                html.H4("Application Error", className="alert-heading"),
                html.P(f"Error initializing application: {str(e)}"),
                html.Hr(),
                html.P("Please check your configuration and database setup.", className="mb-0")
            ], color="danger", style={"margin": "2rem"})
        ])

# Set the app layout
app.layout = create_app_layout()

# Import callbacks (this registers all the callback functions)
from components import callbacks

if __name__ == "__main__":
    print(f"Starting {config.APP_TITLE}")
    print(f"Debug mode: {config.DEBUG_MODE}")
    print(f"Access the dashboard at: http://{config.APP_HOST}:{config.APP_PORT}")
    
    app.run(
        host=config.APP_HOST,
        port=config.APP_PORT,
        debug=config.DEBUG_MODE
    )