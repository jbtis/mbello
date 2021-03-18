from django.db import models


class ContactMe(models.Model):
    item_to_copy = models.CharField(max_length=50)
