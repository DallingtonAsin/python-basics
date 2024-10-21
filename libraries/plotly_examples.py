# Plotly Open Source Graphing Library for Python
# Plotly's Python graphing library makes interactive, publication-quality graphs.
# Examples of how to make line plots, scatter plots, area charts, bar charts,
# error bars, box plots, histograms, heatmaps, subplots, multiple-axes, polar charts, and bubble charts.


# Installation
# pip install plotly
# plotly.express depends on pandas so you have to install pandas by
# using pip install pandas

import plotly.express as px


country = input("Enter country name: ")
data = {
    'Country': [country],
    'Values': [100]
}

fig = px.choropleth(
    data,
    locations='Country',
    locationmode='country names',
    color='Values',
    color_continuous_scale='Inferno',
    scope='africa',
    title=f'Country Map Highlighting - {country}'
)
fig.show()
