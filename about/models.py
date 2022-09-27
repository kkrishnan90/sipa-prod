from django.db import models

# Create your models here.
class About(models.Model):
    class Meta:        
        verbose_name_plural = "About"
    title = models.CharField(max_length=500)
    short_description = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='about')
    created_on = models.DateField(auto_now_add=True)

class CommitteMembers(models.Model):
    class Meta:
        verbose_name_plural = "Committe Members"
    name = models.CharField(max_length=200)    
    image = models.ImageField(upload_to='committee_members')
    designation = models.CharField(max_length=200)
    description = models.CharField(max_length=250,blank=True)
    created_on = models.DateField(auto_now_add=True)