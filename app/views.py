from django.shortcuts import render
from . serializer import *
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from rest_framework import viewsets
from django.db.models import Count, Max



# Create your views here.
class StreamingView(APIView):
    def get(self, request):
        try:
            result = StreamingPlatform.objects.all()
            serializer = StreamingPlatformSerializer(result, many = True)
            return Response(serializer.data, status=200)
        
        except StreamingPlatform.DoesNotExist:
            return Response(serializer._errors, status=404)
        

    def post(self, request):
        try:
            serializer = StreamingPlatformSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            else:
                return Response(serializer.errors, status=400)
        except ValidationError as e:
            return Response({"error": str(e)}, status=400)
        except Exception as e:
            return Response({"error": "An unexpected error occurred"}, status=500)
        


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class RatingView(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class ViewMovieView(viewsets.ModelViewSet):
    queryset = ViewedMovie.objects.all()
    serializer_class = ViewedMovieSerializer


    
class RecommendMovieView(viewsets.ViewSet):
    def list(self, request):
        # Aggregate the count of each platform in ViewMovie
        platform_counts = ViewedMovie.objects.values('platform_id__name').annotate(count=Count('platform_id'))

        # Find the maximum count value
        max_count = platform_counts.aggregate(max_count=Max('count'))['max_count']

        # Filter platform_counts to get platforms with the maximum count
        max_platforms = platform_counts.filter(count=max_count)

        # Return the list of platform names with the maximum count
        platform_names = [platform['platform_id__name'] for platform in max_platforms]
        
        return Response({'platforms_with_max_count': platform_names, 'max_count': max_count})