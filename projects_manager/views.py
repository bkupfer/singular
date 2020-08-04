from django.core import serializers
from django.shortcuts import render
from .models import Project, Customer
import json


def index(request):
    customers = Customer.objects.all()
    customers_json = serializers.serialize('json', customers)
    return render(request, "index.html", {"data": customers_json})
