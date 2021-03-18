from django.db import models


class ProjectsInProgress(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    image1 = models.CharField(max_length=100)
    image1_caption = models.TextField()
    progress = models.DecimalField(decimal_places=0, max_digits=2)
