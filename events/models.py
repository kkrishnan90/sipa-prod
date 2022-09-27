from django.db import models

# Create your models here.
class Events(models.Model):
    class Meta:
        verbose_name_plural = "Events"
    title = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='events')
    date = models.DateField()
    created_on = models.DateField(auto_now_add=True)

    @property
    def formatted_date(self):
        return str(self.date).replace('-','/')

