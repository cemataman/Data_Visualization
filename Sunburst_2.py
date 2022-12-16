import plotly.express as px
import pandas as pd
import numpy as np

### Import data from the excel file and delete the null rows
df = pd.read_excel('/Users/cem_ataman/PycharmProjects/Data_Visualization/Sunburst_Data.xlsx', sheet_name = 'Sheet1')

###create our lists with parent and child values
parent = [str(x) for x in df['root'].values.tolist()]
print('parent: ', parent)

child_int = [str(x) for x in df['branch'].values.tolist()]
child = [str(x) for x in child_int]
print('child: ' , child)

label = [str(x) for x in df['Comment Text'].values.tolist()]
print('label: ' , label)

# value = [int(x) for x in df['value'].values.tolist()]
# print('value: ', value)

###create our data as dictionary
data = dict(
    character=child,
    parent=parent,
    labels=label,
    # value=value
    )

### Define the Sunburst features
fig = px.sunburst(
    data,
    names='character',
    parents='parent',
    hover_name="labels",
    # hover_data={'comment': False},

    ### define color
    color="parent",
    # color_discrete_sequence=px.colors.qualitative.Pastel, ### if it is textual data
    color_continuous_scale=px.colors.sequential.Aggrnyl,  ### if it is numeric data
    range_color=[1, 10],

    ### define text
    branchvalues="total",  ### or 'remainder'
    # hover_name="comment",
    # hover_data={'comment': False},
    title="CEM ATAMAN",
    template='ggplot2',  ### 'ggplot2', 'seaborn', 'simple_white', 'plotly',
                         ### 'plotly_white', 'plotly_dark', 'presentation',
                         ### 'xgridoff', 'ygridoff', 'gridon', 'none'
    maxdepth= -1,
)

### locate figure on plot by distance (top, left, right, bottom)
fig.update_layout(margin=dict(t=50, l=0, r=0, b=0),
                  coloraxis_colorbar_x=0.8, #location of the legend
                  title=dict(y=0.9, font=dict(size=15))) # size of the plot title

### update the size and font of the colorbar legend
# fig.update_coloraxes(colorbar_len=0.5,
#                      colorbar_thickness=15,
#                      colorbar_tickfont_size=10)

### hide the colorbar legend
fig.update_coloraxes(showscale=False)

fig.show()
