import plotly.graph_objects as go

# Step 1: Define the data
teams = ['West Indies', 'India', 'Australia', 'Pakistan', 'Sri Lanka', 'England']
wins = [2, 2, 6, 1, 1, 1]
years = {
    'West Indies': '1975, 1979',
    'India': '1983, 2011',
    'Australia': '1987, 1999, 2003, 2007, 2015, 2023',
    'Pakistan': '1992',
    'Sri Lanka': '1996',
    'England': '2019'
}

# Step 2: Create hover text for each bar
hover_text = [f"{team}<br>Years: {years[team]}" for team in teams]

# Step 3: Create the interactive bar chart
fig = go.Figure(data=[
    go.Bar(
        x=teams,
        y=wins,
        text=wins,                      # Shows win count on the bar
        textposition='auto',
        hovertext=hover_text,          # Custom hover showing years
        hoverinfo="text",
        marker_color='steelblue'
    )
])

# Step 4: Customize layout
fig.update_layout(
    title='ODI Cricket World Cup Titles by Country',
    xaxis_title='Teams',
    yaxis_title='Number of Titles',
    template='plotly_white'
)

# Step 5: Show the interactive plot
fig.show()
