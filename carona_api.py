import json
import requests
import pandas as pd
import django
import os
import time
import schedule
from datetime import datetime




# for accesing the models these lines mandatory.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_project.settings')
django.setup()

from app1.models import CaronaData

now = datetime.now()
curent = now.strftime("%H:%M:%S")
print(curent)
#getting the data from the API
def carona_live_data():
    url = "https://covid-193.p.rapidapi.com/statistics"

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "345f529b75msh54ef897a76821c9p1ebb47jsn761311f759a8"
    }

    response = requests.request("GET", url, headers=headers)
    carona_data_all = []
    raw_data = json.loads(response.text)
    for data in raw_data["response"]:
        carona_data = {}
        carona_data['country'] = data['country']
        carona_data['population'] = data['population']
        carona_data['cases'] = data['cases']['total']
        carona_data['deaths'] = data['deaths']['total']
        carona_data['day'] = data['day']
        carona_data['time'] = data['time']
        carona_data['current_time'] = curent
        carona_data_all.append(carona_data)
    return carona_data_all

    # df = pd.DataFrame(carona_data_all)
    # print(df)


#storing the API data into django Model
def populated_data_into_db():
    print("Populating data.....")
    data = carona_live_data()
    for row in data:
        CaronaData.objects.create(**row)
    print("data populated succesfully")


populated_data_into_db()