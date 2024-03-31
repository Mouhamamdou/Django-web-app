from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from ticket.models import Ticket
from django.conf import settings


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    headline = models.CharField(max_length=128)
    body = models.fields.TextField(max_length=8192, blank=True)
    time_created = models.fields.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} for {self.ticket.title}'

    def is_review(self):
        return True
