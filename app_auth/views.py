from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from app_auth.serializers import UserSerializer


# Create your views here.
@api_view(['POST'])
def register(request):
    serialiser = UserSerializer(data = request.data)
    if serialiser.is_valid():
        serialiser.save()
        return Response(serialiser.data, status = status.HTTP_201_CREATED)
    
    return Response(serialiser.errors, status = status.HTTP_400_BAD_REQUEST)