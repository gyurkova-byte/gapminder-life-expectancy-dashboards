"""
Task 03: Life Expectancy Dashboard with Advanced Interactivity
- Objective: Visualize average life expectancy per continent with detailed hover information.
- Dataset: Gapminder.
- Key Features:
    * Dynamic Bar Chart showing yearly averages.
    * Advanced Hover Effects: Displays the TOP-5 countries with the highest life expectancy 
      for each specific year using 'customdata' and 'hovertemplate'.
    * Custom X-axis formatting with rotated labels for all available years.
"""


import plotly.express as px
from dash import Dash, html, dcc, Input, Output, callback

# Initialize the Dash application
app = Dash(__name__)

# Load the Gapminder dataset and calculate mean life expectancy per continent/year
df = px.data.gapminder()
df_mean = df.groupby(['continent', 'year']).mean('lifeExp').reset_index()

# Define the dashboard header with centered title
header = html.Header(html.H1('Life Expectancy Dashboard by Continent.', 
                             style={'textAlign': 'center', 'color': '#1f77b4', 'fontFamily': 'Arial, sans-serif'}))

# Define the dashboard footer with copyright information
footer = html.Footer([
    html.P('Copyright (c) 2007 My Dashboard'),
    html.P('by Halyna Yurkova')
], className='footer')

# Prepare dropdown options based on unique continent values
continent_options = [{'label': cont, 'value': cont} for cont in df_mean.continent.unique()]

# Initialize the dropdown component for continent selection
dropdown_component = dcc.Dropdown(
    id='my-dropdown',
    options=continent_options,
    value='Europe'
)

# Define the application layout structure
app.layout = html.Div([
    header,
    html.H2("Select Continent", style={'color': '#2ca02c', 'fontFamily': 'Arial, sans-serif'}),
    dropdown_component,
    dcc.Graph(id='graph'),
    footer
])

# Define callback to update the graph and hover data based on dropdown input
@callback(
    Output('graph', 'figure'),
    Input('my-dropdown', 'value')
)
def update_graph(selected_continent):
    # Filter the aggregated data for the selected continent
    filtered_df_mean = df_mean[df_mean['continent'] == selected_continent]
    
    # Create the base bar chart
    fig = px.bar(
        filtered_df_mean, 
        x="year", 
        y="lifeExp",
        title=f"Life Expectancy in {selected_continent}",
        labels={
            "year": "Year", 
            "lifeExp": "Average Life Expectancy (years)"}
    )
    
    # Apply layout updates for axes and margins
    fig.update_layout(
        xaxis=dict(
            title_font=dict(color='blue', size=16, family='Arial'),
            # Ensure all years are displayed on the X-axis
            tickvals=filtered_df_mean['year'].unique(),       
            tickangle=-45), # Rotate labels for better readability
        yaxis=dict(title_font=dict(color='green', size=16, family='Arial')),
        # Add padding to prevent label clipping
        margin=dict(l=40, r=40, t=60, b=40))

    # Logic to identify TOP-5 countries for the hover information
    filtered_df = df[df['continent'] == selected_continent] 
    top_5_countries_data = []

    # Iterate through each year to build the TOP-5 country list for hover data
    for year in filtered_df_mean['year'].unique():
        # Sort countries by life expectancy for the specific year and take the top 5
        top_5 = filtered_df[filtered_df['year'] == year].sort_values( 
            by='lifeExp', ascending=False).head(5)
        
        # Format the list as an HTML string for the Plotly tooltip
        top_5_list = '<br>'.join(
            [f"{row['country']}: {row['lifeExp']:.2f} years" for index, row in top_5.iterrows()]
        )
        top_5_countries_data.append(top_5_list)

    # Inject TOP-5 list into 'customdata' and configure the hover template
    fig.update_traces(
        customdata=top_5_countries_data, # Assign processed list to traces
        # Define the visual structure of the hover tooltip
        hovertemplate=f"""   
<b>Continent:</b> {selected_continent}<br>
<b>Average life expectancy:</b> %{{y:.2f}} years<br>
<br>
<b>TOP-5 Countries:</b><br>
%{{customdata}}<extra></extra>
"""
    )

    return fig

# Run the server
if __name__ == '__main__':
    # Standalone script execution (removed jupyter_mode)
    app.run(debug=True, host='0.0.0.0', port=8055)