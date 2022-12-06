import plotly.graph_objects as go
import plotly.express as px

### in otder to upload it online
# import chart_studio
# import chart_studio.plotly as py
# chart_studio.tools.set_credentials_file(username='xxx', api_key='xxx')

### Upload required data manually
fig =go.Figure(go.Sunburst(

    ids=[
        "Urban Intervention", "Participation Tools",
        "Urbanism", "Community", "Sustainability", "Building Types", "Participation_int",
        "Participation_tl", "Digital Tools", "Representation", "Responsive Cities",
        "Urban Policies", "Economy", "Smart Cities", "Transportation", "Urban Heritage",
        "Interactive & Cultural Int.", "Art-based Int.", "Socio-spatial int.",
        "Urban Sustainability", "Performative Buildings",
        "Museums", "Housing", "Religious Places", "Theaters", "Food Markets", "Playgrounds", "Schools",
        "Participatory Urban Practices",
        "Participants", "Social Inclusion", "Gamification",
        "Tools for Remote Participation", "The Use of the Tools", "The Development of the Tools",
        "Visualization", "Interaciton",
        "Transportation_pt", "Sustainability_pt", "Urban Policies & Governance", "Citizenship"


    ],

    labels=["URBAN<br>INTERVENTION", "PARTICIPATION<br>TOOLS",
            "Urbanism", "Community", "Sustainability", "Building Types", "Participation",
            "Participation", "Digital Tools", "Representation", "Responsive Cities" ,
            "Urban Policies", "Economy", "Smart Cities", "Transportation", "Urban Heritage",
            "Interactive<br>& Cultural Interventions", "Art-based<br>Interventions", "Socio-spatial<br> Interventions",
            "Urban Sustainability", "Performative Buildings",
            "Museums", "Housing", "Religious Places", "Theaters", "Food Markets", "Playgrounds", "Schools",
            "Participatory<br>Urban Practices",
            "Participants", "Social Inclusion", "Gamification",
            "Tools for<br>Remote Participation", "The Use of<br>the Tools", "The Development of<br>the Tools",
            "Visualization", "Interaciton",
            "Transportation", "Sustainability", "Urban Policies<br>& Governance", "Citizenship"
            ],
    insidetextorientation='radial',

    parents=["", "",
             "Urban Intervention", "Urban Intervention", "Urban Intervention", "Urban Intervention", "Urban Intervention",
             "Participation Tools", "Participation Tools", "Participation Tools", "Participation Tools",
             "Urbanism","Urbanism","Urbanism","Urbanism","Urbanism",
             "Community","Community","Community",
             "Sustainability","Sustainability",
             "Building Types","Building Types","Building Types","Building Types","Building Types","Building Types","Building Types",
             "Participation_int",
             "Participation_tl","Participation_tl","Participation_tl",
             "Digital Tools","Digital Tools","Digital Tools",
             "Representation","Representation",
             "Responsive Cities","Responsive Cities","Responsive Cities","Responsive Cities"


             ],
    rotation= 90 ,
    values=[  93,76,
              40,24,15,10,4,
              19,32,4,21 ,
              16,5,10,6,3,
              5,12,7,
              13,2,
              1,3,2,1,1,1,1,
              4,

              9,5,5,
              6,17,9,
              2,2,
              1,9,6,5
              ],
    branchvalues="total",
))


fig.update_layout(uniformtext=dict(minsize=8, mode='hide'),)
fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))
fig.show()

# py.plot(fig, filename = 'Sunburst Chart', auto_open=True)