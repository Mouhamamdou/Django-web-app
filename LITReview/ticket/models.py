from django.db import models
from django.conf import settings
from PIL import Image


class Ticket(models.Model):

    title = models.fields.CharField(max_length=128)
    description = models.fields.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tickets')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    time_created = models.fields.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def is_ticket(self):
        return True

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)
            # if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size, Image.Resampling.LANCZOS)
            img.save(self.image.path)
