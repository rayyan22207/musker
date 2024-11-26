from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from musker.models import Meep, Profile
from .serializers import MeepSerializer, ProfileSerializer, UserSerializer

class MeepListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        meeps = Meep.objects.all().order_by('-created_at')
        serializer = MeepSerializer(meeps, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MeepSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeepDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return Meep.objects.get(pk=pk)

    def get(self, request, pk):
        meep = self.get_object(pk)
        serializer = MeepSerializer(meep)
        return Response(serializer.data)

    def delete(self, request, pk):
        meep = self.get_object(pk)
        if request.user == meep.user:
            meep.delete()
            return Response({"message": "Meep deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)

    def put(self, request, pk):
        meep = self.get_object(pk)
        if request.user == meep.user:
            serializer = MeepSerializer(meep, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)


class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            profile = Profile.objects.get(user_id=pk)
        else:
            profile = request.user.profile
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, pk=None):
        profile = request.user.profile
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FollowUnfollowAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        profile_to_follow = Profile.objects.get(user_id=pk)
        current_profile = request.user.profile
        if profile_to_follow in current_profile.follows.all():
            current_profile.follows.remove(profile_to_follow)
            action = "unfollowed"
        else:
            current_profile.follows.add(profile_to_follow)
            action = "followed"
        current_profile.save()
        return Response({"message": f"You have {action} {profile_to_follow.user.username}."})


class SearchMeepAPIView(APIView):
    def post(self, request):
        search_query = request.data.get('search', '')
        results = Meep.objects.filter(body__icontains=search_query)
        serializer = MeepSerializer(results, many=True)
        return Response(serializer.data)


class MeepLikeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        meep = Meep.objects.get(pk=pk)
        if request.user in meep.likes.all():
            meep.likes.remove(request.user)
            action = "unliked"
        else:
            meep.likes.add(request.user)
            action = "liked"
        meep.save()
        return Response({"message": f"You have {action} the meep."})
