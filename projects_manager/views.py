from django.core import serializers
from django.shortcuts import render
from .models import Project, Client
import json


def index(request):
    json_data = []
    clients = Client.objects.all().prefetch_related('projects')
    for c in clients:
        print(c.projects)
        for p in c.projects.all():
            json_data.append({
                'name': p.name,
                'Client': c.name,
                'location': str(p.location),
            })
    return render(request, "index.html", {"data": json_data})
