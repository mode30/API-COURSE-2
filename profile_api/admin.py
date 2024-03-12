from django.contrib import admin
from profile_api import models
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display=['name','email','is_staff','is_active']
    

admin.site.register(models.UserProfile,UserProfileAdmin)