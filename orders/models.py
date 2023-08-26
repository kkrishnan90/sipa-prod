from django.db import models

# Create your models here.
class OrderModel(models.Model):
    class Meta:
        verbose_name_plural = "Orders"
    csrf_token = models.CharField(max_length=400)
    name = models.CharField(max_length=300)
    email = models.EmailField()
    event_date = models.CharField(max_length=100)
    event_name = models.CharField(max_length=300)
    qr_code_img_url = models.URLField(max_length=1000)
    family_count = models.PositiveIntegerField()
    prasad_count = models.PositiveIntegerField()
    phone = models.CharField(max_length=30)
    is_verified = models.BooleanField(default=False)
    created_on = models.DateField(auto_now_add=True)


class NonMemberModel(models.Model):
    class Meta:
        verbose_name_plural="Non Members"
    member_id = models.CharField(max_length=30,blank=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    family_count = models.PositiveIntegerField()
    prasad_count = models.PositiveIntegerField()
