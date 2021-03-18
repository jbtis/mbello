from django.db import models


# Note: makemigrations creates the migration file
# Object inside the parenthesis is inheritance
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100)

    # Images
    image1 = models.CharField(max_length=100)
    image1_caption = models.TextField()
    image2 = models.CharField(max_length=100)
    image2_caption = models.TextField()
    image3 = models.CharField(max_length=100)
    image3_caption = models.TextField()

