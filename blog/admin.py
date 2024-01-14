from django.contrib import admin
from .models import Post, Comment
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'text', 'created', 'updated']
    prepopulated_fields = {'slug':('title',)}
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'text', 'text']