from rest_framework import serializers
from .models import Skills, Profile, Launch


class MethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ['title', 'id']


class ProfileSerializer(serializers.ModelSerializer):
    # methods = MethodSerializer(many=True, read_only=True)
    id = serializers.CharField(read_only=True)

    class Meta:
        depth = 1
        model = Profile
        fields = ['id', 'name', 'photo', "methods"]


class LaunchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Launch
        fields = ['update', 'data']
