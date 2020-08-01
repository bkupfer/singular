from django.contrib import admin

from .models import Customer, Location, Project

admin.site.register(Customer)
admin.site.register(Project)
admin.site.register(Location)
