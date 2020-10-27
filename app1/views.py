from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
from .models import CaronaData, Asset, SubmitedAssets
from .graph import genarate_bar_graph
from django_pandas.io import read_frame
from users.decorators import my_login_required
from django.template.loader import render_to_string

# Create your views here.
@my_login_required
def index(request):
    carona = CaronaData.objects.all()
    df = read_frame(carona)
    context = {
    "data" : CaronaData.objects.all(),
    # "graph1" : genarate_bar_graph(df),
    # "graph2" : genarate_bar_graph(df),
    "assets1" : Asset.objects.all()[0:10],
    "assets2" : Asset.objects.all()[10:20],
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
def submit_asset(request, asset=None):
    if request.session.get('user', False):
        user = request.session.get('user')
        sa = SubmitedAssets(userid=user, asset_name=asset)
        sa.save()
        return redirect(index)
    else:
        return redirect('login')