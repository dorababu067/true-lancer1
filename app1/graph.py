import plotly.offline as pyo
import plotly.graph_objects as go

def genarate_bar_graph(df=None, option=None):
    """Expecting DataFrame , Creating Graph using the input DataFrame"""
    if option == 'deaths':
        data = [go.Bar(x=df.country, y=df.deaths, name="County Cases")]
        layout = go.Layout(title="Carona deaths country wise")
        figure = go.Figure(data=data, layout=layout)
        graph = pyo.plot(figure, output_type='div')
        return graph
    elif option == 'population':
        data = [go.Bar(x=df.country, y=df.population, name="County Cases")]
        layout = go.Layout(title="Population By country wise")
        figure = go.Figure(data=data, layout=layout)
        graph = pyo.plot(figure, output_type='div')
        return graph
    elif option == 'cases':
        data = [go.Bar(x=df.country, y=df.cases, name="County Cases")]
        layout = go.Layout(title="Carona Cases country wise")
        figure = go.Figure(data=data, layout=layout)
        graph = pyo.plot(figure, output_type='div')
        return graph
    else:
        data = [go.Bar(x=df.country, y=df.cases, name="County Cases")]
        layout = go.Layout(title="Carona Cases country wise")
        figure = go.Figure(data=data, layout=layout)
        graph = pyo.plot(figure, output_type='div')
        # print(graph)
        return graph