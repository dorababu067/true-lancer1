from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import CaronaData, Asset
from .graph import genarate_bar_graph
from django_pandas.io import read_frame
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    carona = CaronaData.objects.all()
    df = read_frame(carona)
    context = {
    "data" : CaronaData.objects.all(),
    "graph1" : genarate_bar_graph(df),
    "graph2" : genarate_bar_graph(df),
    "assets1" : Asset.objects.all()[0:10],
    "assets2" : Asset.objects.all()[10:20],
    }
    return render(request, 'index2.html', context)

def dynamic_graph(request):
    if request.method == 'POST':
        val = request.POST['graph-options']
        data = CaronaData.objects.all().order_by('-id')[0:50]
        df = read_frame(data)
        context = {
            "graph": genarate_bar_graph(df=df, option=val)
        }
        return JsonResponse(context, safe=False)

def dynamic_table(request):
    if request.method == 'POST':
        country = request.POST['country1']
        context = { "data" :CaronaData.objects.filter(country__icontains=country) }
        html = render_to_string("search_table_data.html",context)
        return JsonResponse(html, safe=False)