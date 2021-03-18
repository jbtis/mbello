from django.db import models


class Contacts(models.Model):
    item = models.CharField(max_length=50)

