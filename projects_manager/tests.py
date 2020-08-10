from django.test import TestCase
from .models import Client, Project, Location
from .views import fetch_client_projects


class ProjectManager(TestCase):
    def setUp(self):
        test_client = Client.objects.create(name="Hans Zimmer")
        test_locs = [Location.objects.create(lat=72.123, lon=-34.213),
                     Location.objects.create(lat=75.856, lon=-36.233)]
        Project.objects.create(name="Lipzig", client=test_client, location=test_locs[0])
        Project.objects.create(name="Studgard", client=test_client, location=test_locs[1])

    def test_fetch_projects(self):
        projects_list = fetch_client_projects()
        self.assertEqual(len(projects_list), 2)
        for project in projects_list:
            self.assertEqual(project['Client'], "Hans Zimmer")
