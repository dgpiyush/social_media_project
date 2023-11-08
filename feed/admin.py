from django.contrib import admin
from .models import Like, Message, Comment

# Register your models here.
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'liked_message', 'liked_comment')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'content', 'created_at')
