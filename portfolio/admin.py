from django.contrib import admin
from .models import Ability #added class from models.py

admin.site.register(Ability) #This line of code means, that i can see this model inside admin panel
