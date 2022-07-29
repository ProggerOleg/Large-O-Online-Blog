from django.contrib import admin
from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'image', 'author')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'author')
    list_filter = ('time_create', 'author')
    prepopulated_fields = {'url': ('title',)}


admin.site.register(Post, PostAdmin)
