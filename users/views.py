from django.shortcuts import render  # Provides shortcuts for rendering templates
from rest_framework.decorators import api_view  # Decorator for views that should be called via the REST API
from rest_framework.response import Response  # Wrapper for returning responses with content type as JSON

from .serializers import UserSerializer  # Serializes data to/from Python data types and JSON for user models
from rest_framework import status  # Contains HTTP status codes for response status
from rest_framework.authtoken.models import Token  # Manages authentication tokens for users
from django.contrib.auth.models import User  # Django's built-in user model

from django.shortcuts import get_object_or_404
# Create your views here.
@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username = request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"detail": "Not found."}, status = status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance = user)
    return Response({"token": token.key, "user":serializer.data})

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username = request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user":serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response({"passed for": request.user.email})