from rest_framework import serializers

from files.models import File


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = [
            'id',
            'title',
            'size',
            'upload_date',
            'download_last_date',
            'comment',
            'path',
            'download_link',
            'upload'
        ]

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)



        # title = models.CharField(max_length=128)
        # size = models.CharField()
        # upload_date = models.DateTimeField(auto_now_add=True)
        # download_last_date = models.DateTimeField()
        # comment = models.TextField()
        # path = models.CharField()
        # download_link = models.CharField()
        # upload = models.FileField()