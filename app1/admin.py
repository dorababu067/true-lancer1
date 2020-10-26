from django.contrib import admin
from app1.models import CaronaData, Asset, SubmitedAssets
# Register your models here.

admin.site.register(CaronaData)
admin.site.register(Asset)
admin.site.register(SubmitedAssets)
