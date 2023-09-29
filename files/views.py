from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from files.models import File
from files.serializers import FileSerializer


class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)