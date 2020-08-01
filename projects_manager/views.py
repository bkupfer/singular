from django.shortcuts import render
from .models import Project, Customer


def index(request):
    customers = Customer.objects.all()
    return render(request, "index.html", {"customers": customers})
