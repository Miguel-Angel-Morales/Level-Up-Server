
"""View module for handling requests about event types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event, Gamer, Game


class EventView(ViewSet):
    """Level up event types view"""

    def retrieve(self, request, pk):
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def list(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized event instance
        """
        organizer = Gamer.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=request.data["game"])

        event = Event.objects.create(
            date=request.data["date"],
            time=request.data["time"],
            event_name=request.data["event_name"],
            description=request.data["description"],
            organizer=organizer,
            game=game
        )

        serializer = EventSerializer(event)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for an event

        Returns:
            Response -- Empty body with 204 status code
        """

        event = Event.objects.get(pk=pk)
        event.event_name = request.data["event_name"]
        event.date = request.data["date"]
        event.time = request.data["time"]
        #event.attendees = request.data["attendees"]
        event.description = request.data["description"]

        gamer = Gamer.objects.get(pk=request.data["organizer"])
        event.organizer = gamer

        game = Game.objects.get(pk=request.data["game"])
        event.game = game

        event.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        


class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for event types
    """

    class Meta:
        model = Event
        fields = ('id', 'organizer', 'date', 'time',
                  'attendees', 'event_name', 'description', 'game')
