import plotly.offline as pyo
import plotly.graph_objects as go
from .raw_querys import my_query
import pandas

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


# assset submition graph
def asset_graph(option=None):
    if option == None:
        result = my_query()
        df = pandas.DataFrame(result)
        data = [go.Bar(x=df.userid, y=df.totalcount)]
        layout = go.Layout(title="Asset Submition")
        figure = go.Figure(data=data, layout=layout)
        graph = pyo.plot(figure, output_type='div')
        return graph
    if option == "userid":
        result = my_query()
        df = pandas.DataFrame(result)
        data = [go.Bar(x=df.userid, y=df.totalcount)]
        layout = go.Layout(title="Asset Submition Based on the userid")
        figure = go.Figure(data=data, layout=layout)
        graph = pyo.plot(figure, output_type='div')
        return graph
    if option == "asset":
        result = my_query()
        df = pandas.DataFrame(result)
        data = [go.Bar(x=df.asset_name, y=df.totalcount)]
        layout = go.Layout(title="Asset Submition Based on the asset")
        figure = go.Figure(data=data, layout=layout)
        graph = pyo.plot(figure, output_type='div')
        return graph

def excel_data_to_graph(df):
    data1 = go.Bar(name = 'CAT1', x = df.Asset, y = df.CAT1) 
    data2 = go.Bar(name = 'CAT2', x = df.Asset, y = df.CAT2) 
    data3 = go.Bar(name = 'CAT3', x = df.Asset, y = df.CAT3) 
    data4 = go.Bar(name = 'CAT4', x = df.Asset, y = df.CAT4) 
    data = [data1, data2, data3, data4]
    layout = go.Layout(title="Asset Submition category wise")
    figure = go.Figure(data=data, layout=layout)
    graph = pyo.plot(figure, output_type='div')
    return graph