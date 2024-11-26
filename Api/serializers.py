from rest_framework import serializers
from django.contrib.auth.models import User
from musker.models import Meep, Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class MeepSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Meep
        fields = '__all__'

    def get_likes_count(self, obj):
        return obj.likes.count()

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    followers_count = serializers.SerializerMethodField()
    follows_count = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = '__all__'

    def get_followers_count(self, obj):
        return obj.followed_by.count()

    def get_follows_count(self, obj):
        return obj.follows.count()
