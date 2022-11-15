from rest_framework import serializers
from .models import Project, Audio


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class AudioSerializer(serializers.ModelSerializer):
    processed_text = serializers.ListField(read_only=True)

    class Meta:
        model = Audio
        fields = (
            "id",
            "create_time",
            "update_time",
            "index",
            "text",
            "speed",
            "path",
            "processed_text",
        )


class AudioDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ("text", "speed")
