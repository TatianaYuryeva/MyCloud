from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance):
    return f'{instance.user.username}'


class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    size = models.CharField()
    upload_date = models.DateTimeField(auto_now_add=True)
    download_last_date = models.DateTimeField()
    comment = models.TextField()
    path = models.CharField()
    download_link = models.CharField()
    upload = models.FileField(upload_to=user_directory_path)


