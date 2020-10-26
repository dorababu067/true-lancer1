from django.contrib import admin
from .models import User, LoginDetails

# Register your models here.

admin.site.register(User)
admin.site.register(LoginDetails)
