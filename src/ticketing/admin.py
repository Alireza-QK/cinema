from django.contrib import admin
from .models import Movie, Cinema, ShowTime

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'director', 'year', 'length', 'country', 'language', 'description')


class CinemaAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'capacity', 'phone', 'address')


admin.site.register(Movie, MovieAdmin)
admin.site.register(Cinema, CinemaAdmin)
admin.site.register(ShowTime)
