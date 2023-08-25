import os
import numpy as np
import plotly.graph_objects as go
import pandas as pd

# Folder path where the filtered CSV file is located
folder_path = "/Users/rita/Thesis/Survey/Data From Sites/Analysis/Site E - Sussex/"

# Input filtered CSV file name
filtered_filename = "output_filtered.csv"  # Replace with the actual file name

# Full path to the filtered CSV file
filtered_file_path = os.path.join(folder_path, filtered_filename)

# Create a dictionary to store item counts
item_counts = {}

# Read the filtered CSV file
with open(filtered_file_path, 'r') as file:
    for line in file:
        item = line.split(',')[0]
        if item in item_counts:
            item_counts[item] += 1
        else:
            item_counts[item] = 1

# Create a pie chart
fig = go.Figure(data=[go.Pie(
    labels=list(item_counts.keys()),
    values=list(item_counts.values()),
    textinfo='label+percent',  # Show label and percentage inside the pie chart slices
    insidetextfont=dict(size=20),  # Increase font size of inside text
    outsidetextfont=dict(size=20)  # Increase font size of outside text
)])

# Set the title in the center and increase font size
fig.update_layout(
    title_text="Species of Bats Recorded",
    title_x=0.5,  # Title alignment
    title_font=dict(size=36),  # Increase title font size
    showlegend=False  # Hide the legend
)

# Add the date annotation to the side
fig.add_annotation(
    text="Date: 2023-08-03",
    x= 1,  # Adjust x-coordinate for the side position
    y=0.5,   # Adjust y-coordinate for the center position
    showarrow=False,  # Don't show an arrow
    font=dict(size=20)  # Set font size
)

# Add the site annotation to the side
fig.add_annotation(
    text="Site: Sussex",
    x=1,  # Adjust x-coordinate for the side position
    y=0.4,   # Adjust y-coordinate for the center position
    showarrow=False,  # Don't show an arrow
    font=dict(size=20)  # Set font size
)

# Show the pie chart
fig.show()
