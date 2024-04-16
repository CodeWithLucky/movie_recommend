from django.db import models

# Create your models here.

class StreamingPlatform(models.Model):
    name = models.CharField(max_length=100, null = True)
    about = models.CharField(max_length=200, null = True)
    website = models.URLField(max_length=200, null = True)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.username

class Movie(models.Model):
    name = models.CharField(max_length=255)
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Rating(models.Model):
    m_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.rating.to_eng_string()

class ViewedMovie(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    platform_id = models.ForeignKey(StreamingPlatform, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,  on_delete=models.CASCADE)

    def __str__(self):
        return self.movie_id.name


class PlatformRecommend(models.Model):
    pass