"""
Task 01: Life Expectancy Distribution Dashboard
- Objective: Create a Dash app to visualize life expectancy distribution using a histogram.
- Dataset: Gapminder.
- Key Features: Continent selection dropdown, dynamic histogram updates.
"""


import dash_daq as daq
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, Input, Output, callback, dcc, html


# Initialize the Dash application
app = Dash(__name__)

# Load the Gapminder dataset from plotly express
df = px.data.gapminder()

# Define a color map for visual consistency across continents
continent_colors = {
    'Africa': '#1f77b4',
    'Americas': '#ff7f0e',
    'Asia': '#2ca02c',
    'Europe': '#d62728',
    'Oceania': '#9467bd'
}

# Define the application layout and UI components
app.layout = html.Div(style={'fontFamily': 'Arial, sans-serif', 'padding': '20px'}, children=[
    html.Header(
        html.H1('Life Expectancy Analysis Dashboard', style={'textAlign': 'center', 'color': '#1f77b4'}),
    ),

    html.Div([
        html.Label("Select Continent:", style={'fontWeight': 'bold', 'color': '#2ca02c'}),
        dcc.Dropdown(
            id='continent-dropdown',
            # Map unique continents to dropdown options
            options=[{'label': c, 'value': c} for c in df.continent.unique()],
            value='Europa',     # Default selection on startup
            clearable=False
        ),
    ], style={'width': '30%', 'margin': '20px 0'}),

    # Main graph container for the histogram
    dcc.Graph(id='life-exp-histogram'),

    # Footer section with credits
    html.Footer([
        html.Hr(),
        html.P('© 2007-2026 Analytical Insights | by Halyna Yurkova', style={'fontSize': '12px', 'color': 'gray'})
    ])
])

# Define callback for dynamic UI updates based on user input
@callback(
    Output('life-exp-histogram', 'figure'),
    Input('continent-dropdown', 'value')
)

def update_graph(selected_continent):
    # Filter the primary dataframe based on user selection
    filtered_df = df[df['continent' == selected_continent]]

    # Create a histogram to visualize the distribution of life expectancy
    fig = px.histogram(
        filtered_df, 
        x="lifeExp", 
        nbins=20,           # Set the number of bins for statistical granularity
        title=f"Distribution of Life Expectancy in {selected_continent}",
        labels={'lifeExp': 'Life Expectancy (Years)', 'count': 'Number of Countries'},
        # Apply the specific continent color from the predefined mapping
        color_discrete_sequence=[continent_colors.get(selected_continent, '#636EFA')]
    )

    # Enhance chart aesthetics and axis formatting
    fig.update_layout(
    bargap=0.1,             # Add spacing between bars for better readability
    title_font=dict(size=20),
        xaxis_title="Life Expectancy (Years)",
        yaxis_title="Frequency (Count of Observations)",
        template="plotly_white"
    )
    
    return fig

# Run the server with specific network settings
if __name__ == '__main__':
    # Using port 8055 to avoid common 400 errors and enabling remote access via host '0.0.0.0'
    app.run(debug=True, port=8054, host='0.0.0.0')