from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

class Transaction(models.Model):
    amount = models.FloatField(validators=[MinValueValidator(0.01)])
    date_created = models.DateTimeField(default=timezone.now)
    from_user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='sender', null=True)
    to_user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='receiver', null=True)
    from_username = models.CharField(max_length=255, null=True)
    to_username = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f'{self.amount}: {self.from_user.username} -> {self.to_user.username}'

    def get_absolute_url(self):
        return reverse('transactions', kwargs={'username': self.from_user.username})
