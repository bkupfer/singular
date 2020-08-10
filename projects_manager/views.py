from django.shortcuts import render, redirect
from .models import Client


def index(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')

    json_data = fetch_client_projects()
    return render(request, "index.html", {"data": json_data})


def fetch_client_projects():
    json_data = []
    clients = Client.objects.all().prefetch_related('projects')
    for c in clients:
        for p in c.projects.all():
            json_data.append({
                'name': p.name,
                'Client': c.name,
                'location': str(p.location),
            })
    return json_data
