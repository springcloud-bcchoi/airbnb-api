from rest_framework import viewsets
from .models import Room
from .serializers import BigRoomSeralizer


class RomViewset(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = BigRoomSeralizer
