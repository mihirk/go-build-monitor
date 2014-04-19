from django.db import models
from django.forms import forms, ModelForm



class Configuration(models.Model):
    pipeline_url = models.URLField(verbose_name="Go Pipeline CCtray XML")
    username = models.CharField(verbose_name="Username", null=True, max_length=128)
    password = models.CharField(verbose_name="Password", null=True, max_length=128)

class BuildsToMonitor(models.Model):
    build = models.CharField(verbose_name="Build Name", max_length=256)
    configuration = models.ForeignKey(Configuration)