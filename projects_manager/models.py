from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Location(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()


class Project(models.Model):
    name = models.CharField(max_length=600)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return str(self.name) + ' project - ' + str(self.customer)
