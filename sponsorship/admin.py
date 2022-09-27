from django.contrib import admin

from sponsorship.models import SponsorNote, Sponsorship

# Register your models here.
@admin.register(Sponsorship)
class SponsorshipAdmin(admin.ModelAdmin):
    list_display=['title','description','image','created_on']
@admin.register(SponsorNote)
class SponsorNoteAdmin(admin.ModelAdmin):
    list_display=['title','description','image','created_on']