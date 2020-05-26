from django.db import models

class Ability(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=256)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
