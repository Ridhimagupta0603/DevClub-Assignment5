from django.db import models

# Create your models here.
class Doc(models.Model):
    file = models.FileField(upload_to='files/', null=True, blank=True)
    file_name = models.CharField(max_length=255)
    def __str__(self):
        return self.file_name