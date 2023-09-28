from django.db import models


class File(models.Model):
    title = models.CharField(max_length=128)
    size = models.CharField()
    upload_date = models.DateTimeField(auto_now_add=True)
    download_last_date = models.DateTimeField()
    comment = models.TextField()
    path = models.CharField()
    download_link = models.CharField()
    upload = models.FileField(upload_to='test')


