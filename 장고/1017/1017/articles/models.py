from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(blank=True,upload_to='images/')
    thumbnail = ProcessedImageField(upload_to='images/', blank=True,
                                           processors=[ResizeToFill(1200, 960)],
                                           format='JPEG',
                                           options={'quality':80})