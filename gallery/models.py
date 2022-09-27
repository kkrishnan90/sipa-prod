from django.db import models

# Create your models here.
class Gallery(models.Model):
    class Meta:
        verbose_name_plural = "Gallery"
    image = models.ImageField(upload_to='gallery')
    created_on = models.DateField(auto_now_add=True)

