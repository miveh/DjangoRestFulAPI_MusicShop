from django.contrib import admin

# Register your models here.
import product
from product.models import Artist, Track, Album,MediaType,Genre

admin.site.register(Artist)
admin.site.register(Track)
admin.site.register(Album)
admin.site.register(MediaType)
admin.site.register(Genre)