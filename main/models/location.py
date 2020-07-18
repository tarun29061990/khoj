from django.db import models


class Location(models.Model):
    class Meta:
        db_table = 'locations'
    name = models.CharField(max_length=255)
    popularity = models.IntegerField(max_length=11)
    created_at = models.DateTimeField("created_at", auto_now_add=True)
    updated_at = models.DateTimeField("updated_at", auto_now=True)
