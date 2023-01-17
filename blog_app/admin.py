from django.contrib import admin
from .models import *

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'image', 'author')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'author')
    list_filter = ('time_create', 'author')
    prepopulated_fields = {'url': ('title',)}

    def get_tags(self, instance):
        return [tag.name for tag in instance.tags.all()]


class ComentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'created_date', 'post_id', 'username_id')
    list_filter = ('created_date', 'post_id')
#
# class TagAdmin(admin.ModelAdmin):
#     list_display = ('name', 'slug')
#     search_fields = ('name',)
#     prepopulated_fields = {'slug': ('name',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, ComentsAdmin)
# admin.site.register(Tag, TagAdmin)
