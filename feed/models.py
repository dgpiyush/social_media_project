from django.db import models

from django.contrib.auth import get_user_model

# Get the user model
User = get_user_model()

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_message = models.ForeignKey("Message", on_delete=models.CASCADE, null=True, blank=True)
    liked_comment = models.ForeignKey("Comment", on_delete=models.CASCADE, null=True, blank=True)


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, through=Like, related_name="liked_messages")

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, through=Like, related_name="liked_comments")
