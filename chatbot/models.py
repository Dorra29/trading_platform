from django.db import models
from django.contrib.auth.models import User

class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_message = models.TextField()
    bot_reply = models.TextField()
    personality = models.CharField(max_length=50, default="gen_z")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} at {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

class ChatHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_history')  # Links to the User model
    user_message = models.TextField()  # The message sent by the user
    bot_reply = models.TextField()  # The response from the bot
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the message was sent

    def __str__(self):
        return f"Chat with {self.user.username} at {self.created_at}"