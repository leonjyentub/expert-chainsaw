from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'
    fk_name = 'user'

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture')
    search_fields = ('user__username', 'user__email')

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

# Unregister the original User admin and register the customised one
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Also register Profile for direct access/managing
admin.site.register(Profile, ProfileAdmin)
