from django.contrib import admin

from muhammadyor.models import Profile, Post


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', )
