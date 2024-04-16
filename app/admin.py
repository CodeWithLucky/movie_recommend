from django.contrib import admin
from . models import *
# Register your models here.
class StreamingAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'about', 'website'
    ]

class MovieAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'duration'
    ]

class RatingAdmin(admin.ModelAdmin):
    list_display = [
        'm_id', 'rating', 'user_id'
    ]

class UserAdmin(admin.ModelAdmin):
    list_display = [
        'username' , 'email'
    ]

class ViewedMovieAdmin(admin.ModelAdmin):
    list_display = [
        'movie_id', 'platform_id', 'user_id'
    ]
admin.site.register(StreamingPlatform, StreamingAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(ViewedMovie, ViewedMovieAdmin)
