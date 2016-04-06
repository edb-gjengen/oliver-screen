from rest_framework.response import Response
from rest_framework.views import APIView

from oliver_screen.lastfm import get_track_data, get_last_track_data


class LastTrackView(APIView):
    def get(self, request, format=None):
        return Response({'track': get_last_track_data()})


class CurrentTrackView(APIView):
    def get(self, request, format=None):
        return Response({'track': get_track_data()})
