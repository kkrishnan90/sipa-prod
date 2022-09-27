from django.contrib import admin

from about.models import About, CommitteMembers

# Register your models here.
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display=['title','description','created_on']

@admin.register(CommitteMembers)
class CommitteeAdmin(admin.ModelAdmin):
    list_display=['name','designation','description','image','created_on']    