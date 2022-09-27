from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Membership(models.Model):
    class Meta:
        verbose_name_plural = "Memberships"
    title = models.CharField(max_length=500)
    description = RichTextField()
    created_on = models.DateField(auto_now_add=True)
