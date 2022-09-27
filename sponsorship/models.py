from pydoc import describe
from django.db import models

# Create your models here.
class Sponsorship(models.Model):
    class Meta:
        verbose_name_plural = "Sponsorships"
    title = models.CharField(max_length=600)
    description = models.TextField()
    image = models.ImageField(upload_to='sponsorship')
    created_on = models.DateField(auto_now_add=True)
    

class SponsorNote(models.Model):
    class Meta:
        verbose_name_plural = "Sponsor Note"
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='sponsor_note')
    created_on = models.DateField(auto_now_add=True)