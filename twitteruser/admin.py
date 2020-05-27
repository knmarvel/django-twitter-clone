from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from twitteruser.models import TwitterUser


class TwitterUserAdmin(UserAdmin):
    list_display = ('username', 'display_name', 'is_staff', 'is_active',)
    list_filter = ('username', 'display_name', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'display_name', 'following',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )


# Register your models here.
admin.site.register(TwitterUser, TwitterUserAdmin)
