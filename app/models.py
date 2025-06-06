from django.db import models
from cms.models.pluginmodel import CMSPlugin

class MyPluginModel(CMSPlugin):
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title
