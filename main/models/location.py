from django.db import models


class Location(models.Model):
    class Meta:
        db_table = 'locations'
    name = models.CharField(max_length=255)
    count = models.IntegerField(max_length=11)