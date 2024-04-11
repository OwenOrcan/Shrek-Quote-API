from django.db import models

class Quote(models.Model):
    quote = models.CharField(max_length=255)
    movie = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.quote

