from django.urls import path
from . import views


urlpatterns = [
    path('', views.StreamingView.as_view(), name='StreamingView'),
    path('user/', views.UserView.as_view({'get' : 'list', 'post' : 'create'}), name='userView'),
    path('list/', views.RecommendMovieView.as_view({'get' : 'list'}), name='recommend')
]
