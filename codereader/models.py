from django.db import models


class Repository(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    origin_url = models.CharField(max_length=255, blank=True)
    homepage_url = models.URLField(max_length=255, blank=True)
