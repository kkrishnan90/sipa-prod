from django.db import models

# Create your models here.
class Contact(models.Model):
    class Meta:
        verbose_name_plural = "Contact"
    address = models.CharField(max_length=500)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    created_on= models.DateField(auto_now_add=True)

