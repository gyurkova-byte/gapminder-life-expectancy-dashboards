"""
Task 02: Yearly Life Expectancy Comparison by Continent
- Objective: Create an interactive bar chart to compare average life expectancy across years.
- Dataset: Gapminder (aggregated by mean).
- Key Features: 
    * "All Continents" view for global comparison (grouped bar chart).
    * Individual continent filtering via dropdown.
    * Customized axis labels and branding colors.
"""


import plotly.express as px
from dash import Dash, html, dcc, Input, Output, callback

# Initialize the Dash application
app = Dash(__name__)

# Data preparation: loading Gapminder and calculating mean life expectancy per continent/year
df = px.data.gapminder()
df_mean = df.groupby(['continent', 'year']).mean('lifeExp').reset_index()
available_years = df_mean['year'].unique()

# Define a fixed color mapping for consistent continent branding
continent_colors = {
    'Africa': '#1f77b4',
    'America': '#ff7f0e',
    'Asia': '#2ca02c',
    'Europe': '#d62728',
    'Oceania': '#9467bd'
}

# Define the dashboard header with custom styling
header = html.Header(html.H1('Life Expectancy Dashboard by Continent.', 
                             style={'textAlign': 'center', 'color': '#1f77b4', 'fontFamily': 'Arial, sans-serif'}))

# Define the dashboard footer
footer = html.Footer([
    html.P('Copyright (c) 2007 My Dashboard'),
    html.P('by Halyna Yurkova')
], className='footer')

# Create dropdown options including a global "All Continents" view
continent_options = [{'label': 'All Continents', 'value': 'All'}] + \
                    [{'label': cont, 'value': cont} for cont in df_mean.continent.unique()]

# Initialize the dropdown component
dropdown_component = dcc.Dropdown(
    id='my-dropdown',
    options=continent_options,
    value='All'
)

# Define the final Dash layout structure
app.layout = html.Div([
    header,
    html.H2("Select Continent", style={'color': '#2ca02c', 'fontFamily': 'Arial, sans-serif'}),
    dropdown_component,
    dcc.Graph(id='graph'),
    footer
])

# Define callback to update the bar chart based on dropdown selection
@callback(
    Output('graph', 'figure'),
    Input('my-dropdown', 'value')
)

def update_graph(selected_continent):
    # Set localized labels for the chart axes
    custom_labels = {"year": "Year", "lifeExp": "Average Life Expectancy (Years)"}
    
    if selected_continent == 'All':
        # Generate a grouped bar chart for all continents
        fig = px.bar(
            df_mean,
            x='year',
            y='lifeExp',
            color='continent',
            barmode='group', # Groups bars side-by-side for yearly comparison
            labels=custom_labels,
            color_discrete_map=continent_colors, # Apply consistent colors
            title="Life Expectancy in All Continents"
        )
        
    else:
        # Filter the aggregated dataframe for the specific continent
        filtered_df = df_mean[df_mean['continent'] == selected_continent]

        # Generate a bar chart for the selected individual continent
        fig = px.bar(
            filtered_df,
            x="year",
            y="lifeExp",
            title=f"Life Expectancy in {selected_continent}",
            labels=custom_labels,
            color="continent",                  # Keep 'continent' as color reference for consistency
            color_discrete_map=continent_colors
        )

    # Apply advanced layout configurations and axis formatting
    fig.update_layout(
        xaxis=dict(
            tickmode='array',
            tickvals=available_years,
            ticktext=[str(year) for year in available_years], # Convert years to string labels
            title_font=dict(size=16, family='Arial', color='blue')
        ),
        yaxis=dict(
            title_font=dict(size=16, family='Arial', color='green')
        ),
        title_font=dict(size=20, family='Arial', color='#000000'),
        margin=dict(l=40, r=40, t=60, b=40) # Add padding to prevent label clipping
    )

    return fig

# Run the application
if __name__ == '__main__':
    # Running on port 8053 with global access enabled
    app.run(debug=True, host='0.0.0.0', port=8053)