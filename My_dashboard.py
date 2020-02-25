import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd 
import dash_table

import plotly.graph_objs as go
import plotly.express as px

from Workspace_insight import workspace_insight_plot,workspace_benefits_plot

df=pd.read_csv('./Data/survey.csv')
dfc=pd.read_csv('./Data/new.csv')

navbar = dbc.NavbarSimple(
    children=[
        
        dbc.DropdownMenu(
            nav=True,
            in_navbar=True,
            label="Menu",
            children=[
                dbc.DropdownMenuItem("Home",href="/"),
                dbc.DropdownMenuItem("Understanding Data",href="/understand_data"),
                dbc.DropdownMenuItem("Exploratory Data Analysis",href="/exploratory_data_analysis"),
                
            ],
        ),
    ],
    brand="Mental Health Survey",
    brand_href="/",
    sticky="top",
    color="dark",
    dark=True,
)

footer = dbc.NavbarSimple(
    
    brand=" ",
    color="dark",
    dark=True,
    
    sticky="down",
    fixed="bottom"
)

homepage_body = dbc.Container(
    [
        dbc.Row(
            [ dbc.Col(
                    [
                        html.H1("Data"),
                        dash_table.DataTable(
                            id='table',
                            columns=[{"name": i, "id": i} for i in df.columns],
                            data=df.to_dict('records'),
                            style_table={
                            'padding':'15px',
                            'maxWidth':'900px',
                            'overflowX': 'scroll',
                            'maxHeight': '400px',
                            'overflowY': 'scroll',
                            },
                            style_cell={'textAlign': 'left'},
                            style_cell_conditional=[
                                {'if': {'column_id': 'comments'},
                                        'width': '30%'},
       
                                ]
                            ),

                    ]
                ),
                dbc.Col(
                    [
                        html.H2("About Mental Health Survey Data"),
                        html.P(
                            """\
This data set is taken from Kaggle. This is a dataset from a 2014 survey (over 1200 responses recieved) that measures attitudes towards mental health and frequency of mental health disorders in workplaces. Goal
Our goal is to find out the key factors to mental health problems in the workplace. We are going to perform some descriptive analysis on the survey data and predict treatment based on predictors. This will help in finding out methods to improve worker's experience in a tech workplace.
"""),
html.P(
                            """\
Describing the Data:There are altogether 1200 rows i.e. observations and 27 Columns which are given below :\n
"""),
html.P("""1. Timestamp """),
html.P("""2. Age"""),
html.P("""3. Gender"""),
html.P("""4. Country"""),
html.P("""5. state: If you live in the United States, which state or territory do you live in?"""),
html.P("""6.self_employed: Are you self-employed?"""),
html.P("""7. family_history: Do you have a family history of mental illness?"""),
html.P("""8. treatment: Have you sought treatment for a mental health condition?"""),
html.P("""9. work_interfere: If you have a mental health condition, do you feel that it interferes with your work?"""),
html.P("""10. no_employees: How many employees does your company or organization have?"""),
html.P("""11. remote_work: Do you work remotely (outside of an office) at least 50% of the time?"""),
html.P("""12. tech_company: Is your employer primarily a tech company/organization?"""),
html.P("""13. benefits: Does your employer provide mental health benefits?"""),
html.P("""14. care_options: Do you know the options for mental health care your employer provides?"""),
html.P("""15. wellness_program: Has your employer ever discussed mental health as part of an employee wellness program?"""),
html.P("""16. seek_help: Does your employer provide resources to learn more about mental health issues and how to seek help?"""),
html.P("""17. anonymity: Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources?"""),
html.P("""18. leave: How easy is it for you to take medical leave for a mental health condition?"""),
html.P("""19. mental_health_consequence: Do you think that discussing a mental health issue with your employer would have negative consequences?"""),
html.P("""20. phys_health_consequence: Do you think that discussing a physical health issue with your employer would have negative consequences?"""),
html.P("""21. coworkers: Would you be willing to discuss a mental health issue with your coworkers?"""),
html.P("""22. supervisor: Would you be willing to discuss a mental health issue with your direct supervisor(s)?"""),
html.P("""23. mental_health_interview: Would you bring up a mental health issue with a potential employer in an interview?"""),
html.P("""24. phys_health_interview: Would you bring up a physical health issue with a potential employer in an interview?"""),
html.P("""25. mental_vs_physical: Do you feel that your employer takes mental health as seriously as physical health?"""),
html.P("""26. obs consequence: Have you heard of or observed negative consequences for coworkers with mental health conditions in your workplace?"""),
                    ],
                    md=12,
                ),
        
        html.Div(style={
            'height':'100px'
         }),
            ]
        )
    ],
    className="mt-6",
)


