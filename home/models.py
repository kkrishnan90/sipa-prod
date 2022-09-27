from django.db import models

class Members(models.Model):
    class Meta:
        verbose_name_plural = "Members"
    founding_member = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    family_size = models.IntegerField()
    membership_number = models.CharField(max_length=50)
    created_on = models.DateField(auto_now_add=True,blank=True)


class Slider(models.Model):
    class Meta:
        verbose_name_plural = "Sliders"
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='home_slider')
    description= models.CharField(max_length=200)
    created_on = models.DateField(auto_now_add=True)

class WelcomeNote(models.Model):
    class Meta:
        verbose_name_plural = "WelcomeNote"
    title = models.CharField(max_length=300)
    description= models.TextField()
    left_image = models.ImageField(upload_to='mission',default=None)
    right_image = models.ImageField(upload_to='mission',default=None)
    created_on = models.DateField(auto_now_add=True)

class Announcement(models.Model):
    class Meta:
        verbose_name_plural = "Announcements"
    title = models.CharField(max_length=300)
    description= models.TextField()
    created_on = models.DateField(auto_now_add=True)

class LatestNews(models.Model):
    class Meta:
        verbose_name_plural = "Latest News"
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='latest_news')
    description= models.TextField()
    created_on = models.DateField(auto_now_add=True)

class Gallery(models.Model):
    class Meta:
        verbose_name_plural = "Gallery"
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery')
    created_on = models.DateField(auto_now_add=True)

class Sponsors(models.Model):
    class Meta:
        verbose_name_plural = "Sponsorships"
    image = models.ImageField(upload_to='sponsors')
    created_on = models.DateField(auto_now_add=True)

class Footer(models.Model):
    class Meta:
        verbose_name_plural = "Footer Content"
    logo = models.ImageField(upload_to='footer')
    short_description=models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    