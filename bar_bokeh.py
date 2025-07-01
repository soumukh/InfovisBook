# Step 1: Import required libraries
import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, HoverTool

# Step 2: Read data from CSV file
df = pd.read_csv('odi_wc_winners.csv')

# Step 3: Create a ColumnDataSource for Bokeh
source = ColumnDataSource(df)

# Step 4: Prepare output HTML file
output_file("odi_wc_bokeh.html")

# Step 5: Create a figure for the bar chart
p = figure(
    x_range=df['Team'],              # Set x-axis categories from team names
    height=500,
    title="ODI Cricket World Cup Winners",
    toolbar_location=None,
    tools="hover",                   # Add hover tool for interactivity
    tooltips=[                       # Define what to show on hover
        ("Team", "@Team"),
        ("Wins", "@Champions"),
        ("Years", "@Years")
    ]
)

# Step 6: Draw the bars
p.vbar(
    x='Team',
    top='Champions',
    width=0.6,
    source=source,
    color="navy"
)

# Step 7: Customize plot aesthetics
p.xgrid.grid_line_color = None
p.y_range.start = 0
p.xaxis.axis_label = "Team"
p.yaxis.axis_label = "Number of Wins"
p.title.text_font_size = '16pt'

# Step 8: Show the interactive plot in the browser
show(p)
