from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


class SimulationSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Session #{self.id} for {self.user.username}"




class VirtualBalance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('100000.00'))  # Starting amount

    def __str__(self):
        return f"{self.user.username} Balance: {self.balance}"


class SimulatedTrade(models.Model):
    TRADE_SIDES = [
        ('buy', 'Buy'),
        ('sell', 'Sell'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    asset = models.CharField(max_length=20)
    side = models.CharField(max_length=4, choices=TRADE_SIDES)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_value(self):
        return self.amount * self.price

    def __str__(self):
        return f"{self.user.username} - {self.side.upper()} {self.amount} {self.asset} @ {self.price}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"
class Post(models.Model):
    title = models.CharField(max_length=100)         # Short text field for post title
    content = models.TextField()                     # Large text field for post content
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when post was created
    updated_at = models.DateTimeField(auto_now=True)      # Timestamp for when post was last updated

    def __str__(self):
        return self.title