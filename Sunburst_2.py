import plotly.express as px
import pandas as pd
import numpy as np

### Import data from the excel file and delete the null rows
useful_columns = [0,1,2]
df = pd.read_excel('/Users/cem_ataman/Desktop/sunburst_diagrams.xlsx', sheet_name = 'sunburst2', usecols=useful_columns)
df['child'].replace(" ", np.nan, inplace=True)
df.dropna(subset=['child'], inplace=True)

###create our lists with parent and child values
parent = [str(x) for x in df['parent'].values.tolist()]
print('parent: ', parent)

child_int = [int(x) for x in df['child'].values.tolist()]
child = [str(x) for x in child_int]
print('child: ' , child)
print(len(child))

value = [int(x) for x in df['value'].values.tolist()]
print('value: ', value)

# print(len(parent))
# print(len(child))
# print(len(value))

###create our data as dictionary
data = dict(
    character=child,
    parent=parent,
    # value=value
    )

### Define the Sunburst features
fig = px.sunburst(
    data,
    names='character',
    parents='parent',

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
    # maxdepth= -1,
)

### locate figure on plot by distance (top, left, right, bottom)
fig.update_layout(margin=dict(t=100, l=100, r=0, b=0))
fig.show()
