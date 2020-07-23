from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=80)
    text = models.TextField()
    image = models.ImageField(blank=True, upload_to='blog/images/')
    date = models.DateField()

    def __str__(self):
        return self.title