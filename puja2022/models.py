from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Puja(models.Model):
    class Meta:
        verbose_name_plural = "Puja 2022"
    title = models.CharField(max_length=400)
    content = RichTextField()
    created_on = models.DateField(auto_now_add=True)