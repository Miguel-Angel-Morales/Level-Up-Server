
"""View module for handling requests about game """
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Gamer


class GamerView(ViewSet):
    """Level up gamer  view"""

    def retrieve(self, request, pk):
        gamer_type = Gamer.objects.get(pk=pk)
        serializer = GamerSerializer(gamer_type)
        return Response(serializer.data)


    def list(self, request):
        gamer = Gamer.objects.all()
        serializer = GamerSerializer(gamer, many=True)
        return Response(serializer.data)

class GamerSerializer(serializers.ModelSerializer):
    """JSON serializer for gamer 
    """
    class Meta:
        model = Gamer
        fields = ('id', 'user', 'bio')
