import time
import json
import pandas
from django.shortcuts import render, redirect
from django.http import JsonResponse, StreamingHttpResponse
from django.core import serializers
from .models import CaronaData, Asset, SubmitedAssets
from .graph import genarate_bar_graph, asset_graph, excel_data_to_graph
from django_pandas.io import read_frame
from users.decorators import my_login_required
from django.template.loader import render_to_string
from django.db import connection
from django.core.serializers.json import DjangoJSONEncoder
from .raw_querys import my_query
from .excel_static import convert_df_to_html

# Create your views here.
@my_login_required
def index(request):
    carona = CaronaData.objects.all()
    # df = read_frame(carona)
    df, html = convert_df_to_html()
    context = {
    # "data" : CaronaData.objects.all(),
    # "graph1" : genarate_bar_graph(df),
    # "graph2" : genarate_bar_graph(df),
    "graph": asset_graph(),
    "assets1" : Asset.objects.all()[0:10],
    "assets2" : Asset.objects.all()[10:20],
    "html": html,
    "excel_graph": excel_data_to_graph(df),
    }
    return render(request, 'index.html', context)


@my_login_required
def dynamic_graph(request):
    if request.method == 'POST':
        val = request.POST['graph-options']
        data = CaronaData.objects.all().order_by('-id')[0:50]
        df = read_frame(data)
        context = {
            "graph": genarate_bar_graph(df=df, option=val)
        }
        return JsonResponse(context, safe=False)

@my_login_required
def dynamic_table(request):
    if request.method == 'POST':
        country = request.POST['country1']
        context = { "data" :CaronaData.objects.filter(country__icontains=country) }
        html = render_to_string("search_table_data.html",context)
        return JsonResponse(html, safe=False)

@my_login_required
def submit_asset(request, asset=None, timeremaining=None):
    print(timeremaining)
    if request.session.get('user', False):
        user = request.session.get('user')
        sa = SubmitedAssets(userid=user, asset_name=asset, timeremaining=timeremaining)
        sa.save()
        return redirect(index)
    else:
        return redirect('login')

#streaming data
def event_stream():
    initial_data = ""
    while True:
        result = my_query()
        data = json.dumps(list(result),cls=DjangoJSONEncoder)
        # print(data)
        if not initial_data == data:
            yield "\ndata: {}\n\n".format(data) 
            initial_data = data
            # print(initial_data)
        time.sleep(1)

def caron_live_data(request):
        response = StreamingHttpResponse(event_stream())
        response['Content-Type'] = 'text/event-stream'
        # print(response.readable)
        return response



#streaming data
def dash_event_stream():
    initial_data = ""
    while True:
        result = Asset.objects.all().values()
        data = json.dumps(list(result),cls=DjangoJSONEncoder)
        # print(data)
        # print(data)
        if not initial_data == data:
            yield "\ndata: {}\n\n".format(data) 
            initial_data = data
            # print(initial_data)
        time.sleep(1)

def dashboard_live_data(request):
        response = StreamingHttpResponse(dash_event_stream())
        response['Content-Type'] = 'text/event-stream'
        return response


def asset_graph_view(request):
    if request.method == "GET":
        value = request.GET["option"]
        context = {
            "graph": asset_graph(value)
        }
        
        return JsonResponse(context, safe=False)

def excel_data_view(request):
     if request.method == "GET":
        value = request.GET["option"]
        df, html = convert_df_to_html(field=value)
        context = {
            "html": html,
            "graph":excel_data_to_graph(df)
        }
        
        return JsonResponse(context, safe=False)