import plotly.express as px
import pandas as pd

### Import data from the excel file
df = pd.read_excel('/Users/cem_ataman/Desktop/sunburst_diagrams.xlsx', sheet_name = 'sunburst1')

### Define the Sunburst features
fig = px.sunburst(
    data_frame=df,
    path=["CID", 'Argument', "reply1", "reply2", "reply3", "reply4", "reply5"],  # Root, branches, leaves

    ### define color
    color="color",
    # color_discrete_sequence=px.colors.qualitative.Pastel, ### if it is textual data
    color_continuous_scale=px.colors.sequential.dense,  ### if it is numeric data
    range_color=[1,10],

    ### define text
    branchvalues="remainder",  ### or 'remainder'
    hover_name="comment",
    hover_data={'comment': False},
    title="CEM ATAMAN",
    template='ggplot2',    ### 'ggplot2', 'seaborn', 'simple_white', 'plotly',
                           ### 'plotly_white', 'plotly_dark', 'presentation',
                           ### 'xgridoff', 'ygridoff', 'gridon', 'none'
)

### choose what to show as labels in the figure
fig.update_traces(textinfo='label')

### locate figure on plot by distance (top, left, right, bottom)
fig.update_layout(margin=dict(t=100, l=100, r=0, b=0))
fig.show()

