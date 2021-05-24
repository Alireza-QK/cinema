from django.contrib import admin
from .models import Movie, Cinema, ShowTime

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'director', 'year', 'length', 'country', 'language', 'description')


admin.site.register(Movie, MovieAdmin)
admin.site.register(Cinema)
admin.site.register(ShowTime)
