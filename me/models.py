from django.db import models


# Note: Could have created a hardcoded html file for intro but this is more fun :)
class Introduction(models.Model):
    title = models.CharField(max_length=60)
    about_me = models.TextField()
    call_to_action = models.TextField()
    image = models.CharField(max_length=100)
