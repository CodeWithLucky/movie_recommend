from rest_framework import serializers
from .models import *
from faker import Faker

class StreamingPlatformSerializer(serializers.Serializer):
    class Meta:
        model = StreamingPlatform
        fields = '__all__'
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model : User
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'



class ViewedMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewedMovie
        fields = '__all__'


