from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Resources(models.Model):
    class Meta:
        verbose_name_plural = "Resources"
    title = models.CharField(max_length=500)
    description = RichTextField()
    created_on = models.DateField(auto_now_add=True)