explore_data= dbc.Container(
    [   html.Div(style={
        'height':'50px'
    }),
        dbc.Row([
            
            dbc.Col(
                [
                    html.H3("If you have a mental health condition, do you feel that it interferes with your work?"),
                    dcc.Graph(
                        id='work_interfere',
                        figure = {
                            'data':[ go.Pie(values=[465,144,264,213,173], labels=['Sometimes', 'Often', 'Unknown', 'Never','Rarely'])],
                            'layout': dict(
                                xaxis={ 'title': 'Answer'},
                                yaxis={'title': 'Count'},                                
                                hovermode='closest'
                                ),
                        },                 
                    ),
                    html.P("Insights: Close to 50% people claimed that they often encounter interference with their work due to their mental health issues.")

                ]
            ),
            
        ]),
        html.Hr(),
        html.Div(style={
        'height':'50px'
         }),
        dbc.Row([
            dbc.Col(
                [
                    html.H3("Finding insights based on work environment"),
                    dcc.Graph(
                        
                        figure = workspace_insight_plot(),

                    
                    ),
                ]
            ),
        
        ]),
        html.P("Insights:"),
        html.P("1. A large proportion of the surveyors think that there would be negative consequences for discussing a mental health issues with their employer while some are not sure about that."),
        html.P("2. A large proportion of surveyors are willing to discuss their mental health with their co-workers, showing a positive and healthy work environment in most of the tech companies."),
        html.P("4. More people are willing to discuss mental health issues with supervisors as compared to discussion with the co-workers."),
        html.P("5. Majority of people have not seen negative consequences for co-workers with mental health issues in their workplace but some have."),
            
        html.Hr(),
        html.Div(style={
        'height':'50px'
         }),
        dbc.Row([
            dbc.Col(
                [
                    html.H3("Finding insights based on workspace benefits"),
                    dcc.Graph(
                        
                        figure = workspace_benefits_plot(),

                    
                    ),
                ]
            ),
        
        ]),
    html.Div(style={
        'height':'100px'
    }),
    html.Hr(),
    html.H2('Summary:'),
    html.H3('For Employers –'),
    html.P('-    More than 50% of employees are suffering from mental health issues. So, employers should mandate the provision health programs to its employees'),
    html.P('-    Allow flexible work environment – Flexible scheduling, Modified break schedule, Work from home/Flexi-place'),
    html.P('-    Provide day-to-day guidance and feedback. Also, positive praise and reinforcement will be beneficial to employees'),
    html.H3('For Employees –'),
    html.P('-    Employees should talk to employers about their mental health issues so that they can aid them with benefit provisions like working from home, extra leaves etc.'),
    html.P('-    Employees should be aware of their health coverage and aid programs provided by their employer and should actively participate in any wellness program.'),
    html.P('-    Proper feedback should be given related to effectiveness of the employer’s health program while leaving the organization. This might help in improving existing health policies.'),
    html.Div(style={
        'height':'100px'
    }),
    ]
)


understand= dbc.Container(
    [   html.Div(style={
        'height':'50px'
    }),
        dbc.Row([
            
            dbc.Col(
                [
                    html.H3("Employment status of survey participants"),
                    dcc.Graph(
                        id='self_employed_rate',
                        figure = {
                            'data':[ go.Histogram(x=dfc["self_employed"])],
                            'layout': dict(
                                xaxis={ 'title': 'Self employed'},
                                yaxis={'title': 'Count'},                                
                                hovermode='closest'
                                ),
                        },

                    
                    ),
                ]
            ),
            dbc.Col(
                [
                    html.H3("Age of survey participants"),
                    dcc.Graph(
                        id='age',
                        figure = {
                            'data':[ go.Histogram(x=dfc["age_bins"])],
                            'layout': dict(
                                xaxis={ 'title': 'Age Range'},
                                yaxis={'title': 'Count'},                                
                                hovermode='closest'
                                ),
                        },

                    
                    ),
                ]
            ),
        ]),
        html.Div(style={
        'height':'50px'
         }),
        dbc.Row([
            dbc.Col(
                [
                    html.H3("Survey participants sought treatment related to mental health"),
                    dcc.Graph(
                        id='treatment',
                        figure = {
                            'data':[ go.Histogram(x=dfc['treatment'])],
                            'layout': dict(
                                xaxis={ 'title': 'Treatment sought'},
                                yaxis={'title': 'Count'},                                
                                hovermode='closest'
                                ),
                        },

                    
                    ),
                ]
            ),
            
            dbc.Col(
                [
                    html.H3("Family History related to Mental Health of survey participants"),
                    dcc.Graph(
                        id='family_history',
                        figure = {
                            'data':[ go.Histogram(x=dfc['family_history'])],
                            'layout': dict(
                                xaxis={ 'title': 'Family History'},
                                yaxis={'title': 'Count'},                                
                                hovermode='closest'
                                ),
                        },

                    
                    ),
                ]
            ),
        ]),
        html.Div(style={
        'height':'50px'
         }),
        dbc.Row([
            dbc.Col(
                [
                    html.H3("Country of survey participants"),
                    dcc.Graph(
                        id='country',
                        figure = {
                            'data':[ go.Histogram(x=dfc['Country'])],
                            'layout': dict(
                                xaxis={ 'title': 'Country'},
                                yaxis={'title': 'Count'},                                
                                hovermode='closest'
                                ),
                        },

                    
                    ),
                ]
            ),
            
            
        ]),
    html.Div(style={
        'height':'100px'
    }),
    ]
)


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

homepage = html.Div([navbar, homepage_body,footer])
explore_data_page = html.Div([navbar, explore_data,footer])
understand_data_page = html.Div([navbar,understand,footer])


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])



# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/understand_data':
        return understand_data_page
    elif pathname == '/exploratory_data_analysis':
        return explore_data_page
    else:
        return homepage
    


if __name__ == "__main__":
    app.run_server(debug=True)