import plotly
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
dfc=pd.read_csv('./Data/new.csv')

def workspace_insight_plot():
    trace1 = go.Histogram(
        x=dfc['leave'],
        name="How easy is it for you to take medical leave for a mental health condition?"
    )
    trace2 = go.Histogram(
        x=dfc['mental_health_consequence'],
        name="Do you think that discussing a mental health issue with your employer would have negative consequences?",
    )
    trace3 = go.Histogram(
        x=dfc['coworkers'],
        name="Would you be willing to discuss a mental health issue with your coworkers?",
    )
    trace4 = go.Histogram(
        x=dfc['supervisor'],
        name="Would you be willing to discuss a mental health issue with your direct supervisor(s)?",
    )
    trace5 = go.Histogram(
        x=dfc['obs_consequence'],
        name="Have you heard of or observed negative consequences for coworkers with mental health conditions in your workplace?"
    )
    fig = plotly.subplots.make_subplots(rows=3, cols=2, specs=[[{},{}], [{},{}],[{},{}]],
                            shared_xaxes=False, shared_yaxes=False,
                            subplot_titles=("Plot 1", "Plot 2", "Plot 3", "Plot 4","Plot 5"))
    fig.append_trace(trace1, 1, 1)
    fig.append_trace(trace2, 1, 2)
    fig.append_trace(trace3, 2, 1)
    fig.append_trace(trace4, 2, 2)
    fig.append_trace(trace5, 3, 1)

    fig['layout'].update(height=900,legend=dict(x=-.1, y=1.2))

    return fig


def workspace_benefits_plot():
    trace1 = go.Histogram(
        x=dfc['benefits'],
        name="Does your employer provide mental health benefits?"
    )
    trace2 = go.Histogram(
        x=dfc['care_options'],
        name="Do you know the options for mental health care your employer provides?",
    )
    trace3 = go.Histogram(
        x=dfc['wellness_program'],
        name="Has your employer ever discussed mental health as part of an employee wellness program?",
    )
    trace4 = go.Histogram(
        x=dfc['seek_help'],
        name="Does your employer provide resources to learn more about mental health issues and how to seek help?",
    )
    
    fig = plotly.subplots.make_subplots(rows=2, cols=2, specs=[[{},{}], [{},{}]],
                            shared_xaxes=False, shared_yaxes=False,
                            subplot_titles=("Plot 1", "Plot 2", "Plot 3", "Plot 4"))
    fig.append_trace(trace1, 1, 1)
    fig.append_trace(trace2, 1, 2)
    fig.append_trace(trace3, 2, 1)
    fig.append_trace(trace4, 2, 2)
    

    fig['layout'].update(height=800,legend=dict(x=-.1, y=1.2))

    return fig