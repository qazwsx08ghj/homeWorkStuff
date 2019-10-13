from django.contrib.auth.models import User
from .models import userProfile, userArticle
# include database
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'last_name', 'first_name', 'email', 'groups']


class userProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = userProfile
        fields = ['hobbies', 'selfIntroduction']


class userArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = userArticle
        fields = ['USER', 'Article_writer', 'Article_title']
