from django.urls import path
from .views import (
    MeepListCreateAPIView, MeepDetailAPIView, ProfileAPIView,
    FollowUnfollowAPIView, SearchMeepAPIView, MeepLikeAPIView,
)

urlpatterns = [
    path('meeps/', MeepListCreateAPIView.as_view(), name='meep-list-create'),
    path('meeps/<int:pk>/', MeepDetailAPIView.as_view(), name='meep-detail'),
    path('profile/<int:pk>/', ProfileAPIView.as_view(), name='profile-detail'),
    path('profile/follow/<int:pk>/', FollowUnfollowAPIView.as_view(), name='follow-unfollow'),
    path('meeps/search/', SearchMeepAPIView.as_view(), name='search-meep'),
    path('meeps/<int:pk>/like/', MeepLikeAPIView.as_view(), name='meep-like'),
]
