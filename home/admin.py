from django.contrib import admin

from home.models import Announcement, Footer, Gallery, LatestNews, Members, Slider, Sponsors, WelcomeNote


# Register your models here.
@admin.register(Members)
class SliderAdmin(admin.ModelAdmin):
    list_display=['founding_member','name','email','phone','family_size','membership_number','created_on']
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display=['title','sub_title','description','created_on']
@admin.register(WelcomeNote)
class WelcomeNoteAdmin(admin.ModelAdmin):
    list_display=['title','description','created_on']
@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display=['title','description','created_on']
@admin.register(LatestNews)
class LatestNewsAdmin(admin.ModelAdmin):
    list_display=['title','description','created_on']
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display=['title','image','created_on']
# @admin.register(Sponsors)
# class SponsorsAdmin(admin.ModelAdmin):
#     list_display=['image','created_on']
@admin.register(Footer)
class SliderAdmin(admin.ModelAdmin):
    list_display=['email','logo','short_description','phone',]