from django.db import models

# Example model: Post for a blog app
class Post(models.Model):
    title = models.CharField(max_length=100)         # Short text field for post title
    content = models.TextField()                     # Large text field for post content
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when post was created
    updated_at = models.DateTimeField(auto_now=True)      # Timestamp for when post was last updated

    def __str__(self):
        return self.title