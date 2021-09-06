from django.shortcuts import render
from rest_framework import viewsets


# Create your views here.
from rest_framework.decorators import action
from rest_framework.response import Response

from product.models import Track
from product.serializers import TrackSerializer


class TrackView(viewsets.GenericViewSet):
    @action(methods=['GET'], detail=False, url_name='unit1', url_path='unit1')
    def unit_one_track(self, request, *args, **kwargs):
        qs = Track.objects.filter(unit_price__gt= 1)
        qs_serializer = TrackSerializer(qs, many=True)
        return Response(data={'result': qs_serializer.data}, status=200)

    @action(methods=['GET'], detail=False, url_name='unit1', url_path='all')
    def all_track(self, request, *args, **kwargs):
        qs = Track.objects.all()
        qs_serializer = TrackSerializer(qs, many=True)
        return Response(data={'result': qs_serializer.data}, status=200)