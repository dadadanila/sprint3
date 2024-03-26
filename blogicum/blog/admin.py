from django.contrib import admin

from .models import Category, Location, Post

admin.site.register(Post, admin.ModelAdmin)
admin.site.register(Location, admin.ModelAdmin)
admin.site.register(Category, admin.ModelAdmin)
